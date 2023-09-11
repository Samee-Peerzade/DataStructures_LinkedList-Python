
# Creating a Node : Node = Value + Next Pointer  

class Node:
    
    def __init__(self,value):
        self.value=value
        self.next=None
        
        
# Creating LinkedList : Head and Tail pointing towards the node 
      
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
new_Linked_list=LinkedList(10)
print(new_Linked_list.head.value) #10
print(new_Linked_list.length)  #1
            
            
            
            