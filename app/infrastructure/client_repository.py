from .sql.client_sql import clientSql

"""Service methods for file endpoints"""


class clientRepository:
    def __init__(self, db):
        print("client_repository.init")
        self.mydb = db
        super().__init__()

    def get_client(self, id):
        print("client_repository.get_client")
        cursor = self.mydb.cursor()
        cursor.execute(clientSql.GET.format(id))
        result = cursor.fetchall()
        return result

    def create_client(self, client):
        print("client_repository.create_client")
        cursor = self.mydb.cursor()

        isAdult = 1 if client.isAdult else 0
        sql = clientSql.INSERT.format(
            client.CIF, client.Name, client.LastName, client.Link, client.age, isAdult
        )
        cursor.execute(sql)
        return self.get_client(client.CIF)
