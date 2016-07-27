minuts = int(input("Minutos gastos: "))
if minuts < 200:
    fatura = 0.2
elif minuts <= 400:
    fatura = 0.18
elif minuts <= 800:
    fatura = 0.15
else:
    fatura = 0.08
print("Você usou %d min. Sua fatura é no valor de %.2f"%(minuts,( minuts * fatura)))
