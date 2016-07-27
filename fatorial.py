n = int(input("Digite um numero: "))
fat = 1
i = 1
while i <= n:
    fat = fat * i
    i = i + 1
print("%d! = %d"%(n,fat))
