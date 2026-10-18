# Construction Mapping

Construction renders the artifacts a design schedules. This standard states how: for each kind of
artifact, every field construction writes, where its value comes from, and under which provenance
class. The mapping is code, in `transformation/build/render.py`. This standard specifies it, and
`scripts/testbed/construction_mapping_test.py` holds the two in agreement.

---

## 1. Provenance classes

Every field construction writes has one origin:

| Class | Means |
|---|---|
| `stated_by_design` | a register of the design states the value |
| `governed_elsewhere` | an artifact named in *Governed by* fixes the value, and the design does not restate it |
| `supplied_by_renderer` | construction wrote the value on its own authority, where the design stated none |
| `carried_from_predecessor` | the value came from the artifact being amended, which no register can express |

A field may have two origins: the design states it for some artifacts, and something else governs
it for others. Each origin is a row.

The construction completeness measure admits the first, second and fourth classes. It refuses the
third: a value the renderer invented is design nobody approved.

## 2. Fields

A field is addressed by its dotted path. `[]` stands for a list position. `<name>` stands for a
key the design names: a node, an input, a store, an outcome. `<group>` stands for a vocabulary's
group. A value the design states whole, such as a binding or a test value, is one field; nothing
beneath it is a field of the artifact.

A binding's value renders by the forms DESIGN_LANGUAGE §1.2 specifies. `scripts/testbed/render_vectors_test.py`
pins each form.

### Every artifact

| Field | Kinds | Class | Source |
|---|---|---|---|
| `fqdn` | every | stated_by_design | `new_artifacts.Code`, as the mandate schedules it |
| `artifact_kind` | every | stated_by_design | constant per family (`design.families`) |
| `version` | every | stated_by_design | the `_V<n>` suffix of the identity |
| `governed_by` | every | stated_by_design | constant per family (`design.families`); a transform's by its kind and purity |
| `authority` | every | stated_by_design | constant `pgc.platform` |
| `concern` | every | stated_by_design | the subdomain `new_artifacts.Owner Subdomain` places it in |
| `supersedes` | CAPABILITY_CONTRACT, CAPABILITY_TRANSFORM, INTENT, STRUCTURE, TRANSPORT_INGRESS, WORKFLOW | stated_by_design | `existing_inventory` rows the artifact replaces |
| `subdomain` | WORKFLOW | stated_by_design | the owning subdomain |
| `core.summary` | ACTOR, CAPABILITY_CONTRACT, CAPABILITY_TRANSFORM, EVENT, INTENT, RUNTIME_BINDING, STRUCTURE, TRANSPORT_EGRESS, TRANSPORT_INGRESS, WORKFLOW | stated_by_design | `new_artifacts.Summary`; an intent falls back to `new_intents.Purpose` |

### Actor (AC)

`artifact_kind: ACTOR`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `core.attributes.<name>.default` | stated_by_design |  | `interface_fields` rows for the artifact, direction `ATTRIBUTE`: `Default` |
| `core.attributes.<name>.required` | stated_by_design |  | `interface_fields` rows for the artifact, direction `ATTRIBUTE`: `Required` `YES` |
| `core.attributes.<name>.type` | stated_by_design |  | `interface_fields` rows for the artifact, direction `ATTRIBUTE`: `Type` |
| `core.<property>` | stated_by_design |  | `artifact_properties.Value`, whole, by `Property`: every key of `core` but `summary` and `attributes` |

### Capability contract (CC)

`artifact_kind: CAPABILITY_CONTRACT`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `core.inputs.<name>.default` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Default` |
| `core.inputs.<name>.format` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Format` |
| `core.inputs.<name>.required` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Required` `YES` |
| `core.inputs.<name>.type` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Type` |
| `core.outputs.<name>.required` | stated_by_design |  | `interface_fields` rows for the artifact, direction `OUTPUT`: `Required` `YES` |
| `core.outputs.<name>.type` | stated_by_design |  | `interface_fields` rows for the artifact, direction `OUTPUT`: `Type` |
| `core.pipeline.[].inputs` | stated_by_design |  | declared empty: a step whose `Consumes` lists nothing |
| `core.pipeline.[].outputs` | stated_by_design |  | declared empty: a step with no `OUTPUT` row in `step_bindings`; the schema requires the key |
| `core.pipeline.[].inputs.<name>` | stated_by_design |  | `step_bindings` rows, direction `INPUT`: `Bound To` |
| `core.pipeline.[].on_result.<name>` | stated_by_design |  | `cc_composition.Routing`; an interpreting step routes its `Semantic Status` |
| `core.pipeline.[].op` | stated_by_design |  | `cc_composition.Operation` |
| `core.pipeline.[].outputs.<name>` | stated_by_design |  | `step_bindings` rows, direction `OUTPUT`: `Bound To` |
| `core.pipeline.[].result_surface.[]` | stated_by_design |  | the outcomes `on_result` names |
| `core.pipeline.[].side_effect` | stated_by_design |  | `cc_composition.Capability` where `Kind` is `CS` |
| `core.pipeline.[].step` | stated_by_design |  | `cc_composition.Step Name`; an interpreting step is named by the binding that reads its result |
| `core.pipeline.[].store` | stated_by_design |  | `cc_composition.Store` |
| `core.pipeline.[].transform` | stated_by_design |  | `cc_composition.Capability` where `Kind` is `CT`, or `Interpreted By` |
| `core.result_status_contract.allowed.[]` | stated_by_design |  | the outcomes the pipeline's routing exits on |
| `core.result_status_contract.on_input_failure` | stated_by_design |  | constant `VIOLATION` |

### Capability transform (CT)

`artifact_kind: CAPABILITY_TRANSFORM`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `core.inputs.<name>.required` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Required` `YES` |
| `core.inputs.<name>.structure` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Structure` |
| `core.inputs.<name>.type` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Type` |
| `core.outputs.<name>.required` | stated_by_design |  | `interface_fields` rows for the artifact, direction `OUTPUT`: `Required` `YES` |
| `core.outputs.<name>.structure` | stated_by_design |  | `interface_fields` rows for the artifact, direction `OUTPUT`: `Structure` |
| `core.outputs.<name>.type` | stated_by_design |  | `interface_fields` rows for the artifact, direction `OUTPUT`: `Type` |
| `core.refusal` | stated_by_design |  | `implementation_bindings.Refusal` |
| `machine.atom_stream.[].accumulator.<name>` | stated_by_design |  | `molecule_step_bindings`, role `CARRY` |
| `machine.atom_stream.[].as` | stated_by_design |  | `molecule_steps.Step` |
| `machine.atom_stream.[].atom` | stated_by_design |  | `molecule_steps.Target` of an atom |
| `machine.atom_stream.[].inputs.<name>` | stated_by_design |  | `molecule_step_bindings`, role `INPUT`, of a loop |
| `machine.atom_stream.[].iterator` | stated_by_design |  | `molecule_steps.Iterator` |
| `machine.atom_stream.[].kind` | stated_by_design |  | `molecule_steps.Kind` |
| `machine.atom_stream.[].molecule` | stated_by_design |  | `molecule_steps.Target` of a molecule or a loop |
| `machine.atom_stream.[].over` | stated_by_design |  | `molecule_steps.Over`, as a path |
| `machine.atom_stream.[].update_accumulator.<name>` | stated_by_design |  | `molecule_step_bindings`, role `UPDATE` |
| `machine.atom_stream.[].with.<name>` | stated_by_design |  | `molecule_step_bindings`, role `INPUT`, of an atom or a molecule run once |
| `machine.ct_kind` | stated_by_design |  | `implementation_bindings.Kind`; `atom` where it states none |
| `machine.ct_purity` | stated_by_design |  | `implementation_bindings.Purity`; `ct_pure` where it states none |
| `machine.emit.<name>` | stated_by_design |  | `molecule_steps.Emits`, naming the step |
| `machine.implementation.callable` | stated_by_design |  | `implementation_bindings.Callable` |
| `machine.implementation.module` | governed_elsewhere | `<domain>::STRUCTURE_BUILD_<DOMAIN>_CONFIG_V0` | `<implementation_namespace>.<code>`, the namespace the domain's build manifest declares |
| `machine.operation` | stated_by_design |  | `implementation_bindings.Operation` |

### Event (EV)

`artifact_kind: EVENT`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `core.description` | stated_by_design |  | `new_artifacts.Summary` |
| `core.moment` | stated_by_design |  | `artifact_properties.Value` where `Property` is `moment` |
| `core.schema.<name>.format` | stated_by_design |  | `interface_fields` rows for the artifact: `Format` |
| `core.schema.<name>.required` | stated_by_design |  | `interface_fields` rows for the artifact: `Required` `YES` |
| `core.schema.<name>.type` | stated_by_design |  | `interface_fields` rows for the artifact, any direction: `Type` |
| `core.subdomain` | stated_by_design |  | the owning subdomain |

### Intent (IN)

`artifact_kind: INTENT`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `core.inputs.<name>.default` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Default` |
| `core.inputs.<name>.required` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Required` `YES` |
| `core.inputs.<name>.type` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Type` |
| `core.outcomes.<name>.description` | stated_by_design |  | constant: the `ACK`/`NACK` surface every intent has |
| `core.workflow` | stated_by_design |  | `new_intents.Workflow` |

### Runtime binding (RB)

`artifact_kind: RUNTIME_BINDING`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `core.bindings.<name>.policy` | stated_by_design |  | declared empty: a `runtime_policies` row for the capability whose `Key` states nothing |
| `core.bindings.<name>.policy.<name>` | stated_by_design |  | `runtime_policies` rows: `Key` and `Value`, typed, by `Capability` in `rb_declarations.CS Bindings` |
| `core.storage_structure` | stated_by_design |  | `rb_declarations.Storage Structure`; omitted where it states none |
| `parameters.[]` | stated_by_design |  | `artifact_properties` `parameters` |

### Structure

`artifact_kind: STRUCTURE`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `core.<property>` | stated_by_design |  | `artifact_properties.Value`, whole, by `Property`: every key of `core` but the summary and the storage fields |
| `core.json_schema` | stated_by_design |  | `artifact_properties` `json_schema`, whole: a JSON Schema is data |
| `core.domain` | stated_by_design |  | the namespace of the identity; storage only |
| `core.entity_stores.<name>.path` | stated_by_design |  | `structure_stores.Proposed Path`, by `Store Name`, for the rows whose `Structure` names it or names none; storage only |
| `core.layer` | stated_by_design |  | `artifact_properties` `layer`; `DOMAINS` where the design states none; storage only |
| `core.subdomain` | stated_by_design |  | the owning subdomain; storage only |

A structure is storage when a store belongs to it or the design gives it a `layer`. Any other
structure is a shape: it carries its summary and its properties, and none of the storage fields.

### Test data

`artifact_kind: TEST_DATA`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `cases.[].assertions.<name>` | stated_by_design |  | `test_case_values.Value`, role `ASSERT` |
| `cases.[].bindings.<name>` | stated_by_design |  | `test_case_values.Value`, role `INPUT` |
| `cases.[].case_id` | stated_by_design |  | `test_cases.Case` |
| `cases.[].expected.<name>` | stated_by_design |  | `test_case_values.Value`, role `EXPECTED` |
| `cases.[].expected_outcome` | stated_by_design |  | `test_cases.Expected Outcome` |
| `cases.[].recorded` | stated_by_design |  | `test_case_values.Value`, role `RECORDED` |
| `target` | stated_by_design |  | the transform the vector belongs to |

### Transport egress (TE)

`artifact_kind: TRANSPORT_EGRESS`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `default_result_class` | stated_by_design |  | `artifact_properties` `default_result_class` |
| `evidence_policy` | stated_by_design |  | `artifact_properties` `evidence_policy` |
| `operation` | stated_by_design |  | `transport_bindings.Operation` of the first egress row |
| `output_contract.[].field` | stated_by_design |  | `transport_bindings.Field`, direction `EGRESS`, in order |
| `output_contract.[].from` | stated_by_design |  | `transport_bindings.Bound To` |
| `output_contract.[].required` | stated_by_design |  | `transport_bindings.Required`, written only when `false`: an owed field carries no flag |
| `result_classification.<name>` | stated_by_design |  | `artifact_properties` `result_class.<status>` |

### Transport ingress (TI)

`artifact_kind: TRANSPORT_INGRESS`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `context_requirements` | stated_by_design |  | declared empty: no boundary yet requires context |
| `handler.kind` | stated_by_design |  | `transport_bindings.Handler Kind` |
| `handler.payload_template.<name>` | stated_by_design |  | `transport_bindings.Bound To`, nested at `Field` |
| `handler.workflow` | stated_by_design |  | `transport_bindings.Handler Target` |
| `input_contract.<name>.required` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Required` `YES` |
| `input_contract.<name>.type` | stated_by_design |  | `interface_fields` rows for the artifact, direction `INPUT`: `Type` |
| `operation` | stated_by_design |  | `transport_bindings.Operation` of the first ingress row |

### Vocabulary

`artifact_kind: VOCABULARY`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `<group>.casing` | stated_by_design |  | `vocabulary_extensions.Casing`; `UPPER_SNAKE` where it states none |
| `<group>.entries.[]` | stated_by_design |  | `vocabulary_extensions.Value`, by `Group` (`result_status` where it states none) |
| `extends` | stated_by_design |  | `vocabulary_extensions.Extends` |

### Workflow (WF)

`artifact_kind: WORKFLOW`

| Field | Class | Governed by | Source |
|---|---|---|---|
| `consults.[]` | stated_by_design |  | `declared_reach.Consults` for the workflow |
| `core.actor_context` | stated_by_design |  | `artifact_properties` `actor_context`; where none is stated, the one actor among `new_artifacts`, else in `existing_inventory` |
| `core.nodes.<name>.code` | stated_by_design |  | `execution_topology.Runs`, else the node |
| `core.nodes.<name>.emit` | stated_by_design |  | `artifact_properties` `emit.<exit>`, one event |
| `core.nodes.<name>.emit.[]` | stated_by_design |  | `artifact_properties` `emit.<exit>`, several events |
| `core.nodes.<name>.inputs.<name>` | stated_by_design |  | `step_bindings`, direction `INPUT`, for the node |
| `core.nodes.<name>.next.<name>` | stated_by_design |  | `execution_topology.Routing` |
| `core.nodes.<name>.type` | stated_by_design |  | `execution_topology.Node Type` |
| `core.start_node` | stated_by_design |  | the first `IN` node of `execution_topology` |
| `runtime_binding` | stated_by_design |  | `rb_declarations.RB Code` where `Binds WF` names the workflow |
| `structure` | stated_by_design |  | constant `execution::STRUCTURE_RUNTIME_EXECUTION_V0` |

---

## 3. The construction invariants

`lifecycle::CONSTITUTION_CONSTRUCTION_V1` names four invariants. Each is realised here.

#### DESIGN_UNIQUELY_DETERMINES_ARTIFACT

A scheduled artifact is rendered from its design and nothing else. Construction completeness walks
every field `render_all` emits and counts a field determined when it is present, or declared empty,
and its class is not `supplied_by_renderer`. A design is admitted to construction at 100%.

#### RENDER_INVENTS_NOTHING

Construction records every field it supplies, in the provenance classes of §1, and completeness
refuses what it supplied on its own authority. The mapping test holds the classes of §2 against what
construction reports. §4 names the constants it does not yet record.

#### ONE_PRODUCER_PER_ARTIFACT

An artifact is produced either by construction or by its generator, never by both. A design that
names a generator for an artifact (`generation_provenance`) schedules it as generated, and
construction renders none of its fields; completeness measures only that the generator is named. A
binding stated `{generated: true}` renders as the word `generated`, and is admitted only where its
owner names the generator that supplies the value.

#### MEANING_CHANGE_IS_NEW_IDENTITY

An amended artifact that changes meaning takes a new identity and names its predecessor in
`supersedes`. Construction compares an amendment against the artifact it replaces under the
declared sameness rules (`build/sameness.py`), and renders the re-points the design declares.

---

## 4. Known gaps

- **Constants reported as stated.** `authority`, `artifact_kind`, `governed_by`, a workflow's
  `structure`, a contract's `on_input_failure` and an intent's `outcomes` are constants of the
  platform or of a family. Construction reports them `stated_by_design`, because it reports a field
  only where it supplies one. They are governed elsewhere, and a later change should say by what.
- **Defaults the renderer supplies.** A structure's `core.layer` (`DOMAINS`) and a vocabulary
  group's `casing` (`UPPER_SNAKE`) are written where the design states none, and are refused by
  completeness as invented.
- **The module path in the governed construction step.** `machine.implementation.module` is
  `<implementation_namespace>.<code>`, where the namespace is the one the domain's build manifest
  declares. The construction CLI and the acceptance harness read it from the manifest. The governed
  render transform is handed no manifest, so it places a module where a generated manifest places
  it, `<domain>.implementation.capability_transforms.atoms`.
