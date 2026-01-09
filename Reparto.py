#Reparto de herencia
herencia = 120000000
hermano1 = 0.50
hermano2 = 0.30
hermano3 = 0.20

#division
valor1 = herencia * hermano1
print("El hermano mayor recibe: ", valor1)

Valor2 = herencia * hermano2
print("El hermano del medio recibe: ", Valor2)

valor3 = herencia * hermano3
print("El hermano menor recibe: ", valor3)

#formatear
herencia1 = f"${valor1:,.0f}" .replace(",",".")
herencia2 = f"${Valor2:,.0f}" .replace(",",".")
herencia3 =f"${valor3:,.0f}" .replace(",",".")

print("Al hermano mayor le corresponde: ", herencia1)
print("Al hermano del medio le corresponde: ", herencia2)
print("Al hermano menor le corresponde: ", herencia3)

#suma de herencia
Total = valor1 + Valor2 + valor3
total_formato = f"${Total:,.0f}" .replace(",",".")
print ("El la suma total del valor repartido entre hermanos fue: ",total_formato)
