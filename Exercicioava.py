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



# Exercicio 19

n = int(input("Digite um número para ver sua tabuada: "))

# Mostra um título indicando qual tabuada será exibida
print(f"=== Tabuada de {n} ===\n")

# Laço de repetição de 0 até 10
for i in range(1, 11):
    # Mostra cada linha da tabuada: número x multiplicador = resultado
    print(n, " x ", i, "=", n * i)

# Exercicio 20

semanas = [ Segunda, terça, quarta, quinta, sexta]

for i in range(5):
    print(semanas)

# Exercicio 10