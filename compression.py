from random import randint
class Tree:
	right = None
	left = None
	value = 0
	letter = ""
	
	def __init__(self, value, letter = "", left = None, right = None):
		self.value = value
		self.letter = letter
		self.left = left
		self.right = right
	
	def __gt__(self, other):
		return self.value > other.value
	
	def __ge__(self, other):
		return self.value >= other.value
		
	def __lt__(self, other):
		return self.value < other.value
		
	def __le__(self, other):
		return self.value <= other.value
	
	def __eq__(self, other):
		return self.letter == other
	
	def __repr__(self):
		return "[" + self.letter + ", " + str(self.value) + "]"
	
	def is_leaf(self):
		return (self.left == None and self.right == None)
		

with open ("test.txt", "r") as myfile:
	input=myfile.read()
	
#input = "this is sissty"
nodes = []
dic = {}

def generate_node_list():
	global nodes
	global input
	for i in input:
		if i not in nodes:
			nodes.append(Tree(1, i))
		else:
			for k in nodes:
				if k.letter == i:
					k.value = k.value + 1
					break
	nodes = sorted(nodes)[::-1]

def merge_from_bottom():
	global nodes
	while len(nodes) > 1:
		node1 = nodes.pop()
		node2 = nodes.pop()
		new_node = Tree(node1.value + node2.value, "", node1, node2)
		nodes.append(new_node)
		nodes = sorted(nodes)[::-1]

def get_random_leaf():
	global nodes
	n = nodes[0]
	while n.is_leaf() == False:
		#print(n)
		num = randint(0, 1)
		if num == 0:
			n = n.left
		else:
			n = n.right
	return(n)

def fill_dic():
	global nodes
	global dic
	n = nodes[0]
	def helper(node, path):
		if node.is_leaf():
			dic[node.letter] = path
		else:
			helper(node.left, path + "0")
			helper(node.right, path + "1")
	helper(n, "")
	
def compress_string():
	global input
	s = ""
	for i in input:
		s += dic[i]
	return s


generate_node_list()
merge_from_bottom()
fill_dic()
compressed = compress_string()
print("Length before compression (bits): " + str((len(input) * 8)))
print("Length after compression (bits): " + str(len(compressed)))

#print("Before: " + str(len(input)) + ", After: " + str(len(str(int(compressed, 2)))))



