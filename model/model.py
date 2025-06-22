import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.optPath = None
        self.DAO = DAO()
        self.graph = None

    def passMethods(self):
        listMethods = self.DAO.getMethods()
        return listMethods

    def createGraph(self, methodId, year, s):
        listNodes = self.DAO.getNodes(methodId, year)
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(listNodes)
        for node1 in listNodes:
            for node2 in listNodes:
                if node1 != node2 and float(node2.annualRevenue) > (float(node1.annualRevenue) * float((1+s))):
                    self.graph.add_edge(node1, node2)


    def getOptPath(self):
        self.optPath = []
        graph = self.graph

        for node in graph.nodes:
            print("Il nodo esaminato non ha archi entranti\n")
            if graph.in_degree(node) == 0:
                self.recursion(
                    source=node,
                    partial=[node],
            )
            print("\nENTRATO\n")
        print(self.optPath)
        print("\nFINE\n")

        return self.optPath

    def recursion(self, source, partial):
        graph = self.graph

        if graph.out_degree(source) == 0:
            print("Il nodo esaminato non ha archi uscenti\n")
            if len(partial) > len(self.optPath):
                print("\n---------------------------------")
                print(f"La lunghezza massima ora è {len(partial)}")
                self.optPath = copy.deepcopy(partial)  # copia della lista

        for source, successor in graph.out_edges(source):
            if successor not in partial:
                print("successore non in parziale")
                partial.append(successor)
                self.recursion(successor, partial)
                print("NUOVA RICORSIONE\n")
                partial.pop()






