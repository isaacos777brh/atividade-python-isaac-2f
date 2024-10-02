def par (x):
    return x % 2 == 0

def par_ou_impar(x):
    if par(x):
        return "par"
    else:
        return "impar"

valor = 0
while valor !='sair':
    valor = input("Digite um valor ou 'sair' para sair: ")
    if valor !='sair':
        print(par_ou_impar(int(valor)))
    else:
        print("fim do programa")