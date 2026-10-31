# Rotina diária de postagem (instruções para o Claude)

Executada todo dia pela tarefa agendada. Siga na ordem. Leia antes `REGRAS.md`, `PAUTA.md` e `HISTORICO.md`:
as regras e a pauta mandam; este arquivo só descreve o passo a passo técnico.

## 1. Preparar

1. Clonar/atualizar `lucasmendesinf/Post` (branch `main`).
2. Conferir que `python3 -c "import playwright"` funciona, que existe `/usr/bin/google-chrome` (ou Chromium) e `ffmpeg`.
   Se faltar Playwright: `pip install --break-system-packages playwright`.
3. Se já existir um post com a data de hoje em `HISTORICO.md`, **parar**: o post do dia já foi feito.

## 2. Decidir o post pelo dia da semana (fuso America/Sao_Paulo)

| Dia | Assunto | Formato | Modelo |
| --- | --- | --- | --- |
| Seg, Ter, Qua | LigFlow | oposto do último post único/carrossel de LigFlow no histórico | `kit/modelos/post-unico.html` ou `kit/modelos/carrossel/` |
| Qui, Sex, Sáb | Calutec | post único | `kit/modelos/calutec/post-unico.html` |
| Dom | Vídeo | Reel + Story (mesmo arquivo) | `kit/video/` |

- **Tema:** o primeiro item sem `[x]` na seção do assunto em `PAUTA.md`, sem repetir os últimos 7 temas daquele assunto.
- **Horário:** `getBestTimeToPostByNetwork` (Metricool, instagram, marca 7780320, hoje) → maior valor entre 10h e 20h
  com pelo menos 2h de antecedência; se não houver, 19h.

## 3a. Criar a arte (segunda a sábado)

1. Pasta: `ligflow/AAAA-MM-DD-<tema>/` para LigFlow, `calutec/AAAA-MM-DD-<tema>/` para Calutec.
2. Copiar o(s) modelo(s) do dia:
   - post único: o modelo → `01.html`
   - carrossel: `kit/modelos/carrossel/1.html` … `6.html` → `01.html` … `06.html`
     (tela 1 = capa com "Arraste para o lado"; tela 6 = recursos + CTA; telas 2–5 = conteúdo, numeradas "N / 6")
3. Trocar **só os textos** (e, se preciso, a quantidade de itens repetindo o mesmo bloco), mantendo estrutura, cores,
   tamanhos e os marcadores `{{LOGO}}` / `{{LOGO_CALUTEC}}`. No modelo Calutec, o painel do meio pode virar uma janela
   de navegador (temas de site) ou continuar como painel de sistema. Respeitar o que `REGRAS.md` permite dizer.
4. Rodar `python3 kit/render.py <pasta>` e **olhar cada PNG** gerado: texto cortado, sobreposição,
   texto saindo da arte ou fonte errada → ajustar o HTML e renderizar de novo.

## 3b. Criar o vídeo (domingo)

1. Se o tema da pauta indicar **vídeo pronto** (arquivo em `videos-prontos/`), copiar esse MP4 para a pasta do dia
   como `video.mp4`, conferir que tem áudio e pular direto para "4. Publicar". Não gerar outro.
   Caso contrário, criar a pasta `<ligflow|calutec>/AAAA-MM-DD-video-<tema>/` e seguir os passos abaixo.
2. Escrever `roteiro.json` a partir de `kit/video/exemplo-roteiro.json`:
   - `tema`: `ligflow` ou `calutec` (alternar a cada domingo, ver `HISTORICO.md`).
   - Cenas disponíveis: `gancho`, `lista` (com `busca` digitando, `status` que mudam com `em` em segundos,
     `apagar_em`, `barra`, `pino`, `nota`), `agenda` (reunião + gravação), `numero` (contador grande),
     `grade` (10 linhas discando lado a lado, com destaque para quem atendeu), `comparativo` (duas colunas
     com ✕ e ✓ e uma frase de efeito) e `final` (logo + frases + CTA).
   - Exemplos completos: `kit/video/exemplo-roteiro.json` (estilo do vídeo de referência) e
     `kit/video/exemplo-roteiro-2.json` (contador + grade + comparativo). Variar a combinação de cenas a cada vídeo.
   - Duração total entre 20 e 35 segundos. Começar com `gancho` e terminar com `final`.
   - Nomes nas listas sempre genéricos (ex.: "Lead 01", "Cliente Exemplo"), nunca clientes reais.
3. Rodar `python3 kit/video/gerar_video.py <pasta>/roteiro.json <pasta>/video.mp4` (cerca de 1 minuto).
   A música `kit/video/musica.m4a` entra automaticamente. Conferir com `ffprobe` que o vídeo tem trilha de áudio;
   se não tiver, **não publicar** e avisar o Lucas.
4. Extrair quadros para conferir (`ffmpeg -i video.mp4 -vf "fps=1/2.5,scale=270:480,tile=6x2" -frames:v 1 quadros.png`)
   e **olhar**: textos cortados, sobreposição, cena vazia. Corrigir o roteiro e gerar de novo se preciso.
   Não fazer commit de `quadros.png`.

## 4. Publicar

1. Commit em português (`Adiciona <post único|carrossel|vídeo> <assunto>: <tema>`) e push para `main`.
2. Conferir que o link `https://raw.githubusercontent.com/lucasmendesinf/Post/main/<pasta>/<arquivo>` responde 200.
3. Metricool `createScheduledPost` (blogId 7780320, network instagram):
   - modo `publicar` em `REGRAS.md` → `autoPublish: true`, `draft: false`; modo `rascunho` → `draft: true`.
   - **post único / carrossel:** `instagramData.type` = `POST`, imagens na ordem `01.png` … `06.png`.
   - **domingo:** dois agendamentos no mesmo horário com o mesmo `video.mp4`:
     1. `type` = `REEL`, com legenda e `showReelOnFeed: true`. **Não** usar `audioConfiguration`: a música já está
        embutida no vídeo.
     2. `type` = `STORY`, **sem texto**.
4. Marcar o tema com `[x]` em `PAUTA.md` (com formato e data) e adicionar a linha em `HISTORICO.md`. Commit e push.

## 5. Avisar

Mandar ao Lucas uma mensagem curta: assunto, formato, tema, horário, a legenda e o link `plannerUrl` do Metricool.
Se algo falhar (render, vídeo, push, Metricool), avisar o que falhou e **não** publicar parcialmente.
