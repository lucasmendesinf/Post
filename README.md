# Post — conteúdo do Instagram @calutec.solucoes

Imagens e regras dos posts automáticos do LigFlow (agendados pelo Claude via Metricool).

## Onde mexer

| Quero… | Arquivo |
| --- | --- |
| Mudar regras, tom, o que pode ser dito, horário, publicar direto ou como rascunho | `REGRAS.md` |
| Sugerir ou reordenar temas | `PAUTA.md` |
| Ver o que já foi postado | `HISTORICO.md` |
| Mudar o visual (avisar o Claude antes) | `kit/modelos/` |

Para editar pelo celular ou navegador: abra o arquivo no GitHub → ícone de lápis → editar → **Commit changes**.

## Estrutura

- `ligflow/AAAA-MM-DD-tema/` — imagens de cada post (públicas: o Metricool busca daqui).
- `kit/` — logo, fonte Saira, modelos HTML e `render.py` (gera os PNG 1080×1350).
- `ROTINA.md` — passo a passo técnico que a tarefa diária segue.

> Este repositório é público: não coloque aqui nada sigiloso (senhas, dados de clientes, listas de leads).
