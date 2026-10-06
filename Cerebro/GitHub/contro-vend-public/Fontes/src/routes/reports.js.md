---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-dados]
source: https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/src/routes/reports.js
source_commit: 8ca882161809413bbadfe4997e80a2ec7ae29991
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# src/routes/reports.js

Origem: [Di20232/contro-vend-public](https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/src/routes/reports.js). Versao consultada: 8ca882161809.

[[Cerebro/GitHub/contro-vend-public/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--contro-vend-public--8ca882161809.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```javascript
const express = require('express');
const prisma = require('../db');
const { authenticate, authorize } = require('../auth');
const { getStockForecast, getSlowMovingProducts } = require('../forecast');
const { parseDateParam, clampIntParam } = require('../queryHelpers');

const router = express.Router();
router.use(authenticate, authorize('ADMIN'));

router.get('/forecast', async (req, res) => {
  res.json(await getStockForecast());
});

router.get('/sales-summary', async (req, res) => {
  const from = parseDateParam(req.query.from, 'from');
  const to = parseDateParam(req.query.to, 'to');
  const where = { canceled: false };
  if (from || to) where.createdAt = {};
  if (from) where.createdAt.gte = from;
  if (to) where.createdAt.lte = to;

  const sales = await prisma.sale.findMany({ where, select: { totalAmount: true, createdAt: true } });

  const byDay = {};
  let total = 0;
  for (const s of sales) {
    const day = s.createdAt.toISOString().slice(0, 10);
    byDay[day] = (byDay[day] || 0) + Number(s.totalAmount);
    total += Number(s.totalAmount);
  }

  res.json({ total, count: sales.length, byDay });
});

router.get('/top-products', async (req, res) => {
  const from = parseDateParam(req.query.from, 'from');
  const to = parseDateParam(req.query.to, 'to');
  const limit = clampIntParam(req.query.limit, { min: 1, max: 50, fallback: 10 });

  const saleWhere = { canceled: false };
  if (from || to) saleWhere.createdAt = {};
  if (from) saleWhere.createdAt.gte = from;
  if (to) saleWhere.createdAt.lte = to;

  const items = await prisma.saleItem.groupBy({
    by: ['productId'],
    where: { sale: saleWhere },
    _sum: { quantity: true, subtotal: true },
    orderBy: { _sum: { subtotal: 'desc' } },
    take: limit,
  });

  const products = await prisma.product.findMany({ where: { id: { in: items.map((i) => i.productId) } } });
  const nameById = new Map(products.map((p) => [p.id, p.name]));

  res.json(
    items.map((i) => ({
      productId: i.productId,
      name: nameById.get(i.productId) || 'Produto removido',
      quantitySold: Number(i._sum.quantity),
      revenue: Number(i._sum.subtotal),
    })),
  );
});

router.get('/slow-moving', async (req, res) => {
  const days = clampIntParam(req.query.days, { min: 1, max: 365, fallback: 60 });
  res.json(await getSlowMovingProducts(days));
});

module.exports = router;

```
