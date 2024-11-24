from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

# Función para guardar los datos en la base de datos
def SaveToBD(data):
    try:
        # Conectarse a la base de datos SQLite
        connection = sqlite3.connect("database/contaminacion.db")
        cursor = connection.cursor()

        # Insertar el JSON como texto en la base de datos
        cursor.execute("""
            INSERT INTO T_Conta(Data) 
            VALUES (?)
        """, (data,))

        # Guardar los cambios y cerrar la conexión
        connection.commit()
        connection.close()

    except sqlite3.Error as e:
        print(f"Error al insertar en la base de datos: {e}")
        raise

# Función para obtener los datos de la base de datos
def GetToDb():
    try:
        # Conectarse a la base de datos SQLite
        connection = sqlite3.connect("database/contaminacion.db")
        cursor = connection.cursor()

        # Realizar la consulta SELECT
        cursor.execute("SELECT Data FROM T_Conta")

        # Obtener todos los resultados
        rows = cursor.fetchall()

        # Cerrar la conexión
        connection.close()

        # Devolver los datos recuperados
        return rows

    except sqlite3.Error as e:
        print(f"Error al obtener de la base de datos: {e}")
        raise

# Ruta para subir datos en formato JSON
@app.route('/upload_json', methods=['POST'])
def Insert():
    try:
        # Verifica que el Content-Type de la solicitud sea JSON
        if request.content_type != 'application/json':
            return "Content-Type debe ser application/json", 400

        # Obtener los datos JSON del cuerpo de la solicitud
        data = request.get_data()

        # Convertir los datos de bytes a un objeto Python
        try:
            data_dict = json.loads(data)  # Convertir el JSON a un diccionario
        except json.JSONDecodeError:
            return "JSON mal formado", 400

        # Guardar el JSON en la base de datos
        SaveToBD(json.dumps(data_dict))  # Guardamos como texto JSON

        return "Data subida exitosamente", 200

    except Exception as e:
        print(f"Error en el servidor: {e}")
        return f"Error interno: {str(e)}", 500

# Ruta para obtener los datos JSON desde la base de datos
@app.route('/get_json', methods=['POST'])
def get():
    try:
        # Obtener los datos desde la base de datos
        rows = GetToDb()

        # Si no hay datos, devuelve un mensaje de error
        if not rows:
            return jsonify({"message": "No hay datos disponibles"}), 404

        # Convertir los resultados de las filas en un formato adecuado
        # En este caso, estamos asumiendo que 'Data' está en formato JSON
        data = [json.loads(row[0]) for row in rows]

        # Retornar los datos como respuesta JSON
        return jsonify(data), 200

    except Exception as e:
        print(f"Error al obtener los datos: {e}")
        return jsonify({"message": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)

