# Workspace setup

[English](workspace-setup.md) | [Português](workspace-setup.pt.md) | [Español](workspace-setup.es.md)

Prepare the repository you will work on and confirm which Harness version is available. Versat workspace distribution is managed by an administrator; installation policy and member access must be checked in your workspace.

## Prepare

1. Obtain access to the target repository and read its README and contribution guidance. Clone it with the real repository URL, or use an existing clean checkout.
2. In Codex, open that repository as the project folder. Confirm it is the primary folder before starting work.
3. Read AGENTS.md and identify the project’s Harness/provider version and Standards lock when present. Ask Codex to locate the required Skill and matching canonical resources before changing files.

OpenAI documents folder selection in [Projects and chats](https://learn.chatgpt.com/docs/projects). Project setup actions can be shared through [local environments](https://learn.chatgpt.com/docs/environments/local-environment); configure only commands required by your repository.

## Verify and recover

Ask Codex to report the working directory, selected provider version and where it found versat-sdd. The paths must belong to the intended project/provider. If access or a Skill is missing, stop that workflow and ask the repository or workspace owner to resolve it. Do not copy policy from another release or assume automatic installation. A repository without identity metadata needs an explicit classification before bootstrap or migration.

[Team recording](https://versat.slack.com/files/U04PSSJ2W/F0CF8AH2SVC/pantalla_compartida_-_2026-11-05_16_09_27.mp4) — requires Slack access. Supplemental training; video contents have not been verified for this guide. The written steps are sufficient to continue.

[Continue to quickstart](../quickstart.md)
