class Node:
    data = None
    next_node = None

    # def set_data(self,data):
    #     self.current_node = data
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # TypeError: Node() takes no arguments

    def __init__(self,data):
        self.data = data
    
    # def represent_data(self,current_node):
    #     return "current node is %s" !!!%self.current_node!!!
    def __repr__(self):
        return "<data is %s>" % self.data

#TODO:需要查找和这两个特殊函数相关的内容
    
class LinkedList:
    head = None
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None 
        #TODO:理解这句为什么可以作为判断链表为空的条件

    def size(self):
        count = 0
        current = self.head
        while current != None:
            current = current.next_node
            count += 1
        return count

    #TODO: how to use and check the codes we add
    # """
    #     bigorilla@kristen:~/group_practice/datastructures_algorithms$ python3 -i linked_list.py
    #     >>> l = linked_list()
    #     >>> N1 = Node(10)
    #     >>> l.head = N1
    #     >>> l.size()
    # """

    #TODO: three ways to add data: prepend, append, insert
    def add(self, data):
        """
        adds new Node containing data at head of the list
        takes o(1) time
        TODO: 弄清楚 “说在前面添加新结点元素不会失去对头结点的引用” 是什么意思
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        """
        search for the first node containing node that matches the key
        return the node of 'None' if not found
        """
        current = self.head
        while current != None:
            if current.data == key:
                return current
                #TODO: 这里直接返回current 但是在面向过程的语言中 自己是输出之后直接移动指针位置了 不会分成两种情况
            else:
                current = current.next_node
        return None
    #TODO: 如何检查python代码中没有对齐 如何避免这种错误
    def insert(self, data, key):
    
    def remove_data(self, data):

    def remove_key(self, key):
    
    #TODO: 明天自己先尝试写一遍上面操作 然后再看一遍视频 不是很能跟得上代码逻辑过程3:03:16
    def __repr__(self):
        """
        return a string representation of the list
        takes O(n) time
        TODO: 对比这里的repr写法和Node中的写法 明确开始创建nodes = []的含义
        """
        # current = self.head
        # while current != None:
        #     print(current)
        #     current = current.next_node
        #TODO: 这种思考方式存在的问题是什么 为什么会没有考虑到head和tail的特殊性
        
        nodes = []
        current = self.head
        while current != None:
            if current == self.head:
                # return nodes.append("[head: %s]" % current.data)
                nodes.append("[head: %s]" % current.data)
            elif current.next_node is None:
                # return nodes.append("[tail: %s]" % current.data)
                nodes.append("[tail: %s]" % current.data)
            #TODO: is的判断逻辑和!=的区别是什么
            else:
                # return nodes.append("[%s]" % current.data)
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(nodes)

#TODO: 自己每次测试代码是否可用的时候都要重新输入一遍之前的数据 很累 需要简化一些这些操作

#TODO: find something that indicates that data structure has some advantage over an array or a python list
