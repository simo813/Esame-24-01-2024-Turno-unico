from database.DB_connect import DBConnect
from model.method import Method
from model.product import Product


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

    @staticmethod
    def getNodes(methodId, year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct (gds.Product_number) as id, sum(gds.Quantity*gds.Unit_sale_price) as revenue
                    from go_sales.go_daily_sales gds 
                    where gds.Order_method_code = %s and year(gds.`Date`) = %s 
                    group by gds.Product_number """

        cursor.execute(query, (methodId, year))

        for row in cursor:
            result.append(Product(row['id'], row['revenue']))

        cursor.close()
        conn.close()
        return result