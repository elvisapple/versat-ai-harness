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
