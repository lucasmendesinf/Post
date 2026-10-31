# Rotina diária de postagem (instruções para o Claude)

Executada todo dia pela tarefa agendada. Siga na ordem. Leia antes `REGRAS.md`, `PAUTA.md` e `HISTORICO.md`:
as regras e a pauta mandam; este arquivo só descreve o passo a passo técnico.

## 1. Preparar

1. Clonar/atualizar `lucasmendesinf/Post` (branch `main`).
2. Conferir que `python3 -c "import playwright"` funciona e que existe `/usr/bin/google-chrome` (ou Chromium).
   Se faltar, `pip install --break-system-packages playwright`.
3. Se já existir um post com a data de hoje em `HISTORICO.md`, **parar**: o post do dia já foi feito.

## 2. Decidir o post

1. **Formato:** o oposto do último formato em `HISTORICO.md` (post único ↔ carrossel).
2. **Tema:** o primeiro item sem `[x]` em `PAUTA.md` que funcione no formato do dia e não repita os últimos 7 temas.
3. **Horário:** `getBestTimeToPostByNetwork` (Metricool, instagram, marca 7780320, hoje) → maior valor entre 10h e 20h
   com pelo menos 2h de antecedência; se não houver, 19h.

## 3. Criar a arte

1. Criar a pasta `ligflow/AAAA-MM-DD-<tema-em-kebab-case>/`.
2. Copiar o(s) modelo(s):
   - post único: `kit/modelos/post-unico.html` → `01.html`
   - carrossel: `kit/modelos/carrossel/1.html` … `6.html` → `01.html` … `06.html`
     (tela 1 = capa com "Arraste para o lado"; tela 6 = recursos + CTA; telas 2–5 = conteúdo, numeradas "N / 6")
3. Trocar **só os textos** (e, se preciso, a quantidade de itens repetindo o mesmo bloco), mantendo estrutura, cores,
   tamanhos e o marcador `{{LOGO}}`. Respeitar os fatos aprovados de `REGRAS.md`.
4. Rodar `python3 kit/render.py ligflow/<pasta>` e **olhar cada PNG** gerado: texto cortado, sobreposição,
   texto saindo da arte ou fonte errada → ajustar o HTML e renderizar de novo.

## 4. Publicar

1. Commit em português (`Adiciona post <formato>: <tema>`) e push para `main`.
2. Conferir que `https://raw.githubusercontent.com/lucasmendesinf/Post/main/ligflow/<pasta>/01.png` responde 200.
3. Metricool `createScheduledPost` (blogId 7780320, instagram, `instagramData.type` = `POST`, imagens na ordem
   `01.png` … `06.png`):
   - modo `publicar` em `REGRAS.md` → `autoPublish: true`, `draft: false`
   - modo `rascunho` → `draft: true`
4. Marcar o tema com `[x]` em `PAUTA.md` (com formato e data) e adicionar a linha em `HISTORICO.md`. Commit e push.

## 5. Avisar

Mandar ao Lucas uma mensagem curta: formato, tema, horário, a legenda e o link `plannerUrl` do Metricool.
Se algo falhar (render, push, Metricool), avisar o que falhou e **não** publicar parcialmente.
