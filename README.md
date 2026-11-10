# Motor de Design LUMOS

Para a equipe: [comece aqui com o prompt de instalação e apresentação do ambiente](COMECE-AQUI.md).

Skill para criar, adaptar e revisar **qualquer peça de design LUMOS**, não apenas Instagram: documentos, impressos, apresentações, sites, interfaces, dashboards, anúncios e audiovisual.

Inclui regras de identidade, guias por formato, quatro logos PNG oficiais, uma prancha vetorial PDF, uma peça social de referência aprovada por Júlio e verificação de integridade. A referência inclui uma cena gerada por IA, sem pessoas. Não inclui fotos reais, dados de clientes ou credenciais.

## Cérebro público da LUMOS

A skill inclui uma [base revisada de marca e conteúdo](skills/lumos-design/references/cerebro/indice.md): identidade, voz, serviços documentados, territórios editoriais e públicos. O recorte de dentistas permanece identificado como hipótese. A base distingue posicionamento de entrega comprovada e orienta o que precisa ser confirmado antes de virar afirmação pública.

Esta é a edição pública autorizada por Júlio. O cofre privado, as reuniões, os diagnósticos internos, as condições comerciais e os acessos não foram incorporados. Os arquivos da base ficam dentro da skill e acompanham a instalação.

## Instalar no Codex

No Codex, peça ao instalador de skills:

> Use $skill-installer para instalar a skill do repositório IDEVA-AI/lumos-design, caminho skills/lumos-design.

Alternativa manual, com Git e Python 3.9+:

```sh
git clone https://github.com/IDEVA-AI/lumos-design.git
cd lumos-design
python3 install.py
```

O instalador copia apenas a skill para `$CODEX_HOME/skills/lumos-design`, ou `~/.codex/skills/lumos-design` quando CODEX_HOME não estiver definido. Não altera configurações ou instala dependências. Recusa sobrescrever uma instalação existente. Se a skill ainda não aparecer, abra uma nova conversa/sessão do Codex.

Para outra pasta ou teste isolado:

```sh
python3 install.py --dest /caminho/para/skills
python3 /caminho/para/skills/lumos-design/scripts/validar.py
```

O caminho passado é o diretório que conterá `lumos-design`, não a própria pasta da skill. Para atualizar, revise as mudanças e substitua a cópia antiga manualmente após fazer backup.

## Usar

Posts e carrosséis seguem o acabamento editorial do hero da LUMOS. A skill inclui a referência visual final e o guia `references/social.md`, com luz, profundidade, relação entre headline e texto de apoio e adaptação para carrosséis.

```text
Use $lumos-design para criar uma apresentação de 8 slides sobre o serviço informado. Formato 16:9, público de empresários. Use os dados anexados e entregue PPTX editável e PDF.
```

```text
Use $lumos-design para revisar este folder A4 para impressão. Confira identidade, resolução efetiva, descritor e parâmetros de produção; aponte pendências antes de fechar o PDF.
```

A skill orienta o trabalho. A criação do arquivo depende das ferramentas disponíveis no ambiente, e não é publicação automática. Informe objetivo, público, mensagem, suporte e formato de entrega. Ausência de dados não autoriza inventar resultados.

## Outros aplicativos

A pasta `skills/lumos-design` contém instruções e assets autocontidos. `plugin.json` segue o formato portátil Agent Plugins 1.0 para ferramentas compatíveis. Não há garantia de instalação direta em toda interface do ChatGPT, Claude ou outro produto. Um link do GitHub por si só não instala a skill em uma conta: use o mecanismo de instalação/importação suportado pela ferramenta escolhida. Nenhum plugin de conta foi criado por este repositório.

## Verificar

```sh
python3 skills/lumos-design/scripts/validar.py
```

O teste confere arquivos, referências e hashes; não substitui revisão visual. Os PNGs têm tamanho limitado para impressão. A prancha PDF contém vetores e assinatura com descritor, mas precisa da aplicação adequada extraída em editor vetorial.

## Estrutura

- `skills/lumos-design/SKILL.md`: instruções principais.
- `references/` dentro da skill: marca, ativos, formatos, voz e proveniência.
- `assets/` dentro da skill: logos, PDF vetorial e manifesto SHA-256.
- `install.py`: instalação local sem sobrescrita.

## Direitos e limites

A disponibilidade pública não concede licença irrestrita da marca, dos logos ou das fontes. Use-os somente com autorização para representar a LUMOS. Não foi adicionada licença de código aberto aos materiais de marca. Cormorant Garamond e Inter são referências tipográficas; arquivos instaláveis de fontes não estão incluídos.

A skill não autoriza publicação, envio, alteração de contas ou transmissão de dados. Revise textos, direitos e parâmetros de produção antes de distribuir cada peça.
