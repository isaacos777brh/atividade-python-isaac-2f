def exibirMensagem(nome, idade):
    print(f"Olá, {nome} com {idade} anos!")


def somar(a, b):
    return a + b

def calcularAreaCirculo(raio):
    area = 3.1415 * raio**2
    return area


# inicio do meu algoritmo 
nome = input("digite seu nome, amiguinho!!! ")
idade = int(input("digite sua idade, amiguinho!!! "))
exibirMensagem(nome, idade) # exibe a mensagem com o nome do usuario!

valorA = int(input("digite o primeiro numero: "))
valorB = int(input("digite o segundo numero: "))
resultado = somar(valorA, valorB)
print(f"o resultado da soma foi: {resultado}")

# calcular area do circulo
print("area do circulo!!")
raio = float(input("digite o valor do raio: "))
area = calcularAreaCirculo(raio)
print(f"a area do circulo : {area:.2f}")