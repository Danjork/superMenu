altura = float(input("Ingresa tu altura"))
peso = int(input("Ingresa tu peso"))
imc = peso / altura**2
imc_redondeo = int(imc)

print(f"Tu IMC es: {imc_redondeo}")
if imc <= 20:
    print("SIn obesidad")
elif imc_redondeo >= 25:
    print("Obesidad")
else:
    print("obeso")
