from collections import defaultdict

class Grafo(object):

    def __init__(self, arestas, direcionado=False, ponderado=False):
        self.vert = list()
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.ponderado = ponderado
        self.adiciona_arestas(arestas)


    def get_vertices(self):
        return self.vert


    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def get_vert(self, index):
        return self.vert[index]


    def adiciona_vertice(self, vertices):
        for k in vertices:
            if k not in self.vert:
                self.vert.append(k)


    def adiciona_arestas(self, arestas):
        if not self.ponderado:
            for u, v in arestas:
                self.adiciona_aresta(u, v)
        else:
            for u, v, p in arestas:
                self.adiciona_aresta(u, v, p)


    def adiciona_aresta(self, u, v, peso=0):
        if not self.ponderado:
            self.adj[u].add(v)
        else:
            self.adj[u].add((v, peso))
        # Se o grafo é não-direcionado, adiciona aresta nos dois sentidos.
        if not self.direcionado:
            if not self.ponderado:
                self.adj[v].add(u)
            else:
                self.adj[v].add((u, peso))
        self.adiciona_vertice([u,v])


    def existe_aresta(self, u, v):
        if not self.ponderado:
            return u in self.adj and v in self.adj[u]
        else:
            return self.peso_aresta(u, v) > -1
                
    

    def peso_aresta(self, u, v):
        if not self.ponderado:
            return 0
        else:
            for k, j in self.adj[u]:
                if k == v:
                    return j
        return -1
    

    def remove_aresta(self, u, v):
        if not self.ponderado:
            if self.existe_aresta(u, v):
                self.adj[u].remove(v)
                if not self.direcionado:
                    self.adj[v].remove(u)
        else:
            peso = self.peso_aresta(u, v)
            if peso > -1:
                self.adj[u].remove((v, peso))
                if not self.direcionado:
                    self.adj[v].remove((u, peso))
        self.limpa_adj()
    

    def remove_vertice(self, v):
        if not self.ponderado:
            for u in self.adj:
                if self.existe_aresta(u, v):
                    self.adj[u].remove(v)
        else:
            for u in self.adj:
                peso = self.peso_aresta(u, v)
                if peso > -1:
                    self.adj[u].remove((v, peso))

        self.adj[v].clear()
        self.adj.pop(v)
        self.limpa_adj()

    def limpa_adj(self):
        k = []
        for u in self.adj:
            if self.adj[u] == set():
                k.append(u)
        for u in k:
            self.adj.pop(u)

    def get_matrix(self):
        matrix = []

        #matrix.append(self.vert)
        for u in self.vert:
            linha = [u]
            for v in self.vert:
                if self.existe_aresta(u, v):
                    linha.append(1)
                else:
                    linha.append(0)
            matrix.append(linha)

        self.limpa_adj()
        return matrix


    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({},{})'.format(self.__class__.__name__, self.vert, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]