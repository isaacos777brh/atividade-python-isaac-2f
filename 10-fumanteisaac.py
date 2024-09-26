cigarros = int(input("quantos cigarros voce usa no dia?? "))
anos = float(input("quantos anos na ativa?? "))

reducao_minutos = anos * 365 * cigarros * 10
reducaodias = reducao_minutos / (24 * 60)
print("seu tempo de vida perdido foi: ", reducaodias)
