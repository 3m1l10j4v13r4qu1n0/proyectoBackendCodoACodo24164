import mysql.connector
from mysql.connector import Error
error = Error

config_dev = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'jacarandaclienteuser'
}

config_prod = {} # proximamente, despliegue

conexion = mysql.connector.connect(**config_dev)