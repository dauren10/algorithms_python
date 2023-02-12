'''
Алгоритм Беллмана-Форда используется для поиска кратчайшего пути от исходной вершины до каждой вершины взвешенного графа. 
В отличие от алгоритма Дейкстры, алгоритм Беллмана Форда также может найти кратчайшее расстояние до каждой вершины взвешенного графа даже 
с отрицательными ребрами. 
Единственное различие между алгоритмом Дейкстры и алгоритмом Беллмана Форда состоит в том, что алгоритм Дейкстры просто посещает соседнюю вершину 
на каждой итерации, а алгоритм Беллмана Форда посещает каждую вершину через каждое ребро на каждой итерации.

Помимо алгоритма Беллмана-Форда и алгоритма Дейкстры, алгоритм Флойда-Уоршелла также является алгоритмом кратчайшего пути.
 Но алгоритм Беллмана-Форда используется для вычисления кратчайшего пути от одной исходной вершины ко всем другим вершинам, 
 тогда как алгоритмы Флойда-Уоршалла вычисляют кратчайший путь от каждого узла к каждому другому узлу.

Алгоритм Беллмана-Форда следует подходу динамического программирования, переоценивая длину пути от начальной вершины до всех других вершин.
 А затем он начинает ослаблять оценки, обнаруживая новые пути, которые короче предыдущих. 
 За этим процессом следуют все вершины N-1 раз для нахождения оптимизированного результата.
'''

class Graph:

    def __init__(self, vertices):
        self.M = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges

    def add_edge(self, a, b, c):
        self.graph.append([a, b, c])
    # Print the solution

    def print_solution(self, distance):
        print("Vertex Distance from Source")
        for k in range(self.M):
            print("{0}\t\t{1}".format(k, distance[k]))



    def bellman_ford(self, src):
        distance = [float("Inf")] * self.M
        distance[src] = 0

        for _ in range(self.M - 1):
            for a, b, c in self.graph:
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c



        for a, b, c in self.graph:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                print("Graph contains negative weight cycle")
                return
        self.print_solution(distance)



g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 2)
g.add_edge(2, 4, 3)
g.add_edge(2, 3, 4)
g.add_edge(4, 3, -5)

g.bellman_ford(0)