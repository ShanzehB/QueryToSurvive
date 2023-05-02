import mysql.connector
import streamlit

connection = mysql.connector.connect(host="localhost",
user="root",
password="cpsc408!",
auth_plugin='mysql_native_password',
database = 'Formula1')

dialect = "mysql"
host = "localhost"
port = 3306
database = "Formula1"
username = "root"
password = "cpsc408!"