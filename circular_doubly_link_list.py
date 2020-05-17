class dcircular:
	start=None
	def __init__(self):
		self.data,self.plink,self.nlink=None,None,None

	def add(self,n):
		node=dcircular()
		node.data=n
		if self.start is None:
			self.start=node
			self.start.plink=self.start
			self.start.nlink=self.start
		else:
			temp=self.start.plink
			node.plink=temp
			node.nlink=self.start
			self.start.plink=node
			temp.nlink=node

	def pop(self):
		temp=self.start
		check=self.start
		if temp is None:
			print("No item in list to pop")
		else:
			if temp.plink is temp or temp.nlink is temp:
				print(f"popping item:{temp.data} ...List Empty...")
				self.start=None
			else:
				i=int(input("Enter the position of element to pop (std indexing):"))
				count=0
				while temp.nlink is not check and count!=i:
					temp=temp.nlink
					count+=1
				print(f"popping item:{temp.data}")
				temp.plink.nlink=temp.nlink
				temp.nlink.plink=temp.plink
				if i==0:
					self.start=temp.nlink

				

	def list(self):
		temp=self.start
		check=self.start
		if temp is None:
			print("No item in list")
		else:
			print("1)Print clockwise")
			print("2)Print anticlockwise")
			opt=input("Enter choice:")
			if opt=='1':
				print(temp.data)
				temp=temp.nlink
				while temp is not check:
					print(temp.data)
					temp=temp.nlink
			elif opt=='2':
				temp=temp.plink
				while True:
					print(temp.data)
					if temp is check:
						break
					temp=temp.plink
			else:
				print("..you should have entered valid option..")					



def main():
	opt=None
	dc=dcircular()
	while opt!='q':
		print('1)Add element to dclisk')
		print('2)Pop element from dclink')
		print('3)List dclist')
		opt=input('Enter option (q to quit):')
		if opt=='1':
			i=input('Enter any element')
			dc.add(i)
		elif opt=='2':
			dc.pop()
		elif opt=='3':
			dc.list()
		elif opt=='q':
			pass	
		else:
			print("Enter valid option")

if __name__=='__main__':
	main()
