# Post — conteúdo do Instagram @calutec.solucoes

Imagens, vídeos e regras dos posts automáticos do LigFlow e da Calutec (agendados pelo Claude via Metricool).

Agenda: segunda a quarta LigFlow, quinta a sábado sites e sistemas da Calutec, domingo vídeo (Reels + stories).

## Onde mexer

| Quero… | Arquivo |
| --- | --- |
| Mudar regras, tom, o que pode ser dito, horário, publicar direto ou como rascunho | `REGRAS.md` |
| Sugerir ou reordenar temas | `PAUTA.md` |
| Ver o que já foi postado | `HISTORICO.md` |
| Mudar o visual (avisar o Claude antes) | `kit/modelos/` |

Para editar pelo celular ou navegador: abra o arquivo no GitHub → ícone de lápis → editar → **Commit changes**.

## Estrutura

- `ligflow/AAAA-MM-DD-tema/` e `calutec/AAAA-MM-DD-tema/` — imagens e vídeos de cada post (públicos: o Metricool busca daqui).
- `kit/` — logos, fonte Saira, modelos HTML e `render.py` (gera os PNG 1080×1350).
- `kit/video/` — gerador dos vídeos de domingo (`gerar_video.py` + roteiro JSON → MP4 1080×1920).
- `videos-prontos/` — vídeos já aprovados, que a rotina usa no domingo do tema indicado na pauta.
- `ROTINA.md` — passo a passo técnico que a tarefa diária segue.

> Este repositório é público: não coloque aqui nada sigiloso (senhas, dados de clientes, listas de leads).
