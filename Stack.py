from collections import deque


class Stack :
    def __init__(self) :
        self.container = deque()

    def push(self,val) :
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self) :
        return len(self.container) == 0

    def size(self) :
        return len(self.container)

    def afficher(self) :
        for pm in self.container :
            print(pm)



Stack = Stack()
Stack.push(90)
Stack.push(9100)
Stack.push(9099)
Stack.push(9000000)
Stack.pop()
Stack.afficher()
