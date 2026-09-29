# Documentation Standard

- Every repository MUST explain its purpose, owner, lifecycle and validation entry point.
- Architecture documentation MUST describe current reality, not only intended design.
- Significant structural decisions MUST be recorded as ADRs.
- Product changes MUST keep living specifications synchronized with implementation.
- Examples MUST be clearly distinguishable from normative requirements.
- Sensitive data, credentials and customer information MUST NOT be copied into documentation.

## First-use guides

- When usable product behavior needs explanation, projects MUST provide a concise first-use guide for its intended audience. It MUST cover prerequisites, preparation, one representative action and its observable expected result, using commands or UI steps as appropriate.
- Reuse an equivalent existing guide or README section. Otherwise, use `docs/quickstart.md`. The root README MUST link to the actual guide or section; add the link only when its target exists.
- Guides MUST remain living documentation outside change/archive dossiers. Add focused guides under `docs/guides/` only when distinct workflows need more detail, preserving an existing documentation convention where applicable. Link from the quickstart and reference common setup rather than duplicate it.
- Changes affecting documented usage MUST update the relevant instructions and examples alongside implementation and verify the affected steps against their expected results. Reuse functional checks and evidence where they cover the same behavior; report unavailable verification explicitly under the existing validation contract.
- Empty scaffolds MUST NOT generate empty guides, broken links or instructions claiming unimplemented behavior. Internal changes with no usage impact do not require documentation work solely to satisfy this convention.

Apply the existing [Language](language.md) and [Security](security.md) Standards to guide content and examples.
