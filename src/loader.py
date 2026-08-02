from pathlib import Path
import json

# Path to the data folder
DATA_DIR = Path("../data")

# Path to the knowledge base folder
KB_DIR = DATA_DIR / "knowledge_base"

# Read all Markdown files
kb_files = list(KB_DIR.glob("*.md"))

print(f"Knowledge Base Files Found: {len(kb_files)}")

for file in kb_files:
    print(file.name)

# Read resolved cases
resolved_cases_file = DATA_DIR / "resolved_cases.json"

with open(resolved_cases_file, "r", encoding="utf-8") as f:
    resolved_cases = json.load(f)

print(f"\nResolved Cases Loaded: {len(resolved_cases)}")