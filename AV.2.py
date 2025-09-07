
#avaliação 02
#lista
# Delano Ferreira Queiroz.
# Felipe Figueiredo da Silva.

#1

# Pede ao usuário um autógrafo (uma frase) e armazena na variável autografo_0
autografo_0 = input("Sou seu fã, me dá um autógrafo? ")

# Pede ao usuário seu nome e armazena na variável nome
nome = input("Qual é o seu nome? ")

# Exibe o autógrafo que o usuário digitou
print(autografo_0)

# Exibe o autógrafo junto com o nome da pessoa que assinou
print("Autógrafo assinado por:", nome)


#2

# Pede ao usuário para digitar sua idade e converte para inteiro
idade = int(input("Você tem quantos anos? "))

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    # Se for maior ou igual a 18, exibe a mensagem
    print("Aeeee, já pode ser pr@so")

#3


# Coletando informações do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
trabalho = input("Possui emprego? (sim/não): ")
saldo = float(input("Quanto você tem na conta bancária? "))

# Verificando condições para ser "adultinho"
tem_idade = idade >= 18
tem_trabalho = trabalho.lower() == "sim"
tem_saldo = saldo >= 1000  # Exemplo: mínimo de R$ 1000 na conta

if tem_idade and tem_trabalho and tem_saldo:
    print("Você já é adultinho 😎")
else:
    print("Ainda é molecote 😅")

#4  (funciona)
# Variáveis com diferentes tipos de dados
nome = "cirilo"      # string (texto)
idade = 13           # inteiro
nota = 7.5           # float (número decimal)
aprovado = True      # booleano (True ou False)

# Exibe o tipo de cada variável usando a função type()
print(type(nome))      # <class 'str'>
print(type(idade))     # <class 'int'>
print(type(nota))      # <class 'float'>
print(type(aprovado))  # <class 'bool'>

#5  (funciona)
#agora vou mudar um numero decimal pra inteiro

num_dec= 5.7
num_int= int(num_dec)

print(num_int)

# Exercicio 06

num1 = int(input("Insira primeiro número: "))
num2 = int(input("Insira segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print("\n Resultado dos números de acordo com as operações: \n")
print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)
# Exercicio 07

calc = float(input("Insira um número: "))

resultado = calc * calc

print("O qudrado do número inserido é: ",resultado)

# Exercicio 08

"""
Os operadores x++ e ++x se diferecenciam pois, x++ usa o valor atual e depois incrementa +1,
já ++x primeiro incrementa em +1 e depois usa o valor atualizado.

em python seria:
x += 1 ou x = x + 1

"""

# Exercicio 09
n1 = float(input("Insira um número: "))
n2 = float(input("Insira um número: "))

print(n1 == n2)
print(n1 != n2)
print(n1 > n2)
print(n1 < n2)
print(n1 >= n2)
print(n1 <= n2)

# Exercicio 10

num = float(input("Insira qualquer número:"))

if num > 10 and num < 100:
    print("Número se encontra nas determinações de 1 a 100")
else:
    print("Número não se encontra nas determinações de 1 a 100")

# Exercicio 11

num_qualquer=int(input("digite um numero qualquer: "))

if num_qualquer % 2 == 0:
    print("o numero é par")
else:
    print("o numero é impar")

# Exercicio 12

num1=print(int(input("digite um numero qualquer: ")))
num2=print(int(input("digite um numero qualquer: ")))
num3=print(int(input("digite um numero qualquer: ")))

if num1 > num2 > num3:
    print(num1, "é o maior número.")
if num2 > num1 > num3:
    print(num2, "é o maior número.")
if num3 > num1 > num2:
    print(num3, "é o maior número.")
else:
    print("os tres numeros sao iguais")


# Exercicio 16

x = 0

while x < 11:
    print(" valor de x é: ", x)

    x = x + 1

print("Processo encerrado.")

# Exercicio 17

soma = 0

# Pede ao usuário para digitar um número inteiro
n = int(input("Digite um número: "))

print("\nSequência dos números pares até", n, ":")
for i in range(2, n+1, 2):
    print(i, end=" ")  # mostra cada número par na mesma linha
    soma += i

# Pula uma linha após a sequência
print("\n")

# Mostra o resultado final da soma de todos os números pares
print("A soma dos pares é:", soma)

# Exercicio 18

soma = 0
contador = 0
numero = 1 

while numero != 0:
    numero = int(input("Digite um número (0 para encerrar): "))
    if numero != 0:
        soma += numero
        contador += 1

if contador > 0:
    media = soma / contador
    print("A média é:", media)
else:
    print("Nenhum número foi digitado.")

# Exercicio 19

n = int(input("Digite um número para ver sua tabuada: "))

# Mostra um título indicando qual tabuada será exibida
print(f"=== Tabuada de {n} ===\n")

# Laço de repetição de 0 até 10
for i in range(1, 11):
    # Mostra cada linha da tabuada: número x multiplicador = resultado
    print(n, " x ", i, "=", n * i)

# Exercicio 20

# Lista com os dias da semana
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", 
                  "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

# Usando for para exibir os dias
for dia in dias_semana:
    print(dia)

# Exercicio 21



# Exercicio 22



# Exercicio 23



# Exercicio 24



# Exercicio 25

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

def reajustar_preco(produto, percentual):
    produto.preco = produto.preco + produto.preco * (percentual / 100)

produto1 = Produto("Caneta", 2.5)
produto2 = Produto("Caderno", 15)
produto3 = Produto("Borracha", 1.2)

produtos = [produto1, produto2, produto3]

for p in produtos:
    reajustar_preco(p, 10)
    print(p.nome, "novo preço:", p.preco)
    

# Exercicio 26

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))


# Exercicio 27

frutas = ("Maracujá", "Banana", "Tangerina", "Uva", "Manga", "Melância")

for fruta in frutas:
    print(fruta)
    
# Exercicio 28

numeros_media = []
print("\n=== Média de 5 números ===")
for i in range(5):
    numero = float(input("Digite um número: "))
    numeros_media.append(numero)

media = sum(numeros_media) / len(numeros_media)
print("A média dos números é:", media)


# Exercicio 29

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Bruno", 30)
pessoa3 = Pessoa("Carla", 22)

pessoas = [pessoa1, pessoa2, pessoa3]
print("\n=== Pessoas ===")
for p in pessoas:
    print("Nome:", p.nome, "- Idade:", p.idade)

# Exercicio 30

# Inicializa a matriz
matriz = []

# Preenche a matriz
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um número: "))
        linha.append(valor)
    matriz.append(linha)

# Mostra a matriz
print("Matriz 3x3:")
for linha in matriz:
    print(linha)

