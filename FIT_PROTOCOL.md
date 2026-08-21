# Fit protocol ◇ 1200 × 800

## Treaty surface

The canvas is shared, but not every part of it is negotiable.

```text
┌──────────────────────────────────────────┐
│  fixed: logo exclusion radius            │
│                                          │
│            flexible: caption orbit       │
│                                          │
│  fixed: headline baseline                │
└──────────────────────────────────────────┘
```

A maker proposes the canvas and divides constraints into two sets. Fixed geometry is inviolable. Flexible geometry may absorb a conflict. A public specification is authenticated by GenLayer validators so that the treaty is not based only on the maker’s paraphrase.

Ratification is then mechanical:

- no conflicts → `RATIFIED`;
- every conflict belongs to the flexible set → `ELASTIC`;
- at least one conflict lies outside it → `IMPOSSIBLE`.

This project does not outsource taste to consensus. It does not decide whether a poster is beautiful. It makes the coordination boundary explicit, records the exact geometry collaborators accepted, and prevents a later visual edit from pretending the original constraints were different.

The deployed plane is described in `treaty-vector.json`. Address, ratification transaction, maker, and geometry rule use vocabulary from the design system itself.
