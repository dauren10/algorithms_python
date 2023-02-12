'''
Сортировка Шелла в основном является разновидностью сортировки вставками. 
При сортировке вставками мы перемещаем элементы только на одну позицию вперед. 
Когда элемент нужно переместить далеко вперед, задействовано много движений. Идея ShellSort состоит в том, 
чтобы разрешить обмен удаленными элементами. В сортировке Шелла мы отсортируем массив по h для большого значения h.
 Мы продолжаем уменьшать значение h, пока оно не станет равным 1. Говорят, что массив отсортирован по h, если все подсписки каждого h-го
   элемента отсортированы.

Алгоритм:

Шаг 1 — Начать
Шаг 2 — Инициализируйте значение размера зазора. Пример: ч
Шаг 3 — Разделите список на меньшую часть. Каждый должен иметь равные интервалы до h
Шаг 4 — Отсортируйте эти подсписки, используя сортировку вставками.
Шаг 5 — Повторяйте этот шаг 2, пока список не будет отсортирован.
Шаг 6 – Распечатайте отсортированный список.
Шаг 7 – Стоп.
'''

# Python3 program for implementation of Shell Sort
# Python3 program for implementation of Shell Sort

def shellSort(arr, n):
	# code here
	gap=n//2
	
	
	while gap>0:
		j=gap
		# Check the array in from left to right
		# Till the last possible index of j
		while j<n:
			i=j-gap # This will keep help in maintain gap value
			
			while i>=0:
				# If value on right side is already greater than left side value
				# We don't do swap else we swap
				if arr[i+gap]>arr[i]:

					break
				else:
					arr[i+gap],arr[i]=arr[i],arr[i+gap]

				i=i-gap # To check left side also
							# If the element present is greater than current element
			j+=1
		gap=gap//2





# driver to check the code
arr2 = [12, 34, 54, 2, 3]
print("input array:",arr2)

shellSort(arr2,len(arr2))
print("sorted array",arr2)

# This code is contributed by Illion
