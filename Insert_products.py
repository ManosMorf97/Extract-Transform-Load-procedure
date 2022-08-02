import mysql.connector
import mysql.connector.errorcode
from urllib3 import add_stderr_logger
import secretP
from secretP import *

def Begin():
    try:
        db=mysql.connector.connect(user='newuser',database='Manos',
        password=mysql_pwd,host="localhost")
    except mysql.connector.Error as err:
        print(err)
        return
    prepare_mysql_data(db)

def prepare_mysql_data(db):
    try:
        cursor=db.cursor()
        #cursor.execute('SET GLOBAL connect_timeout=28800')
        #cursor.execute('SET GLOBAL interactive_timeout=28800')
        #cursor.execute('SET GLOBAL wait_timeout=28800')
        sql_statement=("CREATE TABLE IF NOT EXISTS devices ("
            "deviceID varchar(30) not null,"
            "type_device varchar(20) not null,"
            "brand_company varchar(20) not null,"
            "primary key(deviceID)"
            ")ENGINE=InnoDB")
        cursor.execute(sql_statement)
        db.commit()
        types=['mobile_phone','television','microwave','dishwaser','clock',
            'electric_grill','oven','laptop','camera','webcam']
        brand='samsung'
        for type in types:
            for i in range(1,20+1):
                values=(type+'_C'+str(i),type,brand)
                sql_statement="Insert into devices values(%s,%s,%s)"
                cursor.execute(sql_statement,values)
                db.commit() 
        print("Done")
    except mysql.connector.Error as err:
        print(err)
    cursor.close()
    db.close()
    return

Begin()
