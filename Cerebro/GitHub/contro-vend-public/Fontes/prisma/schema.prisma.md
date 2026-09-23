---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-dados]
source: https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/prisma/schema.prisma
source_commit: 8ca882161809413bbadfe4997e80a2ec7ae29991
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# prisma/schema.prisma

Origem: [Di20232/contro-vend-public](https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/prisma/schema.prisma). Versao consultada: 8ca882161809.

[[Cerebro/GitHub/contro-vend-public/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--contro-vend-public--8ca882161809.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```text
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

enum Role {
  ADMIN
  CASHIER
}

enum MovementType {
  ENTRY
  SALE
  ADJUSTMENT
  LOSS
}

model User {
  id           String          @id @default(uuid())
  name         String
  email        String          @unique
  passwordHash String
  role         Role            @default(CASHIER)
  active       Boolean         @default(true)
  createdAt    DateTime        @default(now())
  sales        Sale[]
  movements    StockMovement[]
}

model Product {
  id           String          @id @default(uuid())
  name         String
  barcode      String?         @unique
  category     String?
  unit         String          @default("UN")
  costPrice    Decimal         @db.Decimal(12, 2)
  salePrice    Decimal         @db.Decimal(12, 2)
  currentStock Decimal         @default(0) @db.Decimal(12, 3)
  minStock     Decimal         @default(0) @db.Decimal(12, 3)
  expiryDate   DateTime?
  active       Boolean         @default(true)
  createdAt    DateTime        @default(now())
  updatedAt    DateTime        @updatedAt
  saleItems    SaleItem[]
  movements    StockMovement[]

  @@index([name])
  @@index([active])
}

model Sale {
  id          String          @id @default(uuid())
  sellerId    String
  seller      User            @relation(fields: [sellerId], references: [id])
  totalAmount Decimal         @default(0) @db.Decimal(12, 2)
  canceled    Boolean         @default(false)
  createdAt   DateTime        @default(now())
  items       SaleItem[]
  movements   StockMovement[]

  @@index([createdAt])
  @@index([sellerId])
}

model SaleItem {
  id        String  @id @default(uuid())
  saleId    String
  sale      Sale    @relation(fields: [saleId], references: [id])
  productId String
  product   Product @relation(fields: [productId], references: [id])
  quantity  Decimal @db.Decimal(12, 3)
  unitPrice Decimal @db.Decimal(12, 2)
  subtotal  Decimal @db.Decimal(12, 2)

  @@index([saleId])
  @@index([productId])
}

model StockMovement {
  id            String       @id @default(uuid())
  productId     String
  product       Product      @relation(fields: [productId], references: [id])
  type          MovementType
  quantity      Decimal      @db.Decimal(12, 3)
  previousStock Decimal      @db.Decimal(12, 3)
  newStock      Decimal      @db.Decimal(12, 3)
  reason        String?
  userId        String
  user          User         @relation(fields: [userId], references: [id])
  saleId        String?
  sale          Sale?        @relation(fields: [saleId], references: [id])
  createdAt     DateTime     @default(now())

  @@index([productId, createdAt])
  @@index([type, createdAt])
}

```
