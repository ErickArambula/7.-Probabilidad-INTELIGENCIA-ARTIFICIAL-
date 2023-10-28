# Supongamos tres eventos A, B y C
# Queremos verificar si A y B son independientes dados C

# Probabilidad de A
probabilidad_A = 0.4

# Probabilidad de B
probabilidad_B = 0.3

# Probabilidad de C
probabilidad_C = 0.5

# Probabilidad conjunta de A y B
probabilidad_A_y_B = probabilidad_A * probabilidad_B

# Probabilidad condicional de A dado C
probabilidad_A_dado_C = probabilidad_A_y_B / probabilidad_C

# Probabilidad condicional de B dado C
probabilidad_B_dado_C = probabilidad_A_y_B / probabilidad_C

# Comprobación de independencia condicional
independencia_condicional = probabilidad_A_y_B == probabilidad_A_dado_C * probabilidad_C and probabilidad_A_y_B == probabilidad_B_dado_C * probabilidad_C

if independencia_condicional:
    print("A y B son independientes dado C.")
else:
    print("A y B no son independientes dado C.")
