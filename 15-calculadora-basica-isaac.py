while True: 
    print("##CALCULADORA##\n")
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. resto divisão")
    print("6. sair")
    
    opcao = int(input("digite um numero para selecionar a opção!!"))
    
    if opcao == 1:
        print("1. soma")
        num1 = float(input("digite o primeiro valor: "))
        num2 = float(input("digite o segundo valor: "))
        resultado = num1 + num2
        print("a soma dos valores foi:" ,  resultado,"\n")
    elif opcao == 2:
        print("2. subtração")
        num1 = float(input("digite o primeiro valor: "))
        num2 = float(input("digite o segundo valor: "))
        resultado = num1 - num2
        print("a subtração dos valores: ", resultado)
    elif opcao == 3:
        print("3. multiplicação")
        num1 = float(input("digite o primeiro valor: "))
        num2 = float(input("digite o segundo valor: "))
        resultado = num1  * num2
        print("a multiplicação dos valores: ", resultado)
    elif opcao == 4:
        print("4. divisão")
        num1 = float(input("digite o primeiro valor: "))
        num2 = float(input("digite o segundo valor: "))
        if num2 == 0:
            print("erro: divisão por zero")
        else:
            resultado = num1  / num2
            print("a divisão dos valores: ", resultado) 
    elif opcao == 5:
        print("5. resto divisão")
        num1 = float(input("digite o primeiro valor: "))
        num2 = float(input("digite o segundo valor: "))
        if num2 != 0:
            print("erro: divisão por zero")
        else:
            resultado = num1 % num2
            print("o resto da divisão de valores: ", resultado)
    elif opcao == 6:
        print("saindo da calculadora!!")
        break
    else:
        print("erro: opção invalida!!")
            
     
    