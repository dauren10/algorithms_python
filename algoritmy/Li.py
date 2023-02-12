'''
Определение: Алгоритм Ли — это одно из возможных решений задач маршрутизации в лабиринтах, 
основанное на поиске в ширину. Он всегда дает оптимальное решение, если оно существует, но работает медленно и требует много памяти.
 Мы изучим алгоритм Ли на Python, решив задачу маршрутизации в лабиринте.
'''
#importing libraries
import sys
from collections import deque

# All four potential movements from a cell are listed here.
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

# Whether it is possible to move from the current position to position (row, col)
#  is determined by this function. If row, col is not in a legal location, 
# has a value of 0, or has already been visited, the method returns false.

def Validate(matrix, visited, row, col):
	return (row >= 0) and (row < len(matrix)) and (col >= 0) and (col < len(matrix[0])) \
		   and matrix[row][col] == 1 and not visited[row][col]


# Find the shortest path between sources and destinations in a matrix.
def Shortest_Path(matrix, source, destination):

	# get source cell (i, j)
	i, j = source
	
	# get destination cell (x, y)
	x, y = destination

	# base case: invalid input
	if not matrix or len(matrix) == 0 or matrix[i][j] == 0 or matrix[x][y] == 0:
		return -1

	# `M × N` matrix
	(M, N) = (len(matrix), len(matrix[0]))
	
	# construct a matrix to keep track of visited cells
	visited = [[False for x in range(N)] for y in range(M)]
	
	# create an empty queue
	q = deque()
	
	# mark the source cell as visited and enqueue the source node
	visited[i][j] = True

	# (i, j, dist) represents matrix cell coordinates, and their
	# minimum distance from the source
	q.append((i, j, 0))

	# stores length of the longest path from source to destination
	min_dist = sys.maxsize

	# loop till queue is empty
	while q:
		# dequeue front node and process it
		(i, j, dist) = q.popleft()

		# (i, j) represents a current cell, and `dist` stores its
		# minimum distance from the source.
		# if the destination is found, update `min_dist` and stop
		if i == x and j == y:
			min_dist = dist
			break

		# check for all four possible movements from the current cell
		# and enqueue each valid movement
		for k in range(4):
		    
			# check if it is possible to go to position
			# (i + row[k], j + col[k]) from current position
			if Validate(matrix, visited, i + row[k], j + col[k]):
			    
				# mark next cell as visited and enqueue it
				visited[i + row[k]][j + col[k]] = True
				q.append((i + row[k], j + col[k], dist + 1))

	if min_dist != sys.maxsize:
		return min_dist
	else:
		return -1


if __name__ == '__main__':

	matrix = [
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
		[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
		[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
		[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
	]

	source = (0, 0)
	destination = (3, 2)

	min_dist = Shortest_Path(matrix, source, destination)

	if min_dist != -1:
		print("The length of the shortest route between sources and destinations :- ", min_dist)
	else:
		print("The source cannot lead to")