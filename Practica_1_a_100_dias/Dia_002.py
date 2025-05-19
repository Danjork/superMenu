print("Calculadora de propinas")
monto_total = float(input("Monto total a pagar\n"))
cantidad_personas = int(input("Cantidad de personas a pagar\n"))
porcentaje_propina = float(input("desea agregar propina del 10,12,15 %\n"))

monto_sin_propina = monto_total / cantidad_personas
monto_con_porcentaje = monto_sin_propina * (porcentaje_propina/100)
monto_con_propina = (monto_sin_propina + monto_con_porcentaje)



print(monto_sin_propina)
print(monto_con_porcentaje)
print(monto_con_propina)
print(f"El monto a pagar por persona es: {monto_con_propina} ")
print("Cantidad de ")


#Segundo ejercicio
dividir_dos_digitos = input("Agregar un numero con 2 digitos")

primer_digito = dividir_dos_digitos[0]
segundo_digito = dividir_dos_digitos[1]

resultado = int(primer_digito) + int(segundo_digito)
print(primer_digito)
print(segundo_digito)
print(resultado)
