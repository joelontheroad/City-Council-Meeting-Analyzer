# City-Council-Meeting-Analyzer (V0.2.004)
**Author:** Joel Greenberg ([joelontheroad](https://github.com/joelontheroad))

A secure, local-first AI pipeline for transcribing and analyzing city council meetings. 

## 🛡️ Security & Privacy
Designed with **GDPR Article 25 (Privacy by Design)** principles. This tool uses salted SHA-256 hashing to pseudonymize speakers before data export, ensuring local processing remains private. Hardened against **OWASP Top 10** and **OWASP LLM Top 10** risks.

## 🚀 Quick Start (Pop!_OS / Ubuntu)
1. **Clone the repo:**
   `git clone https://github.com/joelontheroad/City-Council-Meeting-Analyzer.git`
2. **Run the hardened installer:**
   `chmod +x setup.sh && ./setup.sh`
3. **Analyze with Masking:**
   `python3 main.py --mask`

## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.
