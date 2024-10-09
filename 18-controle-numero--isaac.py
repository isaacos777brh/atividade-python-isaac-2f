contador = 0

while contador <= 100:
    contador += 1

    if (contador == 6):
        print("não vou mostrar o seis!!!")

    elif (contador >= 10 and contador <= 27):
        print(f"não vou mostrar o {contador}")
        continue
    print(contador)

    if contador == 40:
        break

print("fim do programa!!")



