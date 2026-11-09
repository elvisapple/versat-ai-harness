# CHECK-002 — Navigation, translations and rendered review

Result: pass (2026-11-09). Input snapshot before/after: see before.txt and after.txt. The user-document contents and organization candidate are unchanged from verification-04; the previous per-section semantic review remains applicable. Current structural traversal is in navigation.json: 39 pages, no missing local file or heading anchor, 21 organization-to-Harness links covering 16 exact published files, and byte-identical organization working copy/candidate snapshots.

## Observed rendered pages

Chrome, authenticated intended-reader session, actual GitHub Markdown preview, normal desktop viewport. Harness pages were inspected at `49e1160d30b8459efabc913bd06df25d64bb168c`; organization pages at `1b6a0a127c85e2c928f4437423be5aaa6f72ae30`. Screenshots and accessibility/DOM observations were returned in the coordinating chat during execution, not generated from source text. This report is the durable observation record.

| Page family | English | Portuguese | Spanish | Observations |
|---|---|---|---|---|
| Harness README | README.md | README.pt.md | README.es.md | Purpose, owners, language switches and Start here links render. Clicked EN→PT→ES switches and followed Spanish quickstart. Validation command is a formatted code block; policy/version boundaries remain readable. |
| Quickstart | quickstart.md | quickstart.pt.md | quickstart.es.md | Preparation link, one planning-only request, result paths and Gate 1 boundary visible; later lifecycle links use matching locales. Long example commands retain GitHub's horizontal code-block scrolling and copy control. |
| Representative guide | workspace-setup.md | workspace-setup.pt.md | workspace-setup.es.md | Three numbered preparation steps, exact-provider checks, recovery and English-only official references render clearly; restricted recording is supplemental. |
| Product | overview.md | overview.pt.md | overview.es.md | Ownership, Issue 22, persona, solution and separate evidence/unknown sections render with equivalent heading structure. |
| Organization contribution | CONTRIBUTING.md | CONTRIBUTING.pt.md | CONTRIBUTING.es.md | Public participation instructions and repository precedence remain visible above explicitly private internal resources. |
| Organization README | README.md | README.pt.md | README.es.md | Purpose/default-file behavior and aligned navigation render; scrolled the English file table and inspected its links and descriptions. No broken table cells or overlapping layout observed. |

Clicked the Spanish organization First use link and observed the actual quickstart at immutable content commit `27735687a37e896cd6b0c95cd9d2d848ee166d90`. The intended signed-in reader can reach the documented target. Also followed organization Issues → New issue; the chooser visibly offered Bug report, Chore, Feature request and Blank issue. No issue was created or sent.

## Translation and scope checks

The 13 locale sets retain their reviewed equivalent purpose, examples, identifiers, stop conditions, permission boundaries and exact-version limitations. Source bytes are unchanged from the retained semantic review, including all seven other focused-guide sets. Current traversal rechecks every local link and localized sibling; the rendered sample above covers each required page type in each language. Technical references stay English and are labeled accordingly. Neither active nor archived dossier paths appear in living user pages. Recheck the same traversal after archival.

## Retained attempt limits

An initial Spanish heading locator used the wrong translated word and timed out; the actual page heading was then read and visually inspected. One browser helper timed out on the cross-repository route; the supported native tab accessibility/screenshot API confirmed the actual loaded target. Early captures taken before navigation completed were not counted as the destination inspection. Native control of the Codex app itself was denied and is documented separately; browser evidence does not claim native-app control. No content change was necessary.
