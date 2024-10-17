print('bem vindo a tabuada de Isaac com for!!!')
numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada de {numero}:")
for i in range(1, 11):  
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")