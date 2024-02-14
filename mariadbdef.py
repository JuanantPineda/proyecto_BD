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

