# v4.1 Domain Engine Specification

All domain engines share:

```text
POST /api/science/engine/run
{
  "domain": "...",
  "operation": "...",
  "payload": {...}
}
```

The response contains:
- domain
- operation
- result
- deterministic certificate
- `verified_computation` status

The certificate proves that the bounded computation implemented by the platform ran successfully. It does not certify a scientific theory or clinical decision.

Domain-specific validation rules remain intentionally conservative.
