

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singlyLinkedList01:
        def __init__(self) -> None:
             self.tail = None
        
        def append(self, data):
            node = Node(data)

            if self.tail == None:
                self.tail = node
            else:
                current = self.tail
                while current.next:
                    current = current.next
                current.next = node


class singlyLinkedList02:
    def __init__(self) -> None:
        self.tail = None
        self.head = None
        self.size = 0

    def append(self,data):
        node = Node(data)

        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1
    
    def getSize(self):
        return self.size
    
    def iter(self):
        current = self.tail
        while current:
            value = current.data
            current = current.next
            yield value

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False
    
    def clear(self):
        """ Clear the entire list. """
        self.tail = None
        self.head = None

if __name__ == "__main__":
    print("hello, Mr12")
