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
                sql = "SELECT * FROM " + table
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    def set(self, table, data):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO " + table + " VALUES (" + data + ")"
                cursor.execute(sql)
                self.connection.commit()
        except Exception as e:
            print(e)
