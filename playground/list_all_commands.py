import json

with open('../devices/specifications/KST3000.json', 'r') as f:
    d = json.load(f)

for m in d['commands']:
    print(f'osc.{m["name"]}()')
