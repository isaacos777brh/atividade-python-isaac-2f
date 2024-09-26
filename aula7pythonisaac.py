print("calculadora de IMC, atualizada em python!!")

peso = float(input("digite seu peso vei!: "))
altura = float(input("digite sua altura vei: "))

imc = peso / (altura ** 2)
print(f"seu IMC é {imc:.2f}")

if (imc < 18.5):
    print("abaixo do peso mano, melhore por favor")
elif (imc >= 18.5 and imc <= 24.9):
    print("peso normal mano, siga sua vida!!!")
elif (imc >= 25.0 and imc <= 34.9):
    print("ta um pouco sobre o peso ein, da pra recuperar!!")
else:
    print("ta obeso mano, voce vai melhorar, tamo junto vei!!")

