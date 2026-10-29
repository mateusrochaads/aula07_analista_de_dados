'''

Construir um algoritmo que tenha a entrada de números inteiros escolhidos
pelo usuário. A quantidade será escolhida, também, pelo usuário e o algoritmo mostrará:
1 - uma lista com todos os números
2 - uma lista com números ímpares
3 - uma lista com os números em ordem crescente
4 - uma lista com os números em ordem decrescente
5 - uma lista com um número removido pelo usuário
'''

print(" --- Lista de números --- ")
numeros=[]
quantidade = int(input("Quantos números quer inserir na lista? "))
for i in range (quantidade):
    numero = int(input(f"{i+1}º número: "))
    numeros.append(numero)

print(f"Numeros da lista: {numeros}")

for i in numeros:
    if i %2 == 1:
        print(f"Números pares: {i}")
    else:
        print(f"Números ímpares: {i}")

numeros.sort()
print(f"Números em ordem crescente: {numeros}")
numeros.sort(reverse=True)
print(f"Números em ordem a decrescente: {numeros}")
numeros.sort(reverse=False)

numero_remove=input("Qual número quer remover?")
numero.remove(nome_remove)

print(f"Nova lista:{numeros}")