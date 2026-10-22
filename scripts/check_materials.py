"""Validate local document targets and required checkpoint artifacts."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
errors = []
for name in ("context", "use-cases", "components"):
    for ext in ("svg", "puml", "png"):
        if not (root / "diagrams" / f"{name}.{ext}").is_file():
            errors.append(f"Missing diagram: {name}.{ext}")
for md in root.rglob("*.md"):
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', md.read_text(encoding="utf-8")):
        if target.startswith(("http:", "https:", "#", "mailto:")):
            continue
        path = target.split("#")[0]
        if path and not (md.parent / path).exists():
            errors.append(f"Broken local link in {md.relative_to(root)}: {target}")
tasks = json.loads((root / "management/backlog.json").read_text(encoding="utf-8"))
for task in tasks["tasks"]:
    for key in ("summary", "priority", "due_date", "proposed_responsible", "outcome", "acceptance_criteria"):
        if not task.get(key):
            errors.append(f"Incomplete task {task.get('local_key')}: {key}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: required diagrams, Markdown links and {len(tasks['tasks'])} prepared task records")
print("This check does not establish user research, supervisor review or YouTrack completion.")

