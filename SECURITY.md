# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| 0.9.x   | ✅        |
| 0.8.x   | ⚠️ security fixes only |
| < 0.8   | ❌        |

## Reporting a vulnerability

PDF Reader parses untrusted files, so we treat parser crashes, memory-safety issues in native bindings, and path-traversal in the annotation cache as security-relevant.

Please email `security@pdf-reader.dev` with:

- A description of the issue
- A minimal reproducer PDF (or a generator script)
- Affected version(s) and platform

Do **not** open a public issue for security reports. We aim to acknowledge within 72 hours and publish a fix within 30 days for confirmed issues.

## Scope

In scope:

- `src/pdfreader/toolkit/render` — PyMuPDF/Pillow rendering pipeline
- `src/pdfreader/toolkit/annotate` — annotation storage
- `src/pdfreader/lib/config` — config deserialization

Out of scope:

- Issues requiring a malicious local user with write access to the library DB
- Third-party PDFs that only cause the OS viewer to crash