#!/usr/bin/env python3

import yaml
import json

# Chemins de fichiers
INPUT_YAML = "site.yaml"
OUTPUT_JSON = "site.json"

def main():
    with open(INPUT_YAML, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Fichier {OUTPUT_JSON} généré à partir de {INPUT_YAML}")

if __name__ == "__main__":
    main()
