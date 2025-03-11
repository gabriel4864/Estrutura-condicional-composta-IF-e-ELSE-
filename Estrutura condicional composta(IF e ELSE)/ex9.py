# Desconto em compras por valor mínimo
Conta = float(input("Digite o valor da conta: "))
if Conta > 150:
    Valor = Conta - 20
    print("Voce pagara", Valor)
else:
    Valor = Conta
    print("Voce pagara", Valor)