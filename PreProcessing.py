import sqlite3
import csv
import os
import SqlSide


def connect_db():
    return sqlite3.connect('weather.db')


def pre_processing(directory_name):
    connection = connect_db()
    create_db(connection)
    insert_csv_into_db(directory_name, connection)
    connection.close()


def create_db(conn):
    cur = conn.cursor()

    sql = SqlSide.create_table()

    cur.execute(sql)
    print("db has been created")
    conn.commit()



def insert_csv_into_db(directory_name,connection):
    cursor = connection.cursor()
    files = os.listdir(directory_name)
    for fileName in files:
        if fileName.endswith(".csv"):
            try:
                with open(os.path.join(directory_name, fileName)) as file:
                    rows = csv.reader(file)
                    next(rows)
                    cursor.executemany(SqlSide.insert_to_db(), rows)
                    connection.commit()
                    print("{} has been committed".format(fileName))
            except IOError:
                print(f"can not read csv file: {fileName} and insert to db")


if __name__ == "__main__":
    pre_processing('C:/projects/climacell_final')
