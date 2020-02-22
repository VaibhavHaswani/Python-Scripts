class Llist:
   
    def __init__(self):
        self.link=None
        self.data=None

        
    def createNode(self,head):
        d=input("Enter Data:")
        node=Llist()
        node.data=d
        if head.link==None:
            head.link=node
        else:
            temp=head
            while temp.link is not None:
                temp=temp.link
            temp.link=node


    def viewList(self,head):
        temp=head.link
        if temp is None:
            print("No data in the list")
        else:
            print("data:")
            while temp is not None:
                print(temp.data)
                temp=temp.link
                
    def removeItem(self,head):
         i=int(input("enter item index to remove(start is 0):"))
         temp=head
         if temp.link is None:
             print("No data in list")
         else:
             counter=0
             while temp is not None:
                 if counter==i:
                     temp.link=temp.link.link
                     break
                 temp=temp.link
                 counter+=1
             if counter!=i:
                  print("Invalid Index")
             else:
                  print("Item removed")
         
                


head=Llist()
li=Llist()
while True:
    print(''' 1)Add item to list
 2)View List
 3)Remove Item
 4)Exit''')
    o=int(input("Enter option:"))
    if  o==1:
        li.createNode(head)
    elif o==2:
        li.viewList(head)
    elif o==3:
        li.removeItem(head)
    elif o==4:
        break
    else:
        print("Enter a valid option")
    
    
        


