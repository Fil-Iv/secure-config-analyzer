
# Secure Config Analyzer

Python tool that detects insecure configuration practices in `.env`, `.yaml`, and `.json` files.

## Features
- Detects hardcoded secrets
- Flags DEBUG enabled in production configs
- Simple severity-based report

## Usage
```bash
python analyze_config.py sample_configs/insecure.env
```

## Disclaimer
This tool performs static analysis only and is intended for security review and educational purposes.
