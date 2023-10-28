# Probabilidad a priori de un evento (probabilidad antes de la evidencia)
probabilidad_apriori = 0.3

# Supongamos que tenemos evidencia que cambia la probabilidad
evidencia = "Positiva"

# Probabilidad a posteriori de un evento (probabilidad después de la evidencia)
if evidencia == "Positiva":
    probabilidad_aposteriori = (probabilidad_apriori * 0.9) / ((probabilidad_apriori * 0.9) + ((1 - probabilidad_apriori) * 0.2))
else:
    probabilidad_aposteriori = (probabilidad_apriori * 0.1) / ((probabilidad_apriori * 0.1) + ((1 - probabilidad_apriori) * 0.8))

print("Probabilidad a priori:", probabilidad_apriori)
print("Probabilidad a posteriori:", probabilidad_aposteriori)
