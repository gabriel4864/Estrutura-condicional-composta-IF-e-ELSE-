# Cálculo de gorjeta
Valor = float(input("Digite o valor da conta: "))
if Valor > 100:
    Conta = (Valor * 0.1) + Valor
    print("Valor com a gorjeta inclusa", Conta)
else:
    Conta = (Valor * 0.05) + Valor
    print("Valor com a gorjeta inclusa", Conta)