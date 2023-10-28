import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución binomial
n = 10  # Número de ensayos
p = 0.3  # Probabilidad de éxito en cada ensayo

# Generar una muestra de la distribución binomial
muestra = np.random.binomial(n, p, size=1000)

# Visualizar la distribución de probabilidad
plt.hist(muestra, bins=11, density=True, color='b', alpha=0.7, rwidth=0.85)
plt.xlabel("Número de Éxitos")
plt.ylabel("Probabilidad")
plt.title("Distribución Binomial (n=10, p=0.3)")
plt.show()
