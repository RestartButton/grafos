from Grafo import Grafo
from tabulate import tabulate #pip install tabulate


if __name__ == "__main__":

    arestas = [('A','C'),('A','B'),('B','C')]
    #arestas = [('A','C', 0),('A','B', 1),('B','C', 0)]
    gf = Grafo(arestas)
    print(gf)
    print(tabulate(gf.get_matrix(), headers=gf.get_vertices()))
    gf.remove_aresta('B', 'C')
    print(gf)
    gf.remove_vertice('A')
    print(gf)
    print(tabulate(gf.get_matrix(), headers=gf.get_vertices()))