# FICA–IGF-U v3.1 Architecture

```text
                    UNIVERSAL KERNEL
                           |
        +------------------+------------------+
        |                  |                  |
     OBJECTS           OPERATORS          RELATIONS
        |                  |                  |
        +------------------+------------------+
                           |
                     APPLICATIONS
                           |
              +------------+------------+
              |            |            |
           Collatz      Physics      Other
          (module)     models       modules
                           |
                     SCIENCE GRAPH
                           |
                      PROVENANCE
                           |
                   EXPERIMENT / DATA
                           |
                     EVIDENCE / CLAIM
                           |
                    PROOF OBLIGATIONS
```

The core does not contain Collatz-specific semantics. Collatz is represented as a registered application.
