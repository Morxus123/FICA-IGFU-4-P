# FICA–IGF-U v3.0 Final Technical Specification

## 1. Purpose

Provide one auditable software substrate for representing, transforming, checking and tracing heterogeneous research objects across multiple scientific domains.

## 2. Kernel principles

- explicit types
- explicit domains
- deterministic serialization/digests
- bounded computation
- traceable provenance
- separation of computation from proof
- separation of model structure from empirical truth
- extensibility through registered domains/operators

## 3. Epistemic status model

`schema_validated` -> object structure is valid.

`verified_computation` -> a bounded computation reproduced successfully.

`verified_derivation` -> supplied finite derivation passed implemented rules.

`provenance_chain_validated` -> all declared provenance links resolve.

`measurement_validated` -> measurement record has valid numerical/unit/uncertainty structure.

`theorem_proved` -> reserved for a complete formal proof kernel.

`empirical_truth_proved` -> deliberately not asserted by this generic kernel.

## 4. Measurement model

A measurement is represented by value, unit and non-negative uncertainty.

For independent measurements x and y with the same unit:

u(x+y) = sqrt(u(x)^2 + u(y)^2).

This is a stated uncertainty-propagation model, not a universal rule for correlated measurements.

## 5. Security and scope

The kernel accepts bounded JSON objects and does not expose arbitrary code execution through its mathematical APIs.

## 6. Reproducibility

Important records receive deterministic SHA-256 digests over canonical JSON representations.

## 7. Final release status

v3.0 is the final integrated prototype release of the current architecture. Future versions should extend domain-specific kernels without weakening the epistemic distinctions above.
