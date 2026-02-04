# """
# Project: City-Council-Meeting-Analyzer
# Version: V0.2.004
# Security: GDPR-Ready (Privacy by Design)
# Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
# """

# Security Policy

## Supported Versions
Only the latest version of the analyzer is supported for security updates.

| Version | Supported          |
| ------- | ------------------ |
| V0.2.x  | :white_check_mark: |
| < V0.2  | :x:                |

## Security Model: Sovereign AI
This project follows a "Sovereign AI" model. The software is designed to run 
entirely on user-controlled hardware. 

1. **Data Confinement:** No data is sent to external APIs (OpenAI, Google, etc.) 
   unless the user explicitly changes the `base_url` in the code.
2. **Secret Management:** Users are responsible for the `.env` file containing 
   the `PSEUDO_SALT`. If this salt is lost, pseudonymized data cannot be re-identified. 
   If it is leaked, the privacy of the pseudonymized reports is compromised.

## NIST SP 800-122 Alignment
This code implements technical controls recommended by NIST for protecting PII 
confidentiality. Users should ensure their local file system permissions and 
SMB mounts are configured to prevent unauthorized access to the `data/` directory.

## Reporting a Vulnerability
Please do not report security vulnerabilities via public GitHub issues. 
Instead, please [Insert your preferred contact method, e.g., an email or private message].
