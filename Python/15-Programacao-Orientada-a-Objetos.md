---
tags: [python, poo]
cssclasses: [cerebro-nota, cerebro-python]
---

# Programação Orientada a Objetos (POO)

## O problema que isso resolve

Em [[09-Listas-Tuplas-Dicionarios]], você viu que um dicionário como `{"nome": "Diego", "idade": 25}` já agrupa dados relacionados. Mas conforme um programa cresce, você também quer agrupar **dados e comportamento** juntos — por exemplo, um "Usuário" não é só nome e idade, ele também pode "fazer login", "atualizar perfil". POO é um jeito de modelar isso: você cria um **molde** (classe) que descreve tanto os dados quanto as ações de algo, e depois cria quantas **instâncias** (objetos) desse molde precisar.

Você já usa objetos sem perceber: uma string tem métodos (`"oi".upper()`, visto em [[10-Strings]]) porque, por trás, uma string **é** um objeto em Python. Tudo em Python, na verdade, é objeto — POO só te dá o poder de criar os seus próprios tipos.

## Classe: o molde

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def se_apresentar(self):
        print(f"Oi, eu sou {self.nome} e tenho {self.idade} anos")
```

Desmontando:
- `class Pessoa:` — define um novo tipo chamado `Pessoa`.
- `__init__` é um método especial chamado **construtor**: roda automaticamente toda vez que um novo objeto `Pessoa` é criado, e serve para configurar seus dados iniciais.
- `self` representa "esta instância específica do objeto" — é sempre o primeiro parâmetro de métodos dentro de uma classe, e o Python o passa automaticamente (você não escreve isso na hora de chamar o método).
- `self.nome = nome` guarda o valor recebido como um **atributo** do objeto — um dado que pertence a ele.

## Criando objetos (instâncias)

```python
pessoa1 = Pessoa("Diego", 25)
pessoa2 = Pessoa("Ana", 30)

pessoa1.se_apresentar()   # "Oi, eu sou Diego e tenho 25 anos"
pessoa2.se_apresentar()   # "Oi, eu sou Ana e tenho 30 anos"

print(pessoa1.nome)        # acessa o atributo diretamente -> "Diego"
```

Cada objeto criado a partir da classe tem **seus próprios valores** para `nome` e `idade`, mesmo compartilhando o mesmo molde. Isso é a diferença central em relação a apenas usar dicionários soltos: o comportamento (`se_apresentar`) vem junto, colado ao dado, em vez de ser uma função separada que você teria que lembrar de associar manualmente.

## Métodos que alteram o próprio objeto

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

conta = ContaBancaria("Diego")
conta.depositar(100)
conta.sacar(30)
print(conta.saldo)   # 70
```

Note que `self.saldo` persiste entre chamadas de métodos diferentes — é o estado interno do objeto, mantido enquanto ele existir.

## Herança: reaproveitar um molde para criar variações

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):        # Cachorro herda de Animal
    def emitir_som(self):       # sobrescreve o comportamento do "pai"
        print(f"{self.nome} diz: Au au!")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")

animais = [Cachorro("Rex"), Gato("Mimi")]
for animal in animais:
    animal.emitir_som()
```

**Por que herança existe**: evita reescrever tudo que é comum entre tipos parecidos (`Cachorro` e `Gato` são ambos `Animal`, e compartilham a estrutura de ter um `nome`), enquanto ainda permite que cada um se comporte de forma diferente onde precisa (`emitir_som`).

## Quando vale a pena usar POO

Para scripts pequenos e diretos (como os exercícios anteriores deste curso), funções simples já bastam — POO adiciona uma camada de organização que só compensa quando o problema tem **entidades com estado e comportamento próprios que se repetem** (usuários, produtos, contas, veículos...). Não é "a forma certa" universal de programar, é **uma ferramenta a mais** para o tipo certo de problema.

## Exercício

Crie uma classe `Produto` com atributos `nome` e `preco`, e um método `aplicar_desconto(percentual)` que reduz `self.preco` proporcionalmente. Crie 3 produtos, aplique descontos diferentes em cada um, e imprima o preço final de cada um usando um `for`.

---
Veja o exemplo em `Python/exemplos/15_poo.py`. Próxima nota: [[16-Boas-Praticas-e-Proximos-Passos]]
