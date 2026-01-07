#verificacion de edad para descuento
edad = 67
compra = 80000
porcentaje = 0.20
descuento = compra * porcentaje

#verificar
if edad >= 65 and compra > 50000:
    print("Califica para descuento.")
    total = compra - descuento
else:
    print("No califica para descuento.")
    total = compra
    
#formato
total_formato = f"${total:,.0f}" .replace(",",".")
print ("precio final:", total_formato)