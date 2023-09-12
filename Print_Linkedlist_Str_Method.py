# Understanding the str method so that we can use it to print the linked list


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def __str__(self):
        return f'{self.name}-{self.age}'
    
new_person=Person("samee","26")
print(new_person)


# Logic to create str method inside the linked list is 
"""
1) Create a temp node pointing towards the head
2)  result empty variable
3) while temp node is not none:  result += str(node.value)
4) If temp node next pointer is not none then result +="-->"
5) continue the temp node at next step.

"""

def __str__(self):
    temp_node=self.head
    result=""
    while temp_node is not None:
        result +=str(temp_node.value)
        if temp_node.next is not None:
            result +='-->'
        temp_node=temp_node.next
        
    return result











