class lstack:
      start=None
      def __init__(self):
            self.cursor=None
            self.data=None
      def add(self,n):
            node=lstack()
            node.data=n
            if self.start is None:
                  self.start=node
            else:
                  temp=self.start
                  while temp.cursor is not None:
                        temp=temp.cursor
                  temp.cursor=node

      def pop(self):
            temp=self.start
            if temp is None:
                  print("Nothing to pop")
            else:
                  while temp.cursor.cursor is not None:
                        temp=temp.cursor
                  print("Popping {}".format(temp.cursor.data))
                  temp.cursor=None      
                  
      def list(self):
            temp=self.start
            if temp is None:
                  print("add some thing")
            else:      
                  while temp is not None:
                        print(temp.data)
                        temp=temp.cursor

def main():
	opt=None
	q=lstack()
	while opt!='q':
		print('1)Add element to stack')
		print('2)Pop element from stack')
		print('3)List stack')
		opt=input('Enter option (q to quit):')
		if opt=='1':
			i=input('Enter any element')
			q.add(i)
		elif opt=='2':
			q.pop()
		elif opt=='3':
			q.list()
		elif opt=='q':
			pass	
		else:
			print("Enter valid option")

if __name__=='__main__':
	main()




