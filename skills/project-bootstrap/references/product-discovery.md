# Guided Product Discovery

Use the [base product overview](../../../project-templates/base/specs/product/overview.md) as the coverage guide and output template. Keep the topic list there instead of maintaining a second questionnaire. This discovery applies to every profile, including internal tools, libraries and infrastructure.

## Conduct the conversation

Read the developer's brief, supplied PRD and prior answers before asking questions. Map what is already known into the overview and ask only for missing or contradictory information. Begin with the problem, intended users and proposed value; follow with market and business assumptions, then growth and impacts. Use a few related questions per round, explain unfamiliar terms briefly, and allow the developer to defer a topic.

Offer draft wording based on the developer's answers when it helps, and label it as a suggestion until confirmed. Separate sourced facts, developer-provided claims, hypotheses and open questions. Do not turn a plausible pitch into a claim of validated demand, competitive advantage or social benefit.

When information is unavailable, populate the relevant section with `Unknown`, its consequence and a concrete next validation step. Use `Not applicable` with a reason when the concept does not fit the project. For an internal service, capture internal users, adoption scope and expected organizational value; do not invent an external market or commission model. Missing market research can remain a documented gap while the repository skeleton is created. If the developer defers discovery entirely, produce an explicitly incomplete draft and report that limitation.

## Market evidence and calculations

For TAM (total addressable market), SAM (serviceable available market) and SOM (serviceable obtainable market), record the segment, geography, period, units, method, inputs, formula and result, with source links or supplied references and their dates. Make assumptions and uncertainty visible. Ask for the basis of SOM, such as reachable customers and delivery capacity, rather than selecting an unexplained percentage of TAM.

Keep transaction volume, customer counts and product revenue distinct. For a commission model, define take rate as platform revenue divided by the corresponding transaction volume, specify what is included, and show the multiplication used to estimate revenue. For subscriptions or internal products, explain why take rate does not apply and describe the relevant pricing or value model. Do not apply a take rate again to a market figure already expressed as platform revenue.

Use supplied evidence first. Research external claims when needed and feasible with available tools; cite what was actually consulted. If research is unavailable or outside scope, leave the claim unverified. Do not fabricate market sizes, competitors, source URLs or project history. Check arithmetic and consistent units for any supplied numeric estimates; these checks do not validate the underlying demand assumptions.

## Generate the documents

Always populate `specs/product/overview.md` using the shared base template. Replace template prompts with project-specific content or explicit gaps, retain every topic, and record the document owner, review state and update date. Preserve provided project content and reconcile conflicts instead of overwriting it silently.

Keep a compact overview for a small project. Split substantial material only when it improves navigation or maintenance:

- `specs/product/research.md` for detailed market calculations, competitor comparisons or customer evidence.
- `specs/product/strategy.md` for developed monetization, positioning, growth objectives and success metrics.
- `specs/product/requirements.md` for established product capabilities and business rules when there is enough confirmed input to specify them.

Create only supporting files with useful content. When splitting, leave a short summary and a relative link under the corresponding overview topic, and maintain the detail in one place. Do not add a second PRD that repeats the product overview or the change's proposal and requirements. A supplied PRD can remain a referenced input; identify where its maintained content now lives.

Connect the bootstrap proposal to the overview. Product strategy describes direction and hypotheses; change requirements specify the observable behavior being delivered. Do not convert every ambition into a committed implementation task or describe planned capabilities as already shipped.

## Review and handoff

Before reporting completion, check that:

- Every overview topic contains a project-specific answer, a linked summary, an explicit unknown with a next step, or a reasoned non-applicability statement.
- Market figures have traceable inputs and calculations, or are explicitly unavailable; evidence and assumptions are distinguishable.
- The overview links resolve and the bootstrap proposal references the product context without copying it.
- The draft identifies its owner and review state, and the handoff names remaining questions, evidence gaps and the next validation actions.

Present the generated files for developer review and incorporate corrections. Follow the canonical SDD review and readiness process; a generated document or passing structural check is not evidence of human acceptance. Report these content checks separately from executable validators, which currently do not assess product completeness or market validity.
