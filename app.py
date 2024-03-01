# Definir variables
fruta = "Manzana"
color = "Rojo"
calorias = 20

# Operaciones matemáticas
triplo = calorias * 3
cuarto = color / 4
logaritmo = math.log(calorias)
exponencial = math.exp(color)

# Estructuras condicionales para verificar el color
if color == "Rojo":
    print("Es una fruta roja")
else:
    print("Es una fruta de otro color")

# Bucle para imprimir las sílabas de la fruta
for i in range(0, len(fruta), 2):
    print(fruta[i : i + 2])
# Imprimir datos en consola
print("Fruta:", fruta)
print("Color:", color)
print("Calorías:", calorias)
print("Triplo:", triplo)
print("Cuarto:", cuarto)
print("Logaritmo:", logaritmo)
print("Exponencial:", exponencial)
