class maxHeap():
    data=[0]
    def __init__(self,data):
        self.data+=data
        self._arrangeHeap()
    def print(self):
        print(self.data[1:])
    def _arrangeHeap(self):
        self.data.sort(reverse=True)
        l=0
        while l<len(self.data)-1:
            try:
                self.data[l*2],self.data[(l*2)+1]=self.data[(l*2)+1],self.data[l*2]
                l+=1
            except:
                break    



def main():
    heap=maxHeap([3,2,5,1,7,43,23])
    heap.print()

if __name__=="__main__":
    main()    