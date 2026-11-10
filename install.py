#!/usr/bin/env python3
"""Install only the bundled skill; never overwrite an existing installation."""
import argparse,os,shutil,subprocess,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--dest',type=Path,default=Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'skills')
a=parser.parse_args();source=Path(__file__).resolve().parent/'skills/lumos-design';target=a.dest.expanduser().resolve()/'lumos-design'
if target.exists():parser.error(f'Destino já existe; faça backup e revise a atualização: {target}')
subprocess.run([sys.executable,str(source/'scripts/validar.py')],check=True)
target.parent.mkdir(parents=True,exist_ok=True)
shutil.copytree(source,target)
subprocess.run([sys.executable,str(target/'scripts/validar.py')],check=True)
print(f'Skill instalada em {target}. Use $lumos-design no Codex.')
