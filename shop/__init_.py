import mysql.connector
class Managerdb:
    def __init__(self,host,user,password, database):
        self.mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
        )
        self.mycursor = self.mydb.cursor()

#--------------------------------------------------------------------------------------------------------------------#
    def selectdb(self, table):
        sql = f"SELECT * FROM {table}"
        self.mycursor.execute(sql)
        show = self.mycursor.fetchall()
        return show

#--------------------------------------------------------------------------------------------------------------------#

    def deletedb(self,table,id_name,id):
        sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
        self.mycursor.execute(sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0 :
            return True
        else:
            return False

#--------------------------------------------------------------------------------------------------------------------#
    def editdb(self,table,colum,product_id,val ,id):
        sql = f"UPDATE {table} SET {colum} = %s WHERE {product_id} = %s"
        val_sql = (val,id)
        self.mycursor.execute(sql,val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0 :
            return True
        else:
            return False

#--------------------------------------------------------------------------------------------------------------------#
    def insert_categories(self, name):  # เปลี่ยนชื่อเป็น categories
        sql = "INSERT INTO categories (category_id,category_name) VALUES (%s, %s)"
        val_sql = (None, name)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False 
        
    def insert_user(self, name,password,email,role):
        sql = "INSERT INTO user VALUES (%s,%s,%s,%s,%s)"
        val_sql = (None, name,password,email,role)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
    def insert_orders(self, date,amount,status):
        sql = "INSERT INTO orders VALUES (%s, %s,%s,%s)"
        val_sql = (None,date,amount,status)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
    def insert_product(self, name,des,price,stock):
        sql = "INSERT INTO product VALUES (%s, %s, %s, %s, %s)"
        val_sql = (None, name,des,price,stock)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
#--------------------------------------------------------------------------------------------------------------------#
result_select = Managerdb('localhost','root','1234','shop')
#เรียกใช้
#print(result_select.selectdb('products'))

#ลบ
#print(result_select.deletedb('products', 'product_id', 113))

#แก้ไข
#print(result_select.editdb('categories', 'category_name', 'category_id','รองเท้าไนกี้' ,2223))

#เพิ่มข้อมูล
#print(result_select.insert_categories('รองเท้า'))