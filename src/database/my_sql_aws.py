import pymysql


class MySqlAws:
    def __init__(self, host: str, username: str, password: str, ):
        self.host = host
        self.username = username
        self.password = password
        self.mysql_connection = pymysql.connect(host=host, user=username, password=password)
        self.cursor = self.mysql_connection.cursor()

    def create_db(self, db_name: str):
        sql = f'''CREATE DATABASE {db_name}'''
        self.cursor.execute(sql)


if __name__ == '__main__':
    my_sql = MySqlAws('url-classifications.c9zrddv82ve8.us-east-1.rds.amazonaws.com', 'orelg', 'Ostg1601')
    my_sql.create_db('urls')
