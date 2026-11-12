# Regras de postagem — Instagram @calutec.solucoes

> Este é o arquivo que você (Lucas) edita para mudar o comportamento das postagens automáticas.
> Pode editar direto no GitHub, pelo navegador ou celular (ícone de lápis). A próxima execução já segue a versão nova.

## Agenda da semana

| Dia | Assunto | Formato |
| --- | --- | --- |
| Segunda, terça e quarta | **LigFlow** | alterna **post único** e **carrossel** (6 telas) |
| Quinta, sexta e sábado | **Calutec: sites e sistemas** | **post único** no modelo Calutec |
| Domingo | **Vídeo** | o mesmo vídeo vai para o **Reels** e para os **stories** |

## Configuração

- **Perfil:** Instagram @calutec.solucoes (marca Metricool 7780320, fuso America/Sao_Paulo)
- **Horário:** o melhor horário do dia segundo o Metricool, entre 10h e 20h, com pelo menos 2h de antecedência.
- **Modo de publicação:** `publicar`
  - `publicar` = agenda e o post sai sozinho no horário.
  - `rascunho` = fica como rascunho no Metricool e só sai depois que eu aprovar.

## Visual (não mudar sem combinar)

### LigFlow (segunda a quarta)
- Modelos de post único em `kit/modelos/ligflow/` (`painel`, `celular`, `manchete`, `notificacoes`) e carrossel em `kit/modelos/ligflow/carrossel/1.html` a `6.html`.
- Fundo preto `#000000`, vermelho `#EE3124`, laranja `#FF8A00`, amarelo `#FFCF22`, cinza `#B7B7B7`, cartões `#1D1D1D` com borda `#343434`.
- Logo do LigFlow (`kit/logo-ligflow.png`).

### Calutec — sites e sistemas (quinta a sábado)
- Modelos em `kit/modelos/calutec/`: `painel` (topo laranja, painel no meio, lista embaixo), `celular` (fundo laranja com celular mostrando um site) e `escuro` (fundo preto #1A1A1A com lista numerada).
- Laranja da logo `#FD5002`, branco `#FFFFFF`, preto `#1A1A1A`, apoio pêssego `#FFF6F0` / `#FFD3B8` / `#FFB27A`.
- Logo da Calutec (`kit/logo-calutec.png`) no quadrado preto arredondado, com "CALUTEC / SOLUÇÕES" ao lado.
- No modelo `painel`, o painel do meio pode mostrar um sistema (dashboard) ou um site (janela de navegador), conforme o tema. Sem números inventados: só barras e rótulos.

### Vídeo (domingo)
- Gerador: `kit/video/` (cenas animadas no estilo do vídeo de referência de 31/10). 1080×1920, 30 fps, 20 a 35 segundos.
- Tema `ligflow` (vermelho) ou `calutec` (laranja): alternar a cada domingo, começando por `calutec` em 08/11.
- Sempre termina com a cena final: logo + 2 ou 3 frases curtas + "Chama no direct" + @calutec.solucoes.
- **Música:** a faixa do vídeo de referência (`kit/video/musica.m4a`) vai embutida em todo vídeo gerado,
  então sai igual no Reels e nos stories. Nunca publicar vídeo sem áudio. Para trocar a música, substitua esse arquivo.

### Para todos
- Fonte Saira (títulos em itálico 900, caixa alta). Tamanho dos posts 1080×1350 (4:5).
- Sem emoji nas artes. Sem fotos de pessoas.
- Pode trocar textos, número de itens e cores de destaque dentro da paleta do assunto.

## Variação das artes (obrigatório)

O feed não pode parecer a mesma imagem repetida.

- **Nunca** usar o mesmo modelo/layout do post anterior do mesmo assunto, nem repetir um layout usado nos **últimos 3 posts** daquele assunto (ver coluna "Modelo" do `HISTORICO.md`).
- Sempre que possível, **criar um layout novo** (composição diferente: posição do título, ilustração, fundo, disposição dos elementos), mantendo a paleta, a fonte Saira e a logo do assunto. Layout novo que ficar bom é salvo em `kit/modelos/<ligflow|calutec>/<nome>.html` para entrar no rodízio.
- Ideias de composição para variar: celular/tela do sistema, manchete tipográfica com faixa diagonal, notificações empilhadas, lista numerada grande, comparativo lado a lado, pergunta gigante centralizada, número/ícone gigante, janela de navegador, fundo invertido (claro/escuro dentro da paleta).
- **Carrossel:** a capa também varia (não repetir a capa centralizada com logo + selo + título); as telas de dentro podem usar layouts diferentes entre si.
- Olhar também os 3 posts anteriores do **outro** assunto: o post do dia não pode parecer igual ao que está do lado no feed.

## O que pode ser dito

### LigFlow (fatos aprovados)
- Até **10 chamadas simultâneas**.
- O consultor **só fala com quem atendeu**; quem não atende fica para trás.
- Você **sobe sua lista de leads**; se ninguém atende, o sistema **parte sozinho para o próximo lote** de números.
- **Radar de Leads:** busca empresas por segmento, cidade e bairro e monta a lista pronta para discar.
- **Identifica caixa postal / secretária eletrônica.**
- **Gravação e transcrição** das ligações.
- **Agendar retornos e reuniões** com Google Agenda.
- **Relatórios** de chamadas, minutos e custos por consultor.
- Lista de bloqueio (não ligar para quem pediu para não receber ligação).

### Calutec — sites e sistemas (serviços aprovados)
- **Sites** institucionais e responsivos (funcionam no celular).
- **Landing pages** para campanhas e vendas.
- **Sistemas sob medida** para gestão: estoque, vendas e caixa, pedidos e delivery, relatórios.
- Sistemas para mais de uma empresa ou unidade no mesmo sistema.

## O que NÃO fazer

- Não inventar números, porcentagens, clientes ou depoimentos.
- Não citar nomes de clientes da Calutec sem estar escrito aqui.
- Estimativas (ex.: "~1 min por tentativa no celular", "até 10x mais tentativas") só com a nota "estimativa" visível na arte.
- Não citar preço, plano, prazo de entrega ou promoção sem estar escrito aqui.
- Não falar mal de concorrentes pelo nome.
- Não repetir o mesmo tema dos últimos 7 posts do mesmo assunto (ver `HISTORICO.md`).

## Legenda

- Português do Brasil, tom direto.
  - LigFlow: de consultor para consultor.
  - Calutec: de dono de negócio para dono de negócio.
- Estrutura: gancho (1 linha) → como funciona / benefício (2 a 5 linhas) → CTA.
  - CTA LigFlow: "Quer ver funcionando? Chama no direct 👇"
  - CTA Calutec: "Quer um orçamento? Chama no direct 👇"
- Pode usar emoji com moderação na legenda (máx. 4).
- Hashtags no final, 5 a 8:
  - LigFlow: base `#prospecção #vendas #telemarketing #consultor #crm #ligflow`
  - Calutec: base `#desenvolvimentoweb #sites #sistemas #landingpage #empreendedorismo #calutec`

## Público

- LigFlow: consultores e equipes que prospectam por telefone (consórcio, seguros, crédito, B2B), donos de escritório e supervisores de vendas.
- Calutec: donos de pequenas e médias empresas (comércio, distribuidoras, restaurantes, serviços) que precisam de site ou de um sistema de gestão.
