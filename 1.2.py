# Paso 1: Solicitar datos de entrada
user = input("Ingrese su usuario: ")
pwd = input("Ingrese su contraseña: ")

# Paso 2: Procesar la información y validar el acceso
if user == "duoc" and pwd == "123duoc":
    # Paso 3: Mostrar mensaje de bienvenida
    print("Bienvenido")
else:
    # Paso 3: Mostrar mensaje de error en la contraseña
    print("Error en contraseña")