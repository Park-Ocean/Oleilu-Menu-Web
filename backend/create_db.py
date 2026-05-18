import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    conn = psycopg2.connect("postgresql://postgres:Park123@127.0.0.1:5432/postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute('CREATE DATABASE "oleilu_bd"')
    print("Base de datos oleilu_bd creada.")
    cur.close()
    conn.close()
except psycopg2.errors.DuplicateDatabase:
    print("La base de datos oleilu_bd ya existe.")
except Exception as e:
    print(f"Error creando base de datos: {e}")
