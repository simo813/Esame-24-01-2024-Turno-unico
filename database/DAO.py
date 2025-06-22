from database.DB_connect import DBConnect
from model.method import Method


class DAO:

    @staticmethod
    def getMethods():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gm.Order_method_code as code , gm.Order_method_type as name 
                    from go_sales.go_methods gm 
                    order by gm.Order_method_type """

        cursor.execute(query)

        for row in cursor:
            result.append(Method(row['code'], row['name']))

        cursor.close()
        conn.close()
        return result