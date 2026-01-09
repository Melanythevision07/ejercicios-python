#Datos que se tienen
calificacion = 4.2
reseñas = 156

#Verificar categoria
if calificacion >= 4.0 and reseñas >= 100:
    print("Muy recomendado.")
elif 3.0 <= calificacion <= 3.9:
    print("Recomendado.")
else: 
    print("Necesita mejorar.")
