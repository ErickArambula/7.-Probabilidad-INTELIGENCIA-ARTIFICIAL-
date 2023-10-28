import random

# Simular un lanzamiento de moneda con incertidumbre
def lanzar_moneda_con_incertidumbre():
    probabilidad_de_cara = random.uniform(0, 1)  # Generar una probabilidad entre 0 y 1
    if probabilidad_de_cara < 0.5:
        return "Sello"  # Si la probabilidad es baja, se asume sello
    else:
        return "Cara"  # Si la probabilidad es alta, se asume cara

# Realizar múltiples lanzamientos de moneda con incertidumbre
num_lanzamientos = 10
resultados = [lanzar_moneda_con_incertidumbre() for _ in range(num_lanzamientos)]

print("Resultados de los lanzamientos con incertidumbre:")
print(resultados)
