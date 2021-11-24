km = int(input("Digite a quantidade de quilometros percorridos:"))
dias = int(input("Digite quantos dias você ficou com o carro:"))
preço_dia = 60
preço_km = 0.15
preço_pagar = km * preço_km + dias * preço_dia
print("Total a pagar: R$ %.2f" % preço_pagar)