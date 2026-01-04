
import sys, re, pathlib

HIGH = []
MEDIUM = []
LOW = []

def analyze_env(text):
    for line in text.splitlines():
        if re.search(r'(password|secret|api_key)=.+', line, re.I):
            HIGH.append(f"Hardcoded secret detected: {line.split('=')[0]}")
        if re.search(r'DEBUG\s*=\s*true', line, re.I):
            MEDIUM.append("DEBUG mode enabled")

def analyze_yaml_json(text):
    if re.search(r'"?password"?\s*:\s*".+"', text, re.I):
        HIGH.append("Hardcoded password in config")
    if re.search(r'"?debug"?\s*:\s*true', text, re.I):
        MEDIUM.append("DEBUG flag enabled")

def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_config.py <config file>")
        sys.exit(1)

    path = pathlib.Path(sys.argv[1])
    text = path.read_text(errors="ignore")

    if path.suffix in [".env"]:
        analyze_env(text)
    elif path.suffix in [".yaml", ".yml", ".json"]:
        analyze_yaml_json(text)

    print("=== Security Config Analysis ===")
    for h in HIGH: print("[HIGH]", h)
    for m in MEDIUM: print("[MEDIUM]", m)
    for l in LOW: print("[LOW]", l)

    print(f"Summary: High={len(HIGH)}, Medium={len(MEDIUM)}, Low={len(LOW)}")

if __name__ == "__main__":
    main()
