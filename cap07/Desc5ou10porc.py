compra = float(input("Digite o valor da sua compra: "))
if compra > 300:
    compra_com_desconto = compra * 0.9
else:
    compra_com_desconto = compra * 0.95
print(f"Valor da compra.....: R$ {compra:.2f}\nValor atualizado....: R$ {compra_com_desconto:.2f}")