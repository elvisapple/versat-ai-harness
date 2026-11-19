# Marketplace identity fixture

Synthetic target catalog for deterministic validation of the current package. Tests copy it into a temporary package root and mutate one contract at a time. The repository URL and v0.4.0 reference are metadata only; tests do not fetch, install, register or publish anything. Native discovery, source deduplication, managed identity and recovery require separate real observations. Legacy installations retain their version-matched provider; the new package validator does not create a legacy alias.

Copied-package tests additionally resolve canonical resources and relative Markdown links from all five Skill directories, comparing file bytes with the source. A removed Standards index must be detected for every Skill. These are offline packaging checks, not native discovery or supervised Skill execution.
