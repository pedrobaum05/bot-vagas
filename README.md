# bot-vagas

Fase 1 - (`feature/bot-basico`): bot do Telegram feito em Python que responde ao comando `/start`.
Aprendi a criar o Bot no BotFather e a configurar o projeto com variáveis de ambiente.
Usei um ambiente virtual (`.venv`) para isolar as bibliotecas do projeto e um `requirements.txt` com as versões fixas.
O bot só responde ao meu `chat_id`, e ás logs foram configuradas para não aparecerem.
Pratiquei o fluxo de Git: branch por fase, commits pequenos com mensagens claras e, no final, Pull Request para a `main`.

## Fase 2: Scraper (feature/scraper)

- Usei a biblioteca `requests` para pedir vagas à API de issues do GitHub, com filtros (`params`), um `User-Agent` que identifica o projeto e `timeout` para não esperar para sempre ás vagas que vem da API.
- Tratei erros com `try/except` e conferi o `status_code`: se algo falha, a função devolve lista vazia e o programa não quebra.
- Fiz o crawling com um loop que percorre as páginas, com `time.sleep(1)` entre elas para não sobrecarregar o servidor.
- Fiz o scraping montando uma ficha (dicionário) com título, link, fonte, id e nível de cada vaga, usando `.get` porque dados da internet não são confiáveis.
- Descarto pull requests e issues de regras (usando um `set`) e não há segredos no código: conferi o repositório e rodei o `pip-audit`.