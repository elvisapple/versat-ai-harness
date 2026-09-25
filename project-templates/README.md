# Project Templates

Templates are composable modules. The bootstrap starts with `base` and adds one or more profile modules.

```text
software       = base + software
agent          = base + agent
hybrid         = base + software + agent
library        = base + library
infrastructure = base + infrastructure
```

Structure manifests describe directories to create. The bootstrap must detect file conflicts and preserve project-specific content during upgrades.

The base includes [the product overview template](base/specs/product/overview.md) for all profiles. During bootstrap, populate it through the project-bootstrap Skill's guided discovery. Supporting product documents are created only when the collected content warrants them; profile modules do not copy or redefine the shared overview.
