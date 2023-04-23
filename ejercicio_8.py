contraseña = "contraseña"

entrada = input("Ingrese la contraseña: ")

if entrada.lower() == contraseña.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")