import pymysql


class Sql:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='elperri2021',
                                          charset='utf8mb4',
                                          db='bebedores')

    def get(self, table):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM " + table
                )
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    def add(self, table, data):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO " + table + " VALUES (" + data + ")"
                )
                self.connection.commit()
        except Exception as e:
            print(e)
