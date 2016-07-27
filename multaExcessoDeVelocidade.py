velocidade  = int(input("Digite a velocidade: "))
if velocidade > 110:
    print ("Você utrapassou o limite de velocidade em %d Km/h, e deverá pagar R$ %.2f de multa "%((velocidade - 110),((velocidade - 110)*5)))
else:
    print("Você está dentro do limite de velocidade")
