import flet as ft
import networkx as nx
from model.product import Product


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

    def handle_graph(self, e):
        self.view.txt_result.clean()
        if self.view.ddMethodValue is not None and self.view.ddYearValue is not None and self.view._txtInS is not None:
            method = int(self.view.ddMethodValue)
            year = int(self.view.ddYearValue)
            s = float(self.view._txtInS.value)
            self.model.createGraph(method, year, s)
            graph = self.model.graph
            self.view.txt_result.controls.append(
                ft.Text(f"Grafo creato\n"
                        f"Ci sono {graph.number_of_nodes()} vertici\n"
                        f"Ci sono {graph.number_of_edges()} archi\n"))

        else:
            ft.Text(f"Inserisci i valori")
        self.view.update_page()


    def handle_topProducts(self, e):
        graph = self.model.graph
        listOfValidNodes = []
        for source in graph.nodes():
            count = 0
            if graph.out_degree(source) == 0:
                for successors in graph.in_edges(source):
                    count += 1
                listOfValidNodes.append((source, count, source.annualRevenue))
        listOfValidNodes.sort(key=lambda tup: tup[1], reverse=True)
        self.view.txt_result.controls.append(
            ft.Text(f"I prodotti più redditizi sono"))
        for i in range(0, 5):
            self.view.txt_result.controls.append(
                ft.Text(f"Prodotto {listOfValidNodes[i][0]}  Archi entranti {listOfValidNodes[i][1]} Ricavo {listOfValidNodes[i][2]}"))
        self.view.update_page()





