class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []

        i, e = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1 and i < len(self.graph):
            src, dest, weight = self.graph[i]
            i += 1

            x = self.find(parent, src)
            y = self.find(parent, dest)

            if x != y:
                result.append([src, dest, weight])
                e += 1
                self.union(parent, rank, x, y)

        print("Following are the edges in the constructed MST")
        for src, dest, weight in result:
            print(f"{src} -- {dest} == {weight}")


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()
