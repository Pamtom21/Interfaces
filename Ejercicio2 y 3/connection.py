import sqlite3 #importamos sqlite3

try: #intentamos una conexion, si no hay la crea
    connection = sqlite3.connect("database/contaminacion.db")
    cursor = connection.cursor() #crea un cursor que nos permite interactuar con la bd
    #ejecuta un llamado a la bd, verifica si existe una tabla, si no la crea
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS T_Conta(       
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data BLOB
        )
    """)
    #blob (binary large object), almacena grandes cantidades de datos binarios, como imagenes
    connection.commit()#guarda los cambios en la bd
    connection.close() # cierra el archivo

except Exception as ex:
    print(ex)