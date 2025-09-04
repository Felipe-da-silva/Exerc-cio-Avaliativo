
#avaliação 02
#lista
#Delano Ferreira Queiroz

#1

autografo-0 = input("sou seu fã, me dá um autógrafo?")

print(autografo-0)

#2

idade=int(input("vc tem quantos anos? "))

if idade >= 18:
    print("aeeee ja pode ser pr@so")


#3


nome(input("digite seu nome: "))
idade(int(input("digite sua idade: ")))
trabalho("possui emprego?(sim/não): ")
saldo-em-conta(float(input("quanto vc tem na sua conta bancaria? ")))

#condição pra ser adulto
idade = true
trabalho = true
saldo = true

if idade and trabalho and saldo:
    print("vc já é adultinho")
else:
    print("ainda é molecote")

#4  (funciona)
nome = "cirilo"
idade = 13
nota = 7.5
aprovado = True

print(type(nome))
print(type(idade))
print(type(nota))
print(type(aprovado))


#5  (funciona)
#agora vou mudar um numero decimal pra inteiro

num_dec= 5.7
num_int= int(num_dec)

print(num_int)

#11  (funciona)

num_qualquer=int(input("digite um numero qualquer: "))

if num_qualquer % 2 == 0:
    print("o numero é par")
else:
    print("o numero é impar")

#12
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