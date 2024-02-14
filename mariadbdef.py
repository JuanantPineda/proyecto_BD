import sys
import MySQLdb

def conexionMariaDB():
    try:
        db = MySQLdb.connect("localhost","pineda","pineda","proyecto" )
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)
    print("Conexión correcta.")
    
    return db

def cerrarConexion(db):
    print("Se ha cerrado la conexion")
    db.close()

def listarMaterial(db):
    
    sql="select * from material"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("El contenido de la tabla material son los siguientes:")
        for registro in registros:
            print(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6])
    except:
        print("Error en la consulta")

def listarNombre(db):

    cad= input("Introduzca el nombre del alumno: ")

    sql=(f"select * from ninios where nombre = '{cad}'")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("El contenido de la tabla ninios son los siguientes:")
        for registro in registros:
            print(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8],registro[9],registro[10])
    except:
        print("Error en la consulta")