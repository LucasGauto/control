import sqlite3
conexion=sqlite3.connect('inventario.db')
cursor = conexion.cursor()
cursor.execute("CREATE TABLE productos("+
    "productoID INTEGER PRIMARY KEY AUTOINCREMENT,"
    "nombre VARCHAR(50),"
    "descripcion VARCHAR(255),"
    "precio INTEGER,"\
    "existencia INTEGER"
    ")")
cursor.execute("CREATE TABLE proveedores("+
    "proveedorID INTEGER PRIMARY KEY AUTOINCREMENT,"
    "productoID INTEGER,"
    "nombre VARCHAR(50),"
    "direccion VARCHAR(50),"
    "telefono INTEGER,"
    "FOREIGN KEY (productoID) REFERENCES productos(productoID)"
    ")")
cursor.close()