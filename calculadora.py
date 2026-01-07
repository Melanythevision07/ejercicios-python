#CALCULADORA DE PROPINA

#variables para encontrar el valor
cuenta = 45000
propina = 0.15

#calcular propina
valor_propina = cuenta * propina

#calcular valor de la cuenta
total_a_pagar = cuenta + valor_propina

#FORMATEAR ESTILO
propina_formato = f"{valor_propina:,.0f}" .replace(",",".")
total_formato = f"{total_a_pagar:,.0f}" .replace(",",".")

#MOSTRAR RESULTADOS
print("Valor de la propina: $ ", propina_formato)
print("Total a pagar $:", total_formato)