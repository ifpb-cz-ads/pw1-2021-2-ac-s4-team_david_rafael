salário = float(input("Digite o salário:"))
porcetagem_aumento = float(input("Digite a porcentagem de aumento:"))
aumento = salário * porcetagem_aumento / 100
novo_salário = salário + aumento
print("Aumento de R$ %.2f" % aumento)
print("Novo salário de R$ %.2f" % novo_salário)