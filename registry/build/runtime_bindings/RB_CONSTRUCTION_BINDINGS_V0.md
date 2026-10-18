# RB_CONSTRUCTION_BINDINGS_V0

## 1. Intent

Runtime bindings for the Construction lifecycle: the one write the pipeline performs.

---

## 2. Why construction does not reuse the phase bindings

`RB_TRANSFORMATION_BINDINGS_V0` declares, in its own words, *no storage, no writes* — observation
cannot disturb what it observes. Adding a write binding to it would make that declaration false for
every phase workflow that binds it, and a phase would silently acquire the ability to write.

So the subdomain split is a binding split too. Phases observe and cannot write **by construction**;
construction writes and declares exactly where.

---

## 3. The root is declared here, not by a caller

Where generated artifacts land is governance, so the policy root lives in the binding. Construction
writes beneath the instance data root, never into a source registry: a generated artifact is build
output, and whether it replaces an authored one is a separate, human decision. Having the runtime
overwrite the corpus that proves it correct would destroy the evidence in the act of producing it.

---

## Machine

```yaml
fqdn: transformation::RB_CONSTRUCTION_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: build
parameters:
- module_data_root
core:
  summary: Runtime bindings for the construction lifecycle
  description: Binds the single write the construction pipeline performs, beneath a declared root.
  bindings:
    capability_side_effects::CS_TEXT_ARTIFACT_V0:
      policy:
        root: "{{module_data_root}}/construction"

extensions:
  notes:
    - Generated artifacts are build output; they are never written into a source registry.
    - The root is policy, so no caller can redirect where a construction lands.
```
