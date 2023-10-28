# Supongamos que estamos probando una prueba médica para una enfermedad
# P(D) es la probabilidad de tener la enfermedad antes de hacer la prueba
# P(Pos|D) es la probabilidad de dar positivo en la prueba si tienes la enfermedad
# P(Pos|¬D) es la probabilidad de dar positivo en la prueba si no tienes la enfermedad

# Datos de ejemplo
probabilidad_enfermedad = 0.01  # P(D)
probabilidad_positivo_dado_enfermedad = 0.95  # P(Pos|D)
probabilidad_positivo_dado_no_enfermedad = 0.10  # P(Pos|¬D)

# Aplicar la Regla de Bayes para calcular P(D|Pos)
# P(D|Pos) = (P(Pos|D) * P(D)) / (P(Pos|D) * P(D) + P(Pos|¬D) * P(¬D))
probabilidad_positivo = (probabilidad_positivo_dado_enfermedad * probabilidad_enfermedad) + (probabilidad_positivo_dado_no_enfermedad * (1 - probabilidad_enfermedad))
probabilidad_enfermedad_dado_positivo = (probabilidad_positivo_dado_enfermedad * probabilidad_enfermedad) / probabilidad_positivo

print("Probabilidad de tener la enfermedad dado un resultado positivo:", probabilidad_enfermedad_dado_positivo)
