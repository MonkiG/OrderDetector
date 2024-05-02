import os
import json


def get_json(filename):
    json_file_path = os.path.join("db", filename)

    if os.path.exists(json_file_path):
        # Leer el contenido del archivo JSON
        with open(json_file_path, "r") as file:
            # Cargar el contenido del archivo JSON en un diccionario Python
            data = json.load(file)
        print("Archivo JSON cargado exitosamente.")
        return data
    else:
        print(f"No se encontró el archivo JSON en la ruta '{json_file_path}'.")


def save_json_local(data, filename):
    json_object = json.dumps(data, indent=4)

    file_path = os.path.join("db", filename)

    with open(file_path, "w") as outfile:
        outfile.write(json_object)
