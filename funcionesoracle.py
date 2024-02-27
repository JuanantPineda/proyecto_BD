import sys
import oracledb

def conexionOracle():

    try:
        db = oracledb.connect("c##proyecto/usuario@localhost/xe")
        print("Se ha conectado correctamente a Oracle")
    except:
        print("No se ha podido realizar la conexión a la base de datos.")
        sys.exit(1)

    return db

def cerrarConexion(db):
    print("Se ha cerrado la conexion")
    db.close()


def menuCRUD():
    menu = '''Bien venido al menu CRUD
    1. Listar todo el contenido de la tabla material
    2. Mostrar los alumnos que tenga cierto nombre
    3. Mostrar los alumnos que hay en cierta aula
    4. Insertar datos en la tabla Material
    5. Elimina un matrial por su titulo
    6. Hacer un decuento de la tarifa a cierto niño
    7. Salir
    '''

    print(menu)

    while True:
        try:
            opcion = int(input("Elija un numero para probar la consulta: "))
            while opcion > 7:
                print("Tienes que elejir una opcion que este disponible")
                opcion = int(input("Elija un numero para probar la consulta: "))
            break
        except ValueError:
            print ("Debes introducir un número")

    return opcion

#Listar el titulo de todos los materiales de la tabla materiales

def listarMaterial(db):
    sql="select Titulo from material"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("El contenido de la tabla material son los siguientes:")
        print("Nombre Material:")
        for registro in registros:
            print("-",registro[0])
        print("Número de registros seleccionados:", cursor.rowcount)
    except:
        print("Error en la consulta")

#Listar el nombre de los alumnos que se pide por pantalla de la tabla alumnos
        
def listarNombre(db):

    cad= input("Introduzca el nombre del alumno: ")

    sql=(f"select Nombre,Apellidos,DNI from ninios where nombre = '{cad}'")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("El contenido de la tabla ninios son los siguientes:")
        print(("{:<30}{:<30}{:<30}".format("Nombre","Apellidos","DNI")))
        for registro in registros:
            print("{:<30}{:<30}{:<30}".format(registro[0],registro[1],registro[2]))
    except:
        print("Error en la consulta")

#Listar los alumnos que hay en cierta clase

def listarAlumnos(db):
    
    cad= input("Introduzca el identificador de la aula: ")

    sql=(f"select Nombre,Apellidos from ninios where Id_aula = '{cad}'")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        
        registros = cursor.fetchall()
        print("Los alumnos que pertenecen a la aula",cad ,"son los siguientes:")
        print(("{:<30}{:<30}".format("Nombre","Apellidos")))
        for registro in registros:
            print("{:<30}{:<30}".format(registro[0],registro[1]))
    except:
        print("Error en la consulta")

#Insertar datos en la tabla material

def insertarDatos(db):

    titulo = input("Ingrese el titulo del materia: ")
    formato = input("Ingrese el formato del material: ")

    estadoMaterial = input("Ingrese el estado funcional del material (usado o nuevo): ").lower()
    while estadoMaterial not in ['usado', 'nuevo']:
        print("Estado funcional del material no válido. Por favor, ingrese uno de los siguientes valores: usado o nuevo")
        estadoMaterial = input("Ingrese el estado funcional del material nuevamente: ").lower()

    estadoFuncional = input("Ingrese el estado del material (bueno, excelente, inutilizable, usado o regular): ").lower()
    while estadoFuncional not in ['bueno', 'excelente', 'inutilizable', 'usado', 'regular']:
        print("Estado del material no válido. Por favor, ingrese uno de los siguientes valores: bueno, excelente, inutilizable, usado o regular")
        estadoFuncional = input("Ingrese el estado del material nuevamente: ").lower()

    comentario= input("Ingrese un comentario del material: ")

    while True:
        try:
            numEjemplares = int(input("Ingrese el numero de ejemplares que tiene ese material: "))
            while numEjemplares <= 0:
                print("Tienes que poner un numero acorde")
                numEjemplares = int("Ingrese el numero de ejemplares que tiene ese material: ")
            break
        except ValueError:
            print ("Debes introducir un número")

    tipoMaterial = input("Ingrese el tipo de material que es: ")

    cursor = db.cursor()
    sql="insert into material values ('%s','%s','%s','%s','%s',%d,'%s')" % (titulo,formato,estadoMaterial,estadoFuncional,comentario,numEjemplares,tipoMaterial)
    try:
        print("Se han insertado correctamente los datos",sql)
        cursor.execute(sql)
        db.commit()
    except:
        print("No se ha ingresado ningun dato")
        db.rollback()

def eliminarMaterial(db):
    titulo = input("Ingrese el titulo a eliminar: ")

    cursor=db.cursor()
    sql=(f"delete from material where titulo = '{titulo}'")

    try:
        cursor.execute(sql)
        db.commit()
        if cursor.rowcount==0:
            print("No hay valores con ese dato")
        else:
            print("Se ha eliminado",titulo,"de la tabla material")
    except :
        print("No se ha eliminado ningun dato")
        db.rollback()

def actualizarTarifa(db):

    while True:
        try:
            descuento = int(input("Ingresa el descuento para la tarifa: "))
            while descuento <= 0 or descuento >= 100:
                print("Tienes que poner un numero acorde")
                descuento = int(input("Ingresa el descuento para la tarifa: "))
            break
        except ValueError:
            print ("Debes introducir un número")

    idNinino = input("Ingrese el identificador del niño: ")

    sql=(f"UPDATE ninios SET Tarifa = Tarifa * ((100-{descuento})*0.01) WHERE Id_ninio = '{idNinino}' ")
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print("Se ha actualizado correctamente los datos")
    except Exception as e:
        print("Error ", e)     

