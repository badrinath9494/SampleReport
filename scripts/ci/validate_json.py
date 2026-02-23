#!/usr/bin/env python3
import json
import pathlib
import sys

errors = []
json_files = list(pathlib.Path('.').rglob('*.json'))

for f in json_files:
    try:
        json.loads(f.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f"{f}: {e}")

for pbir in pathlib.Path('.').rglob('definition.pbir'):
    report_json = pbir.parent / 'report.json'
    if not report_json.exists():
        errors.append(f"{pbir}: missing sibling report.json")

if errors:
    print('Report/JSON validation errors:')
    print('\n'.join(errors))
    sys.exit(1)

print('Report JSON validation passed')
