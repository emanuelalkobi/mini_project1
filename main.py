import sys
import get_images as get_images
import create_video as create_video
import analyze_video as analyze_video
import mysql_func as mysql_func

import mysql.connector
from statistics import mode

def main():
    #set mysql db
   
    while(1):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="qwerasdf",auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS  mini_project3_db")
        mycursor.execute("use mini_project3_db")
        mycursor.execute("CREATE TABLE  IF NOT EXISTS user_data (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255), img_num VARCHAR(255),description VARCHAR(255),description_num VARCHAR(255))")
        mycursor.execute("use mini_project3_db")
        print("------------------------------------------------")
        print("Menu:\n1.Query new user name\n2.Query exsist user name\n3.See full database \n4.Delete DataBase\n5.Search for a word\n6.Exit")
        data = input("Enter a number: ")
        data=int(data)
        print(data)
        if (data==1):
            mysql_func.add_user(mycursor)
        elif(data==2):
            mysql_func.query_user(mycursor)
        elif(data==3):
            mysql_func.print_db(mycursor)
        elif(data==4):
            mysql_func.delete_db()
        elif(data==5):
            mysql_func.search_word(mycursor)
    

        elif(data==6):
            return







main()
