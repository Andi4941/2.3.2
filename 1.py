# Paso 1: Solicitar datos de entrada
edad = int(input("Ingrese su edad: "))

# Paso 2: Procesar la información
if edad >= 0 and edad < 18:
    descuento = 50
    mensaje = "tiene descuento de un 50%"
elif edad >= 18 and edad < 30:
    descuento = 20
    mensaje = "tiene descuento de un 20%"
elif edad >= 60:
    descuento = 90
    mensaje = "tiene descuento de un 90%"
else:
    descuento = 0
    mensaje = "no aplica descuento"

# Paso 3: Mostrar datos de salida
print(f"Edad: {edad}, {mensaje}")