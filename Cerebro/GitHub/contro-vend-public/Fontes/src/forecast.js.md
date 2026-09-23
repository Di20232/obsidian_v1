---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-dados]
source: https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/src/forecast.js
source_commit: 8ca882161809413bbadfe4997e80a2ec7ae29991
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# src/forecast.js

Origem: [Di20232/contro-vend-public](https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/src/forecast.js). Versao consultada: 8ca882161809.

[[Cerebro/GitHub/contro-vend-public/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--contro-vend-public--8ca882161809.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```javascript
const prisma = require('./db');
const config = require('./config');

// Previsão simples: consumo médio diário nos últimos N dias (baseado em
// movimentações de venda) projetado sobre o estoque atual.
async function getStockForecast() {
  const windowDays = config.forecastWindowDays;
  const since = new Date(Date.now() - windowDays * 24 * 60 * 60 * 1000);

  const [products, sold] = await Promise.all([
    prisma.product.findMany({ where: { active: true }, orderBy: { name: 'asc' } }),
    prisma.stockMovement.groupBy({
      by: ['productId'],
      where: { type: 'SALE', createdAt: { gte: since } },
      _sum: { quantity: true },
    }),
  ]);

  const soldMap = new Map(sold.map((s) => [s.productId, Math.abs(Number(s._sum.quantity || 0))]));

  const forecast = products.map((p) => {
    const totalSold = soldMap.get(p.id) || 0;
    const avgDaily = totalSold / windowDays;
    const currentStock = Number(p.currentStock);
    const minStock = Number(p.minStock);
    const daysUntilStockout = avgDaily > 0 ? currentStock / avgDaily : null;

    return {
      productId: p.id,
      name: p.name,
      unit: p.unit,
      currentStock,
      minStock,
      avgDailySales: Number(avgDaily.toFixed(3)),
      daysUntilStockout: daysUntilStockout !== null ? Number(daysUntilStockout.toFixed(1)) : null,
      lowStock: currentStock <= minStock,
    };
  });

  forecast.sort((a, b) => {
    if (a.daysUntilStockout === null && b.daysUntilStockout === null) return 0;
    if (a.daysUntilStockout === null) return 1;
    if (b.daysUntilStockout === null) return -1;
    return a.daysUntilStockout - b.daysUntilStockout;
  });

  return forecast;
}

// Separa o resultado de getStockForecast() em "abaixo do mínimo" e
// "previsão de acabar em breve, mas ainda não abaixo do mínimo" — usado
// tanto no painel quanto no e-mail de alerta diário, que antes duplicavam
// exatamente esta mesma lógica de filtro em dois arquivos diferentes.
function splitForecastAlerts(forecast) {
  const lowStock = forecast.filter((p) => p.lowStock);
  const soonOut = forecast.filter((p) => !p.lowStock && p.daysUntilStockout !== null && p.daysUntilStockout <= 7);
  return { lowStock, soonOut };
}

// Produtos com estoque > 0 mas sem nenhuma venda registrada nos últimos
// `days` dias — ajuda a identificar capital parado em itens que não giram.
// Compartilhado entre o painel (janela fixa de 60 dias) e o relatório
// dedicado (janela configurável pelo usuário), que antes duplicavam a
// mesma sequência de consultas.
async function getSlowMovingProducts(days) {
  const since = new Date(Date.now() - days * 24 * 60 * 60 * 1000);

  const [stockedProducts, recentSales] = await Promise.all([
    prisma.product.findMany({
      where: { active: true, currentStock: { gt: 0 } },
      select: { id: true, name: true, currentStock: true, costPrice: true },
    }),
    prisma.stockMovement.groupBy({ by: ['productId'], where: { type: 'SALE', createdAt: { gte: since } }, _sum: { quantity: true } }),
  ]);

  const soldRecently = new Set(recentSales.map((r) => r.productId));
  return stockedProducts
    .filter((p) => !soldRecently.has(p.id))
    .map((p) => ({
      id: p.id,
      name: p.name,
      currentStock: Number(p.currentStock),
      capitalParado: Number((Number(p.currentStock) * Number(p.costPrice)).toFixed(2)),
    }));
}

module.exports = { getStockForecast, splitForecastAlerts, getSlowMovingProducts };

```
