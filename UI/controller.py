import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model

    def fillDD(self):
        listMethods = self.model.passMethods()
        for method in listMethods:
            self.view.ddMethod.options.append(ft.dropdown.Option(key=method.code, text=method.name))
        self.view.ddYear.options.append(ft.dropdown.Option(key="2015", text="2015"))
        self.view.ddYear.options.append(ft.dropdown.Option(key="2016", text="2016"))
        self.view.ddYear.options.append(ft.dropdown.Option(key="2017", text="2017"))
        self.view.ddYear.options.append(ft.dropdown.Option(key="2018", text="2018"))
        self.view.update_page()



