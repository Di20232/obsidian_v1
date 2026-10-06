---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-dados]
source: https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/src/routes/users.js
source_commit: 8ca882161809413bbadfe4997e80a2ec7ae29991
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# src/routes/users.js

Origem: [Di20232/contro-vend-public](https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/src/routes/users.js). Versao consultada: 8ca882161809.

[[Cerebro/GitHub/contro-vend-public/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--contro-vend-public--8ca882161809.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```javascript
const express = require('express');
const { z } = require('zod');
const prisma = require('../db');
const validate = require('../validate');
const httpError = require('../httpError');
const { authenticate, authorize, hashPassword } = require('../auth');

const router = express.Router();
router.use(authenticate, authorize('ADMIN'));

const createSchema = z.object({
  name: z.string().trim().min(1).max(120),
  email: z.string().trim().email().max(255),
  password: z.string().min(8, 'A senha precisa ter ao menos 8 caracteres.').max(200),
  role: z.enum(['ADMIN', 'CASHIER']).default('CASHIER'),
});

const updateSchema = z.object({
  name: z.string().trim().min(1).max(120).optional(),
  role: z.enum(['ADMIN', 'CASHIER']).optional(),
  active: z.boolean().optional(),
  password: z.string().min(8).max(200).optional(),
});

router.get('/', async (req, res) => {
  const users = await prisma.user.findMany({
    select: { id: true, name: true, email: true, role: true, active: true, createdAt: true },
    orderBy: { name: 'asc' },
  });
  res.json(users);
});

router.post('/', validate(createSchema), async (req, res) => {
  const { name, email, password, role } = req.body;
  const existing = await prisma.user.findUnique({ where: { email: email.toLowerCase() } });
  if (existing) throw httpError(409, 'Já existe um usuário com este e-mail.');

  const passwordHash = await hashPassword(password);
  let user;
  try {
    user = await prisma.user.create({ data: { name, email: email.toLowerCase(), passwordHash, role } });
  } catch (err) {
    if (err.code === 'P2002') throw httpError(409, 'Já existe um usuário com este e-mail.');
    throw err;
  }
  res.status(201).json({ id: user.id, name: user.name, email: user.email, role: user.role, active: user.active });
});

router.put('/:id', validate(updateSchema), async (req, res) => {
  const data = req.body;

  // Evita que o administrador se autoexclua/rebaixe por engano e fique trancado fora do sistema.
  if (req.params.id === req.user.sub) {
    if (data.active === false) throw httpError(400, 'Você não pode desativar seu próprio usuário.');
    if (data.role && data.role !== 'ADMIN') throw httpError(400, 'Você não pode remover seu próprio acesso de administrador.');
  }

  const existing = await prisma.user.findUnique({ where: { id: req.params.id } });
  if (!existing) throw httpError(404, 'Usuário não encontrado.');

  const update = {};
  if (data.name !== undefined) update.name = data.name;
  if (data.role !== undefined) update.role = data.role;
  if (data.active !== undefined) update.active = data.active;
  // O hash (bcrypt, ~12 rounds) só é calculado depois de confirmar que o
  // usuário existe — evita gastar CPU cara de hashing em requisições para
  // IDs inexistentes, o que serviria de amplificador de custo para um
  // atacante disparando muitas requisições PUT em sequência.
  if (data.password) update.passwordHash = await hashPassword(data.password);

  const user = await prisma.user.update({ where: { id: req.params.id }, data: update });
  res.json({ id: user.id, name: user.name, email: user.email, role: user.role, active: user.active });
});

module.exports = router;

```
