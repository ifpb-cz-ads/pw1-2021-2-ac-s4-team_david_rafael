preco = float(input("Digite o preço:"))
porcetagem_desconto = float(input("Digite a porcentagem de desconto:"))
aumento = preco * porcetagem_desconto / 100
novo_preco= preco - aumento
print("desconto de R$ %.2f" % aumento)
print("Novo salário de R$ %.2f" % novo_preco)