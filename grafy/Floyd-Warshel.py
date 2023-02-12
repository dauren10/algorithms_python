# Floyd Warshall Algorithm in python


# The number of vertices
nV = 4

INF = 999


'''
Алгоритм Флойда-Уоршалла — это алгоритм поиска кратчайшего пути между всеми парами вершин во взвешенном графе. 
Этот алгоритм работает как для ориентированных, так и для неориентированных взвешенных графов.
Но это не работает для графов с отрицательными циклами (где сумма ребер в цикле отрицательна).
'''
# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_warshall(G)