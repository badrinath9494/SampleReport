#!/usr/bin/env python3
import json
import pathlib
import sys

errors = []
for notebook in pathlib.Path('.').rglob('*.ipynb'):
    try:
        data = json.loads(notebook.read_text(encoding='utf-8'))
        cells = data.get('cells', [])
        for i, cell in enumerate(cells):
            if cell.get('cell_type') == 'code':
                src = ''.join(cell.get('source', []))
                try:
                    compile(src, f"{notebook}:cell:{i}", 'exec')
                except SyntaxError as e:
                    errors.append(f"{notebook}:cell:{i}: {e}")
    except Exception as e:
        errors.append(f"{notebook}: invalid notebook/json: {e}")

if errors:
    print('\n'.join(errors))
    sys.exit(1)

print('Notebook syntax validation passed')
