import database
mycursor = database.mydb.cursor()
#-------------------------------------#
def selectdb(table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    show = mycursor.execute(sql)
    return show
#print(selectdb('"products"'))
#-------------------------------------#

def deletedb(table,id_name,id):
    sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
    mycursor.execute(sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print(deletedb("products","product_id",3))
#-------------------------------------#
def editdb(table,colum,product_id,val ,id):
    sql = f"UPDATE {table} SET {colum} = %s WHERE {product_id} = %s"
    val_sql = (val,id)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print(editdb("products","stock","product_id",110,112))
#-------------------------------------#
def insert_product(name,des,price,stock):
        sql = "INSERT INTO product VALUES (%s, %s, %s, %s, %s)"
        val_sql = (None, name,des,price,stock)
        mycursor.execute(sql,val_sql)
        database.mydb.commit()
        if mycursor.rowcount > 0 :
            return True
        else:
            return False
        