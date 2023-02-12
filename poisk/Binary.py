'''
В двух словах, этот алгоритм поиска использует набор элементов, который уже отсортирован, игнорируя половину элементов после всего лишь одного сравнения.

     Сравните x со средним элементом.
     Если x совпадает со средним элементом, мы возвращаем средний индекс.
     В противном случае, если x больше среднего элемента, то x может лежать только в правой (большей) половине подмассива после среднего элемента. Затем снова применяем алгоритм для правой половины.
     В противном случае, если x меньше, цель x должна лежать в левой (нижней) половине. Итак, применяем алгоритм для левой половины.
'''

def binary_search(lst,search_item):
    low = 0
    high = len(lst) - 1
    search_res = False
    count_iter = 0
    while search_res is False:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_item:
            search_res = True
            break
        elif guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
        count_iter += 1
    return count_iter


lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
search_item = 9
result = binary_search(lst,search_item)
print(result)