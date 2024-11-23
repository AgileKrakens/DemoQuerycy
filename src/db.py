import os
import pymysql

def get_db_connection():
    connection = pymysql.connect(
        host=os.environ.get('DATABASE_HOST', 'localhost'), 
        user=os.environ.get('DATABASE_USER', 'admin'),
        password=os.environ.get('DATABASE_PASSWORD', 'qwerty'),
        database=os.environ.get('DATABASE_NAME', 'db'),
        port=int(os.environ.get('DATABASE_PORT', 3306)),
    )
    return connection
