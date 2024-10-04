import pymysql

conexion = pymysql.connect(
    host="localhost",
    user="root",
    passwd="3138340058",
    database="restaurant",
)
cursor = conexion.cursor()
cursor.execute("select * from categoria")
for i,m in cursor.fetchall():
    print(i, " + ",m)
conexion.close()
