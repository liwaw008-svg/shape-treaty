# Shape Treaty / STP-1

**Status:** experimental protocol  
**Domain:** evidence-backed compatibility  
**Question:** how much may a proposal change before it becomes a different thing?

## Abstract

Shape Treaty is a GenLayer protocol for comparing a candidate design against a frozen reference. “Design” is intentionally broad: a public-space plan, an interface contract, a physical specification, or an interoperability proposal can all be treated as shapes.

The proposer separates invariants from preferences. Validators retrieve the authoritative reference and the candidate independently. Ratification is derived from the resulting conflict map, not from the proposer's opinion of its own work.

## Constraint model

Let `F` be fixed constraints and `E` be elastic constraints.

```text
fixed conflict exists            → IMPOSSIBLE
no fixed conflict + elastic gap  → ELASTIC
no material conflict             → RATIFIED
unavailable decisive evidence    → IMPOSSIBLE
```

The fail-closed last line is part of the protocol, not an implementation accident.

## Proposal envelope

A proposal freezes:

- a treaty identifier;
- the canvas or problem being shaped;
- fixed constraints that may not move;
- elastic preferences that may bend;
- an authoritative reference URL.

A candidate later supplies its own public URL. Neither call contains a verdict, conflict list, or confidence value.

## State interface

```python
propose(id, canvas, fixed, flexible, reference_url)
ratify(id, candidate_url)
get_treaty(id)
```

`get_treaty` exposes the reference and candidate snapshots, fixed conflicts, elastic conflicts, rationale, confidence, and ratification state. This is the canonical record consumed by the frontend.

## Security considerations

### Evidence injection
Retrieved pages are wrapped as untrusted content. Text inside a page cannot redefine the comparison task.

### Self-certification
The candidate author cannot supply “all constraints passed.” Validators construct the conflict map.

### Order dependence
Constraint evaluation is normalized so rearranging caller input cannot change the treaty outcome.

### Partial availability
An inaccessible decisive source cannot yield ratification.

## Implementation index

| Area | Location |
|---|---|
| Protocol contract | `contracts/contract.py` |
| Interactive treaty canvas | `frontend/` |
| Conformance vectors | `tests/` |
| Bradbury release helpers | `scripts/` |

Conformance requires passing the Python vectors, GenVM lint, and a production frontend build. A deployed browser instance points to Bradbury through `NEXT_PUBLIC_CONTRACT_ADDRESS`.

## Reference implementation

`bradbury:0xbC043D84d371B78081b1173B2baaC31311f891E6`

## Design principle

> Preserve the promise, not the pixels.
