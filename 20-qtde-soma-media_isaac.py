soma = 0
contador = 0

while True: 
    numero = int(input('digite um numero inteiro (0 para sair): '))
    if numero == 0:
        break
    soma += numero
    contador += 1

if contador >0: 
    media = soma / contador
    
    print(f'a quantidade de numeros digitados: {contador}') 
    print(f'a soma dos numeros digitados: {soma}')
    print(f'a media dos numeros digitados: {media:.2f}')
else:
    print('não foi digitado nenhum numero')