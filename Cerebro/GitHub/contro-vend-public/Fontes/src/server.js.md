---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-dados]
source: https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/src/server.js
source_commit: 8ca882161809413bbadfe4997e80a2ec7ae29991
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# src/server.js

Origem: [Di20232/contro-vend-public](https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/src/server.js). Versao consultada: 8ca882161809.

[[Cerebro/GitHub/contro-vend-public/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--contro-vend-public--8ca882161809.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```javascript
const app = require('./app');
const config = require('./config');
const { scheduleDailyAlerts } = require('./jobs/dailyAlerts');

// Rede de segurança contra falha catastrófica do processo: qualquer erro que,
// por algum descuido, escape do tratamento normal do Express (ex: uma
// promise rejeitada fora do ciclo de requisição) é registrado em vez de
// derrubar o servidor inteiro. Exceções síncronas não tratadas (uncaughtException)
// deixam o processo em estado potencialmente inconsistente — nesse caso registramos
// e encerramos de forma controlada, para que o gerenciador de processo (Docker,
// Render, PM2 etc.) reinicie o serviço automaticamente, em vez de deixá-lo travado
// ou corrompido no ar.
process.on('unhandledRejection', (reason) => {
  console.error('[fatal] Promise rejeitada sem tratamento:', reason);
});

process.on('uncaughtException', (err) => {
  console.error('[fatal] Exceção não tratada — encerrando para reinício controlado:', err);
  process.exit(1);
});

const server = app.listen(config.port, () => {
  console.log(`Contro Vend rodando na porta ${config.port} (${config.nodeEnv})`);
  scheduleDailyAlerts();
});

function shutdown(signal) {
  console.log(`[server] ${signal} recebido, encerrando graciosamente...`);
  server.close(() => process.exit(0));
  // Se alguma conexão ficar pendurada, força o encerramento em vez de travar o processo.
  setTimeout(() => process.exit(1), 10_000).unref();
}

process.on('SIGTERM', () => shutdown('SIGTERM'));
process.on('SIGINT', () => shutdown('SIGINT'));

```
