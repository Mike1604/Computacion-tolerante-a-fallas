import pickle

# Crear un objeto para guardar
data = {
    "var1": "valor1",
    "var2": [1, 2, 3, 4],
    "var3": {"clave1": "valor1", "clave2": "valor2"}
}

# Guardar el objeto en un archivo
with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

# Restaurar el objeto desde el archivo
with open("data.pickle", "rb") as f:
    restored_data = pickle.load(f)

# Mostrar el objeto restaurado
print(restored_data)
"""
El código crea un objeto data, lo guarda en un archivo usando la función pickle.dump, 
y luego lo restaura usando la función pickle.load. Finalmente, se muestra el objeto 
restaurado.
"""