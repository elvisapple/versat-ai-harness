"""Behavioral checks for SDD metadata, sequencing, evidence and compatibility.

Every dossier lives in a temporary synthetic repository. Approval records are
test data: these checks establish content binding, never human authenticity.
Run with ``python -m unittest discover -s tests/validators -p 'test_*.py'``.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml


SOURCE_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = SOURCE_ROOT / "validators" / "sdd" / "validate.py"
SPEC = importlib.util.spec_from_file_location("versat_sdd_validator", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class SddValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="versat-sdd-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.change_id = "greeting-button"
        self.change = self.root / "specs" / "changes" / self.change_id
        self.change.mkdir(parents=True)
        self.data = {
            "proposal": {
                "sdd_version": 2,
                "change": self.change_id,
                "status": "proposed",
                "owner": "Synthetic developer",
                "summary": "Add a greeting button to the home screen.",
                "risk": "low",
                "review": self.review(),
            },
            "requirements": {
                "sdd_version": 2,
                "change": self.change_id,
                "requirements": [{
                    "id": "REQ-001",
                    "statement": "The home screen button displays Hello world.",
                    "acceptance": ["Activating the button displays Hello world."],
                }],
            },
            "design": {
                "sdd_version": 2,
                "change": self.change_id,
                "requirements": ["REQ-001"],
                "adrs": [],
                "validation": [{
                    "id": "CHECK-001",
                    "description": "Check the greeting button interaction.",
                    "requirements": ["REQ-001"],
                    "required": True,
                }],
                "review": self.review(),
            },
            "tasks": {
                "sdd_version": 2,
                "change": self.change_id,
                "tasks": [{
                    "id": "TASK-001",
                    "description": "Add the greeting button and interaction test.",
                    "requirements": ["REQ-001"],
                    "status": "pending",
                }],
                "review": self.review(),
                "validation": {"plan_digest": None, "results": []},
                "closure": "active",
            },
        }
        self.compat_bindings = {}
        self.body = {
            "proposal": "# Greeting button\n\nAdd a greeting in the existing home screen.\n",
            "requirements": "# Requirements\n\nREQ-001 defines the greeting interaction.\n",
            "design": "# Design\n\nReuse the existing button and message components.\n",
            "tasks": "# Tasks\n\n- [ ] TASK-001 — Add the greeting button and interaction test.\n",
        }

    @staticmethod
    def review():
        return {
            "revision": 1,
            "state": "awaiting-approval",
            "blockers": [],
            "upstream": {},
            "approval": None,
        }

    def write(self, name):
        metadata = yaml.safe_dump(self.data[name], sort_keys=False, allow_unicode=True)
        (self.change / f"{name}.md").write_text(
            f"---\n{metadata}---\n\n{self.body[name]}", encoding="utf-8"
        )
        self.bind_v2_fixture()

    def bind_v2_fixture(self):
        """Explicit synthetic in-flight admission; never update a captured digest."""
        if self.data['proposal'].get('sdd_version') != 2:
            return
        for stage in ('proposal', 'design', 'tasks'):
            needed = ('proposal', 'requirements') if stage == 'proposal' else (stage,)
            if stage not in self.compat_bindings and all((self.change / f'{n}.md').exists() for n in needed):
                self.compat_bindings[stage] = self.digest(stage)
        path = self.root / 'sdd' / 'compatibility.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({'version': 1, 'historical': {}, 'in_flight': {
            self.change_id: {'reason': 'Synthetic v2 in-flight contract fixture, not actual human approval.',
                             'digests': {n: self.compat_bindings.get(n, '0' * 64) for n in ('proposal', 'design', 'tasks')}}}}))

    def begin(self):
        self.write("proposal")
        self.write("requirements")

    def digest(self, stage):
        return VALIDATOR.stage_digest(self.change, stage)

    def approve(self, stage):
        review = self.data[stage]["review"]
        review["state"] = "approved"
        review["blockers"] = []
        review["upstream"] = {
            name: self.digest(name)
            for name in {"proposal": [], "design": ["proposal"],
                         "tasks": ["proposal", "design"]}[stage]
        }
        self.write(stage)
        review["approval"] = {
            "source": f"synthetic-chat/{stage}/message-1",
            "quote": f"I approve the {stage} presented in this synthetic test.",
            "revision": review["revision"],
            "digest": self.digest(stage),
        }
        self.write(stage)

    def approved_plan(self):
        self.begin()
        for stage in ("proposal", "design", "tasks"):
            self.approve(stage)

    def complete(self):
        self.data["tasks"]["tasks"][0]["status"] = "completed"
        self.body["tasks"] = self.body["tasks"].replace("- [ ]", "- [x]")
        self.write("tasks")

    def passing_evidence(self):
        evidence = self.root / "docs" / "evidence" / "greeting.txt"
        evidence.parent.mkdir(parents=True, exist_ok=True)
        evidence.write_text("Synthetic CHECK-001: interaction passed.\n", encoding="utf-8")
        self.data["tasks"]["validation"] = {
            "plan_digest": self.digest("tasks"),
            "results": [{
                "check": "CHECK-001",
                "result": "pass",
                "evidence": "docs/evidence/greeting.txt",
                "revision": "synthetic-working-tree-1",
            }],
        }
        self.write("tasks")

    def ready(self):
        self.approved_plan()
        self.complete()
        self.passing_evidence()

    def result(self, phase="planning", change_id=None):
        result = VALIDATOR.validate_repository(self.root, phase=phase, change_id=change_id)
        self.assertIn(result["status"], {"pass", "fail", "unable-to-verify"})
        self.assertIsInstance(result["findings"], list)
        return result

    def assert_status(self, expected, phase="planning", change_id=None):
        result = self.result(phase, change_id)
        self.assertEqual(expected, result["status"], json.dumps(result, indent=2))
        return result

    def make_legacy(self):
        compatibility = self.root / 'sdd' / 'compatibility.json'
        if compatibility.exists():
            compatibility.unlink()
        for name in self.data:
            self.data[name].pop("sdd_version", None)
            self.data[name].pop("review", None)
        self.data["design"]["validation"] = ["Check the greeting button interaction."]
        self.data["tasks"].pop("validation", None)
        self.data["tasks"].pop("closure", None)
        for name in self.data:
            self.write(name)
        manifest = {
            "version": 1,
            "changes": {self.change_id: {
                "reason": "Immutable pre-v2 fixture; no historical approvals asserted.",
                "files": {
                    f"{name}.md": hashlib.sha256(
                        (self.change / f"{name}.md").read_bytes()
                    ).hexdigest() for name in self.data
                },
            }},
        }
        path = self.root / "sdd" / "legacy-changes.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest), encoding="utf-8")
        return manifest

    def test_empty_repository_does_not_claim_delivery(self):
        self.change.rmdir()
        self.assert_status("pass")

    def test_proposal_and_requirements_are_valid_partial_planning(self):
        self.begin()
        self.assert_status("pass")

    def test_partial_planning_cannot_start_implementation(self):
        self.begin()
        self.assertNotEqual("pass", self.result("implementation")["status"])

    def test_design_requires_prior_proposal_approval(self):
        self.begin()
        self.write("design")
        self.assert_status("fail")

    def test_design_draft_after_proposal_approval_is_valid(self):
        self.begin()
        self.approve("proposal")
        self.data["design"]["review"]["upstream"] = {"proposal": self.digest("proposal")}
        self.write("design")
        self.assert_status("pass")

    def test_tasks_require_prior_design_approval(self):
        self.begin()
        self.approve("proposal")
        self.data["design"]["review"]["upstream"] = {"proposal": self.digest("proposal")}
        self.write("design")
        self.write("tasks")
        self.assert_status("fail")

    def test_approved_plan_can_start_implementation(self):
        self.approved_plan()
        self.assert_status("pass", "implementation")

    def test_malformed_yaml_is_a_structured_failure(self):
        self.begin()
        (self.change / "proposal.md").write_text("---\nreview: [\n---\n", encoding="utf-8")
        result = self.assert_status("fail")
        self.assertTrue(result["findings"])

    def test_scalar_frontmatter_is_rejected(self):
        self.begin()
        (self.change / "proposal.md").write_text("---\nfalse\n---\n# Proposal\n", encoding="utf-8")
        self.assert_status("fail")

    def test_schema_does_not_coerce_string_revision(self):
        self.begin()
        self.data["proposal"]["review"]["revision"] = "1"
        self.write("proposal")
        self.assert_status("fail")

    def test_unversioned_new_dossier_cannot_bypass_gates(self):
        self.begin()
        self.data["proposal"].pop("sdd_version")
        self.write("proposal")
        self.assert_status("fail")

    def test_requirement_edit_invalidates_joint_proposal_approval(self):
        self.approved_plan()
        self.data["requirements"]["requirements"][0]["acceptance"] = ["Display a personalized greeting."]
        self.write("requirements")
        self.assert_status("fail")

    def test_design_body_edit_invalidates_approval(self):
        self.approved_plan()
        self.body["design"] += "\nStore every greeting in a new database table.\n"
        self.write("design")
        self.assert_status("fail")

    def test_reapproving_design_does_not_reapprove_tasks(self):
        self.approved_plan()
        self.body["design"] += "\nUse the existing dialog component for the message.\n"
        self.data["design"]["review"]["revision"] += 1
        self.approve("design")
        self.assert_status("fail")

    def test_approval_revision_must_match_artifact_revision(self):
        self.approved_plan()
        self.data["tasks"]["review"]["revision"] += 1
        self.write("tasks")
        self.assert_status("fail")

    def test_approved_stage_cannot_retain_blockers(self):
        self.approved_plan()
        self.data["design"]["review"]["blockers"] = ["Message placement unresolved."]
        self.write("design")
        self.assert_status("fail", "implementation")

    def test_v2_replanning_requires_explicit_migration(self):
        self.approved_plan()
        proposal = self.data["proposal"]["review"]
        proposal.update(state="awaiting-approval", approval=None, revision=2)
        self.data["requirements"]["requirements"][0]["statement"] = "Display a personalized greeting."
        self.write("requirements")
        self.write("proposal")
        for stage in ("design", "tasks"):
            self.data[stage]["review"].update(state="superseded", approval=None)
            self.write(stage)
        self.assert_status("fail")  # Changed in-flight v2 scope now requires migration.
        self.assertNotEqual("pass", self.result("implementation")["status"])

    def test_progress_and_evidence_do_not_invalidate_task_approval(self):
        self.approved_plan()
        original = self.digest("tasks")
        self.complete()
        self.passing_evidence()
        self.body["tasks"] += "\n## Progress\n\nCompleted locally.\n\n## Validation evidence\n\nCHECK-001 passed.\n"
        self.write("tasks")
        self.assertEqual(original, self.digest("tasks"))
        self.assert_status("pass", "delivery")

    def test_task_description_is_part_of_approved_scope(self):
        self.approved_plan()
        self.data["tasks"]["tasks"][0]["description"] = "Send each greeting to a remote service."
        self.write("tasks")
        self.assert_status("fail")

    def test_yaml_order_line_endings_and_trailing_space_do_not_change_digest(self):
        self.begin()
        original = self.digest("proposal")
        self.data["proposal"] = dict(reversed(list(self.data["proposal"].items())))
        self.write("proposal")
        path = self.change / "proposal.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_bytes(("\r\n".join(line + "  " for line in lines) + "\r\n").encode())
        self.assertEqual(original, self.digest("proposal"))

    def test_generated_review_section_does_not_hide_later_scope_section(self):
        self.begin()
        original = self.digest("proposal")
        self.body["proposal"] += "\n## Planning review\n\nWaiting for reviewer.\n"
        self.write("proposal")
        self.assertEqual(original, self.digest("proposal"))
        self.body["proposal"] += "\n## Additional scope\n\nAlso add analytics tracking.\n"
        self.write("proposal")
        self.assertNotEqual(original, self.digest("proposal"))

    def test_duplicate_requirement_ids_are_rejected(self):
        self.begin()
        self.data["requirements"]["requirements"].append(
            copy.deepcopy(self.data["requirements"]["requirements"][0])
        )
        self.write("requirements")
        self.assert_status("fail")

    def test_requirement_reference_must_resolve(self):
        self.approved_plan()
        self.data["tasks"]["tasks"][0]["requirements"] = ["REQ-999"]
        self.approve("tasks")
        self.assert_status("fail")

    def test_every_requirement_needs_required_validation_coverage(self):
        self.begin()
        self.approve("proposal")
        self.data["design"]["validation"][0]["required"] = False
        self.approve("design")
        self.assert_status("fail")

    def test_task_ids_must_be_unique(self):
        self.approved_plan()
        self.data["tasks"]["tasks"].append(copy.deepcopy(self.data["tasks"]["tasks"][0]))
        self.approve("tasks")
        self.assert_status("fail")

    def test_completed_task_requires_checked_body_item(self):
        self.approved_plan()
        self.data["tasks"]["tasks"][0]["status"] = "completed"
        self.write("tasks")
        self.assert_status("fail")

    def test_body_task_must_exist_in_metadata(self):
        self.approved_plan()
        self.body["tasks"] += "- [ ] TASK-999 — Untracked task.\n"
        self.approve("tasks")
        self.assert_status("fail")

    def test_pending_task_prevents_delivery(self):
        self.approved_plan()
        self.passing_evidence()
        self.assert_status("fail", "delivery")

    def test_required_check_without_result_is_unverified(self):
        self.approved_plan()
        self.complete()
        self.data["tasks"]["validation"]["plan_digest"] = self.digest("tasks")
        self.write("tasks")
        self.assert_status("unable-to-verify", "delivery")

    def test_explicit_failed_check_fails_delivery(self):
        self.ready()
        self.data["tasks"]["validation"]["results"][0]["result"] = "fail"
        self.write("tasks")
        self.assert_status("fail", "delivery")

    def test_unverified_check_prevents_delivery(self):
        self.ready()
        self.data["tasks"]["validation"]["results"][0]["result"] = "unverified"
        self.write("tasks")
        self.assert_status("unable-to-verify", "delivery")

    def test_local_evidence_must_exist(self):
        self.ready()
        self.data["tasks"]["validation"]["results"][0]["evidence"] = "docs/evidence/missing.txt"
        self.write("tasks")
        self.assertNotEqual("pass", self.result("delivery")["status"])

    def test_stale_plan_digest_prevents_delivery(self):
        self.ready()
        self.data["tasks"]["validation"]["plan_digest"] = "0" * 64
        self.write("tasks")
        self.assert_status("unable-to-verify", "delivery")

    def test_unknown_and_duplicate_check_results_are_rejected(self):
        self.ready()
        results = self.data["tasks"]["validation"]["results"]
        results.append(copy.deepcopy(results[0]))
        self.write("tasks")
        self.assert_status("fail", "delivery")
        results.pop()
        results[0]["check"] = "CHECK-999"
        self.write("tasks")
        self.assert_status("fail", "delivery")

    def test_prepared_closure_enforces_delivery_even_in_planning(self):
        self.approved_plan()
        self.data["tasks"]["closure"] = "prepared"
        self.write("tasks")
        self.assertNotEqual("pass", self.result()["status"])

    def test_archive_path_enforces_delivery_even_when_closure_active(self):
        self.approved_plan()
        archive = self.root / "specs" / "archive" / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        self.assertNotEqual("pass", self.result()["status"])

    def test_prepared_archive_passes_without_git_or_merge_claim(self):
        self.ready()
        self.data["tasks"]["closure"] = "prepared"
        self.write("tasks")
        archive = self.root / "specs" / "archive" / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        self.assertFalse((self.root / ".git").exists())
        self.assert_status("pass", "delivery")

    def test_duplicate_change_in_active_and_archive_is_rejected(self):
        self.ready()
        archive = self.root / "specs" / "archive" / self.change_id
        archive.mkdir(parents=True)
        for path in self.change.glob("*.md"):
            (archive / path.name).write_bytes(path.read_bytes())
        self.assert_status("fail")

    def test_exact_legacy_allowlist_exemption_does_not_verify_delivery(self):
        self.make_legacy()
        self.assert_status("pass")
        self.assert_status("unable-to-verify", "implementation")
        self.assert_status("unable-to-verify", "delivery")

    def test_modified_legacy_document_is_not_grandfathered(self):
        self.make_legacy()
        self.body["proposal"] += "\nAdditional behavior added after grandfathering.\n"
        self.write("proposal")
        self.assert_status("fail")

    def historical_archive(self):
        self.data["tasks"]["tasks"][0]["status"] = "completed"
        self.body["tasks"] = self.body["tasks"].replace("- [ ]", "- [x]")
        manifest = self.make_legacy()
        archive = self.root / "specs" / "archive" / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        evidence = self.root / "historical-merge.md"
        evidence.write_text("Synthetic merge record, not real approval evidence.\n")
        manifest["changes"][self.change_id]["historical_archive"] = {
            "merge_commit": "a" * 40,
            "evidence": "historical-merge.md",
        }
        (self.root / "sdd" / "legacy-changes.json").write_text(json.dumps(manifest))
        return manifest

    def test_historical_archive_preserves_history_without_verifying_readiness(self):
        self.historical_archive()
        result = self.assert_status("pass")
        self.assertIn("LEGACY_HISTORICAL_ARCHIVE", {item["code"] for item in result["warnings"]})
        for phase in ("implementation", "delivery"):
            with self.subTest(phase=phase):
                self.assert_status("unable-to-verify", phase)

    def test_legacy_archive_without_historical_record_is_unverified(self):
        self.make_legacy()
        archive = self.root / "specs" / "archive" / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        self.assert_status("unable-to-verify")

    def test_historical_archive_cannot_hide_changed_artifacts(self):
        self.historical_archive()
        self.body["proposal"] += "\nNew unreviewed scope.\n"
        self.write("proposal")
        self.assert_status("fail")

    def test_historical_archive_cannot_be_used_in_active_storage(self):
        self.historical_archive()
        active = self.root / "specs" / "changes" / self.change_id
        self.change.rename(active)
        self.change = active
        self.assert_status("fail")

    def test_historical_archive_requires_valid_record_and_safe_evidence(self):
        manifest = self.historical_archive()
        invalid_records = [
            None, {}, True,
            {"merge_commit": "not-a-commit", "evidence": "historical-merge.md"},
            {"merge_commit": "a" * 40, "evidence": ""},
            {"merge_commit": "a" * 40, "evidence": "missing.md"},
            {"merge_commit": "a" * 40, "evidence": "../outside.md"},
            {"merge_commit": "a" * 40, "evidence": "historical-merge.md", "approved": True},
        ]
        for record in invalid_records:
            with self.subTest(record=record):
                manifest["changes"][self.change_id]["historical_archive"] = record
                (self.root / "sdd" / "legacy-changes.json").write_text(json.dumps(manifest))
                self.assert_status("fail")

    def test_historical_archive_cannot_hide_unfinished_tasks(self):
        manifest = self.historical_archive()
        self.data["tasks"]["tasks"][0]["status"] = "pending"
        self.body["tasks"] = self.body["tasks"].replace("- [x]", "- [ ]")
        self.write("tasks")
        manifest["changes"][self.change_id]["files"]["tasks.md"] = hashlib.sha256(
            (self.change / "tasks.md").read_bytes()
        ).hexdigest()
        (self.root / "sdd" / "legacy-changes.json").write_text(json.dumps(manifest))
        self.assert_status("fail")

    def test_missing_legacy_allowlist_cannot_bypass_v2(self):
        self.make_legacy()
        (self.root / "sdd" / "legacy-changes.json").unlink()
        self.assert_status("fail")

    def test_legacy_hash_match_does_not_bypass_schema_or_references(self):
        self.data["tasks"]["tasks"][0]["requirements"] = ["REQ-999"]
        self.make_legacy()
        self.assert_status("fail")

    def test_unknown_legacy_manifest_entry_is_rejected(self):
        manifest = self.make_legacy()
        manifest["changes"]["unknown-change"] = copy.deepcopy(manifest["changes"][self.change_id])
        (self.root / "sdd" / "legacy-changes.json").write_text(json.dumps(manifest), encoding="utf-8")
        self.assert_status("fail")

    def test_change_selection_rejects_path_escape(self):
        self.begin()
        self.assert_status("fail", change_id="../../outside")

    def test_symlinked_dossier_is_rejected(self):
        self.begin()
        real_path = self.root / "outside-dossier"
        self.change.rename(real_path)
        self.change.symlink_to(real_path, target_is_directory=True)
        self.assert_status("fail")

    def test_evidence_cannot_escape_target_repository(self):
        self.ready()
        self.data["tasks"]["validation"]["results"][0]["evidence"] = "../../outside-evidence.txt"
        self.write("tasks")
        self.assert_status("fail", "delivery")

    def test_cli_json_exit_codes_match_status(self):
        self.begin()
        cases = [("planning", 0, "pass"), ("implementation", 1, "fail")]
        for phase, expected_exit, expected_status in cases:
            with self.subTest(phase=phase):
                result = subprocess.run(
                    [sys.executable, str(VALIDATOR_PATH), "--root", str(self.root),
                     "--change", self.change_id, "--phase", phase, "--json"],
                    capture_output=True, text=True, check=False,
                )
                self.assertEqual(expected_exit, result.returncode, result.stdout + result.stderr)
                self.assertEqual(expected_status, json.loads(result.stdout)["status"])
        self.approved_plan()
        self.complete()
        self.data["tasks"]["validation"]["plan_digest"] = self.digest("tasks")
        self.write("tasks")
        result = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--root", str(self.root),
             "--phase", "delivery", "--json"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertEqual("unable-to-verify", json.loads(result.stdout)["status"])

    def test_cli_digest_matches_public_api(self):
        self.begin()
        result = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--root", str(self.root),
             "--change", self.change_id, "--digest", "proposal"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(self.digest("proposal"), result.stdout.strip())


if __name__ == "__main__":
    unittest.main()
