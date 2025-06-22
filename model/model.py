from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
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


    def getMaxPath(self):
        self.maxPath = []
        self.maxPathWeight = 0
        graph = self.graph

        for node in graph.nodes:
            self.recursion(
                source=node,
                partial=[node],
                partialWeight=0,
                weightPrec = None
            )
            print("\nENTRATO\n")
        print(self.maxPath)
        print(self.maxPathWeight)
        print("\nFINE\n")

        return self.maxPath, self.maxPathWeight

    def recursion(self, source, partial, partialWeight, weightPrec):
        graph = self.graph

        if len(partial) > len(self.maxPath):
            print("\n---------------------------------")
            print(len(partial))
            print(partialWeight)
            self.maxPathWeight = partialWeight
            self.maxPath = copy.deepcopy(partial)  # copia della lista
        elif len(partial) == len(self.maxPath):
            if partialWeight < self.maxPathWeight:
                print("\n---------------------------------")
                print(len(partial))
                print(partialWeight)
                self.maxPathWeight = partialWeight
                self.maxPath = copy.deepcopy(partial)

        for source, successor, data in graph.out_edges(source, data=True):
            if successor not in partial:
                print("successore non in parziale")
                if successor.Essential != source.Essential:
                    print("successore ha valore di essential diverso da source")
                    weight = graph.get_edge_data(source, successor).get('weight', 0)
                    print("weight: ", weight)
                    if weightPrec is None:
                        partial.append(successor)
                        self.recursion(successor, partial, partialWeight + weight, weight)
                        print("NUOVA RICORSIONE\n")
                        partial.pop()

                    else:
                        if weight >= weightPrec:
                            partial.append(successor)
                            self.recursion(successor, partial, partialWeight + weight, weight)
                            print("NUOVA RICORSIONE\n")
                            partial.pop()





