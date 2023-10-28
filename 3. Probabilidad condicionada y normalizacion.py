# Supongamos que tenemos tres cajas con bolas de colores
caja_1 = {'roja': 3, 'verde': 2, 'azul': 1}
caja_2 = {'roja': 1, 'verde': 2, 'azul': 3}
caja_3 = {'roja': 2, 'verde': 1, 'azul': 2}

# Probabilidad de elegir una caja al azar
probabilidad_caja_1 = 1/3
probabilidad_caja_2 = 1/3
probabilidad_caja_3 = 1/3

# Probabilidad de elegir una bola roja condicionada a la elección de una caja
def probabilidad_bola_roja_en_caja(condicion):
    if condicion == 1:
        probabilidad = caja_1['roja'] / sum(caja_1.values())
    elif condicion == 2:
        probabilidad = caja_2['roja'] / sum(caja_2.values())
    elif condicion == 3:
        probabilidad = caja_3['roja'] / sum(caja_3.values())
    return probabilidad

# Probabilidad de elegir una caja y luego una bola roja
def probabilidad_caja_y_bola(condicion):
    probabilidad = probabilidad_caja_1 * probabilidad_bola_roja_en_caja(condicion)
    probabilidad += probabilidad_caja_2 * probabilidad_bola_roja_en_caja(condicion)
    probabilidad += probabilidad_caja_3 * probabilidad_bola_roja_en_caja(condicion)
    return probabilidad

# Normalización: Probabilidad de elegir una caja dada la elección de una bola roja
def probabilidad_caja_dada_bola(condicion):
    probabilidad = probabilidad_caja_1 * probabilidad_bola_roja_en_caja(condicion)
    probabilidad += probabilidad_caja_2 * probabilidad_bola_roja_en_caja(condicion)
    probabilidad += probabilidad_caja_3 * probabilidad_bola_roja_en_caja(condicion)
    return probabilidad / probabilidad_caja_y_bola(condicion)

# Calcular la probabilidad condicionada
eleccion_caja = 1  # Elegimos la caja 1
eleccion_bola_roja = probabilidad_caja_dada_bola(eleccion_caja)

print("Probabilidad de elegir una caja y luego una bola roja:", probabilidad_caja_y_bola(eleccion_caja))
print("Probabilidad de elegir la caja 1 dado que se eligió una bola roja:", eleccion_bola_roja)
