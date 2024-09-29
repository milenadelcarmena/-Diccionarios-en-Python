# Crear un diccionario llamado informacion_personal con datos ficticios
informacion_personal = {
    "nombre": "Roberto Riofrio",
    "edad": 38,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Loja"
print(f"Nueva ciudad: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para la "profesion" (aunque ya existe, la modificaremos)
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar existencia de la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0988874704"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)