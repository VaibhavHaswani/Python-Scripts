import queue 


class Tree:
	rightChild=None
	leftChild=None
	def __init__(self,data):
		self.data=data
	@staticmethod
	def height(node):
		if node is None:
			return 0
		return 1+max(Tree.height(node.leftChild),Tree.height(node.rightChild))
	@staticmethod
	def size(node):
		if node is None:
			return 0
		return 1+Tree.size(node.leftChild)+Tree.size(node.rightChild)
	#T R A V E R S A L S
	@staticmethod
	def inorder(node):
		if node is None:
			return
		Tree.inorder(node.leftChild)
		print(node.data,end="\t")
		Tree.inorder(node.rightChild)
	@staticmethod
	def preorder(node):
		if node is None:
			return
		print(node.data,end="\t")
		Tree.preorder(node.leftChild)
		Tree.preorder(node.rightChild)
	@staticmethod
	def postorder(node):
		if node is None:
			return
		Tree.postorder(node.leftChild)
		Tree.postorder(node.rightChild)
		print(node.data,end="\t")
	@staticmethod
	def levelorder(node):
		if node is None:
			return
		q=queue.Queue()
		q.put(node)
		while not q.empty():
			node=q.get()
			print(node.data,end="\t")
			if node.leftChild is not None:
				q.put(node.leftChild)
			if node.rightChild is not None:
				q.put(node.rightChild)



t=Tree("A")
t.leftChild=Tree("B")
t.rightChild=Tree("C")
t.leftChild.leftChild=Tree("D")
t.leftChild.rightChild=Tree("E")
t.rightChild.leftChild=Tree("F")
t.rightChild.rightChild=Tree("G")


print("T R E E\n")
print(f"Height:{Tree.height(t)}\tSize:{Tree.size(t)}\n")
print("Inorder:")
Tree.inorder(t)
print("\nPreorder:")
Tree.preorder(t)
print("\nPostorder:")
Tree.postorder(t)
print("\nLevelOrder:")
Tree.levelorder(t)
print()
