# atividade aula  de tabuada
# fazer um programa que mostre a tabuada
numero = int(input("Digite um numero para ver a sua tabuada: "))
contador = 1
while contador <=10:
    resultado = numero * contador
    print(f"{numero} X {contador} = {resultado}")
    contador +=1  
