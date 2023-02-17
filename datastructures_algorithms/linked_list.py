class Node:
    data = None
    next_node = None

    # def set_data(self,data):
    #     self.current_node = data
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # TypeError: Node() takes no arguments

    # TODO:需要查找和这两个特殊函数相关的内容
    def __init__(self,data):
        self.data = data
    
    # def represent_data(self,current_node):
    #     return "current node is %s" !!!%self.current_node!!!
    def __repr__(self):
        return "<data is %s>" % self.data
    
class linked_list:
    head = None
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None ## TODO:理解这句为什么可以作为判断链表为空的条件

    def size(self):
        count = 0
        current = self.head
        while current != None:
            current = current.next_node
            count += 1
        return count
#TODO: how to use and check the codes we add
#TODO: three ways to add data: prepend, append, insert