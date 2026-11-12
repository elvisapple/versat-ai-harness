# Diagnostic path correction

The original Design-only helper assumed both proposed dossiers were active. After the authorized H01 move, rerunning it raised FileNotFoundError before producing new observations. The R2 execution copy now locates the unique active/archive Design. Original helper remains historical; no product validator or check scope changed.
