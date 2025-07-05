import os
import json
import yaml  # pip install pyyaml

def flatten_structure(node, base_path=""):
    pages = []
    for key, value in node.items():
        if key in ("icon",): continue
        if isinstance(value, dict):
            if isinstance(value.get("content"), str):
                pages.append({
                    "title": key,
                    "file": value["content"]
                })
            elif isinstance(value.get("content"), dict):
                pages.extend(flatten_structure(value["content"], base_path))
    return pages

with open("site.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

pages = flatten_structure(data["content"])

index = []
for page in pages:
    file_path = os.path.join("docs", page["file"])
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        index.append({
            "title": page["title"],
            "file": page["file"],
            "content": content
        })

with open("search-index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print(f"Generated search-index.json with {len(index)} entries.")
