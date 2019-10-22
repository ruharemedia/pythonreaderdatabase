import time
import mysql.connector
from mysql.connector import Error
from win10toast import ToastNotifier

def main():
    readedVar = read()
    writedVar = write()
    if readedVar == writedVar:
        print("Все нормально!")
    else:
        toaster = ToastNotifier()
        toaster.show_toast("Обновление!", "В базе данных новая заявка! Следует проверить!", threaded=True,
                           icon_path=None, duration=7)
        while toaster.notification_active():
            time.sleep(0.1)
    
def read():
    f=open("col.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        return int(contents)
        
def write():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='database_name',
                                             user='user_name',
                                             password='password')

        sql_select_Query = "select * from zayavki"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        numbers = cursor.rowcount

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print(numbers)
            f = open("col.txt","w+")
            f.write(str(numbers))
            f.close()
            return int(numbers)

def starter():
    while 1 > 0:    
        main()
        time.sleep(60)   
        
starter()