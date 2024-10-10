def converte_fahrenheit_celsius(f):
    graus = (f - 32) * 5/9
    return graus
def converte_kelvin_fahrenheit(k):
    graus = (k - 273.15) * 9/5 + 32
    return graus
def converte__kelvin_celsius(k):
    graus = k-273.15
    return graus
def converte_fahrenheit_kelvin(f):
    graus = c * (9/5) + 32
    return graus
def converte_celsius_fahrenheit(c):
    graus = c * 9/5 + 32
    return graus
def converte_celsius_kelvin(c):
    graus = c + 273.15
    return graus
def exibirMenu():
    print("bem vindo a calculadora de temperatura maninho!!")
    print("1. Convert. Fahrenheit para Celsius!")
    print("2. Convert. Kelvin para Fahrenheit!")
    print("3. Convert. Kelvin para Celsius!")
    print("4. Convert. Fahrenheit para Kelvin!")
    print("5. Convert. Celsius para Fahrenheit!")
    print("6. Convert. Celsius para Kelvin!")
    print("7. Sair!")

while True:
    exibirMenu()

    opcao = int(input("digite a temperatura que voce deseja calcular: "))

    if opcao == 1:
        print("vc quer passar de Fahrenheit para Celsius?? certo! aqui esta!!")
        f = float(input("Digite quantos graus Fahrenheit fazem: "))
        print(f"aqui esta o resultado: {converte_fahrenheit_celsius(f):.2f}° C\n\n")

    elif opcao == 2:
        print("vc quer passar de Kelvin para Fahrenheit?? certo! aqui esta!!")
        k = float(input("Digite quantos graus Kelvin fazem: "))
        print(f"aqui esta o resultado: {converte_kelvin_fahrenheit(k):.2f} °F \n\n")

    elif opcao == 3:
        print("vc quer passar de Kelvin para Celsius?? certo! aqui esta!!")
        k = float(input("Digite quantos graus Kelvin fazem: "))
        print(f"aqui esta o resultado: {converte__kelvin_celsius(k):.2f} °C \n\n")

    elif opcao == 4:
        print("vc quer passar de Fahrenheit para Kelvin?? certo! aqui esta!!")
        f = float(input("Digite quantos graus Fahrenheit fazem: "))
        print(f"aqui esta o resultado: {converte_fahrenheit_kelvin(f):.2f} K \n\n")

    elif opcao == 5:
        print("vc quer passar Celsius para Fahrenheit?? certo! aqui esta!!")
        c = float(input("Digite quantos graus Celsius fazem: "))
        print(f"aqui esta o resultado: {converte_celsius_fahrenheit(f):.2f} °F \n\n")
    elif opcao == 6:
        print("vc quer passar de Celsius para Kelvin?? certo! aqui esta!!")
        c = float(input("Digite quantos graus Celsius fazem: "))
        print(f"aqui esta o resultado: {converte_celsius_kelvin(c):.2f} K \n\n")

    elif opcao == 7:
        print("saindo do programa...\n\n")
        break

    else:
        print("opção inválida!! digite novamente, um certo dessa vez por favor!\n\n")