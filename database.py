import re
import sqlite3 as sql
import os

def createDB():
    conn = sql.connect("CoDeck.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE buttons(
            button integer,
            path text
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(button, path):
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO buttons VALUES({button}, '{path}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM buttons"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def insertRows(buttonList):
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO buttons VALUES(?, ?)"
    cursor.executemany(instruccion, buttonList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM buttons ORDER BY {field}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def readRow(button):
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM buttons WHERE button='{button}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def getPath(button):
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM buttons WHERE button='{button}'"
    cursor.execute(instruccion)
    path = cursor.fetchall()
    conn.commit()
    conn.close()
    return (path[0][1])

def updateRow(button, path):
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE buttons SET path='{path}' WHERE button='{button}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteRow(button):
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM buttons WHERE button='{button}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteRows():
    conn = sql.connect("CoDeck.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM buttons"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow(0, "hola")
    #readRows()
    #buttonList = [(1, "Inserta una acción para el boton 1"), (2, "Inserta una acción para el boton 2"), (3, "Inserta una acción para el boton 3"), (4, "Inserta una acción para el boton 4"), (5, "Inserta una acción para el boton 5"), (6, "Inserta una acción para el boton 6"), (7, "Inserta una acción para el boton 7"), (8, "Inserta una acción para el boton 8"), (9, "Inserta una acción para el boton 9")]
    #insertRows(buttonList)
    #readOrdered("button")
    #deleteRows()
    readRows()


