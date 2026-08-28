# PostgreSQL Standard

- Schema changes MUST use versioned migrations.
- Destructive changes MUST include a reviewed rollout and recovery plan.
- Queries on critical paths MUST be assessed for indexes and execution cost.
- Backup, restore testing and recovery objectives MUST match project criticality.
- Access MUST follow least privilege and application identities MUST not own shared administrative roles.
