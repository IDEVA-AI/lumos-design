#!/usr/bin/env python3
"""Check portable package metadata, internal references and asset integrity."""
import hashlib,json,re,struct,zlib
from pathlib import Path
s=Path(__file__).resolve().parents[1]
p=s.parents[1]
if (p/'plugin.json').exists():
    manifest=json.loads((p/'plugin.json').read_text())
    assert manifest['$schema']=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',manifest['name'])
    assert re.fullmatch(r'\d+\.\d+\.\d+',manifest['version'])
body=(s/'SKILL.md').read_text()
assert body.startswith('---\n')
front=body.split('---',2)[1]
assert re.search(r'^name: lumos-design$',front,re.M)
assert re.search(r'^description: \S.+$',front,re.M)
for path in s.rglob('*.md'):
    text=path.read_text()
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if '://' not in target:
            dest=(path.parent/target).resolve()
            assert dest.is_relative_to(s),target
            assert dest.exists(),target
for record in json.loads((s/'assets/manifest.json').read_text()):
    path=s/'assets'/record['path'];data=path.read_bytes()
    assert hashlib.sha256(data).hexdigest()==record['sha256'],path
    assert len(data)==record['bytes']
    if record.get('format')=='pdf':
        assert data.startswith(b'%PDF-') and b'%%EOF' in data[-100:]
        continue
    assert data[:8]==b'\x89PNG\r\n\x1a\n'
    assert struct.unpack('>II',data[16:24])==(record['width'],record['height'])
    i=8
    while i<len(data):
        size=struct.unpack('>I',data[i:i+4])[0];typ=data[i+4:i+8];chunk=data[i+8:i+8+size]
        assert (zlib.crc32(typ+chunk)&0xffffffff)==struct.unpack('>I',data[i+8+size:i+12+size])[0]
        i+=size+12
    assert i==len(data)
assert len(list((s/'assets/logos').glob('*.png')))==4
assert not list(s.rglob('*.jpg'))
print('PASS: metadata, frontmatter, internal references, all manifest hashes/dimensions/CRC, vector PDF header, 4 official logos; no JPG.')
