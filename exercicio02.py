print("O usuário escolhe os números")
numeros = []
quantidade = int(input("Quantos números você quer digitar na lista? "))
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º "))
    numeros.append(numero)
print(f"Números digitados: {numeros}")   

#mostrar somente os números pares 
for i in numeros:
     if i %2 == 0:
          print(i)
          