'''
Кодирование Хаффмана — это метод сжатия и кодирования текста без потерь, основанный на частоте символов в тексте. 
В исследованиях теории информации и информатики код Хаффмана представляет собой особый тип оптимального префиксного кода, 
который обычно используется для сжатия данных без потерь.

Часто встречающаяся буква или символ иллюстрируется более коротким кодом, 
а редко встречающаяся буква или символ иллюстрируется более длинным кодом.
Эта мысль приводит к эффективному изображению персонажей, для хранения которых требуется меньше памяти. Следовательно, мы можем сделать вывод, что мы можем использовать кодирование Хаффмана в качестве метода сжатия данных.

Давайте теперь разберемся с теорией кодирования Хаффмана.
Понимание теории кодирования Хаффмана

Мы знаем, что файл хранится на компьютере в виде двоичного кода и что каждому символу в файле присвоен двоичный символ, а коды символов обычно имеют фиксированную длину для отдельных символов. Кодирование Хаффмана основано на частоте появления каждого символа в файле и количестве символов в структуре данных с частотой, равной нулю (0). Кодировка Хаффмана для типичного текстового файла экономит около 40 процентов размера фактических данных. Таким образом, двоичный код Хаффмана, подобно скомпилированным исполняемым файлам, имел бы явную экономию места. Двоичный файл, в котором символ ASCII закодирован с частотой 0,5, будет иметь очень другую частоту и распределение по сравнению с его эквивалентом ASCII.

Чтобы сжать файл, используя последовательность символов, нам нужна таблица, которая предоставляет нам последовательности битов, используемых для каждого символа. Эта таблица создает дерево кодирования, в котором используется путь корня/листа для создания битовой последовательности, кодирующей символы. Мы можем следовать корням и листьям, чтобы создать список символов с максимальной битовой длиной закодированных символов и количеством вхождений.

Мы можем использовать жадный алгоритм для построения оптимального дерева. Деревья кодирования Хаффмана возвращают кодировки символов минимальной длины, используемые при сжатии данных. Узлы в дереве изображают частоту появления символа. Корневой узел отображает длину строки, а обход дерева дает нам кодировку, указанную для символа. Как только дерево построено, обход дерева дает нам соответствующие коды каждого символа.

Оптимальное дерево после завершения показано в следующей таблице и на изображении:
'''
# A Huffman Tree Node
import heapq

class node:
	def __init__(self, freq, symbol, left=None, right=None):
		# frequency of symbol
		self.freq = freq

		# symbol name (character)
		self.symbol = symbol

		# node left of current node
		self.left = left

		# node right of current node
		self.right = right

		# tree direction (0/1)
		self.huff = ''
		
	def __lt__(self, nxt):
		return self.freq < nxt.freq
		

# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def printNodes(node, val=''):
	
	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node
	# then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

		# if node is edge node then
		# display its huffman code
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")


# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']

# frequency of characters
freq = [ 5, 9, 12, 13, 16, 45]

# list containing unused nodes
nodes = []

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
	heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:
	
	# sort all the nodes in ascending order
	# based on their frequency
	left = heapq.heappop(nodes)
	right = heapq.heappop(nodes)

	# assign directional value to these nodes
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create
	# new node as their parent
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

	heapq.heappush(nodes, newNode)

# Huffman Tree is ready!
printNodes(nodes[0])
