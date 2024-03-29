# Python program for implementation of MergeSort
'''
Сортировка слиянием — это алгоритм сортировки, который работает путем деления массива на более мелкие подмассивы, 
сортировки каждого подмассива и последующего слияния отсортированных подмассивов вместе для формирования окончательного отсортированного массива.

Проще говоря, мы можем сказать, что процесс сортировки слиянием состоит в том,
 чтобы разделить массив на две половины, отсортировать каждую половину, а затем снова объединить отсортированные половины. 
Этот процесс повторяется до тех пор, пока весь массив не будет отсортирован.

Вы можете задаться вопросом, в чем особенность этого алгоритма. 
У нас уже есть ряд алгоритмов сортировки, 
тогда зачем нам этот алгоритм? Одним из основных преимуществ сортировки слиянием является то, что она имеет временную сложность O(n log n), 
что означает, что она может относительно быстро сортировать большие массивы. Это также стабильная сортировка, 
что означает, что порядок элементов с одинаковыми значениями сохраняется во время сортировки.

Сортировка слиянием является популярным выбором для сортировки больших наборов данных, 
поскольку она относительно эффективна и проста в реализации. Он часто используется в сочетании с другими алгоритмами,
 такими как быстрая сортировка, для повышения общей производительности процедуры сортировки.
'''

def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the list


def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)

# This code is contributed by Mayank Khanna
