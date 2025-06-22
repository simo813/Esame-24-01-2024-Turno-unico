from database.DAO import DAO


class Model:
    def __init__(self):
        self.DAO = DAO()

    def passMethods(self):
        listMethods = self.DAO.getMethods()
        return listMethods