class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list in empty")
            return

        itr = self.head
        llst = ""

        while itr:
            llst = llst + str(itr.data) + "-->"
            itr = itr.next
        print(llst)

    def insert_at_end(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, date_list):
        self.head = None
        for data in date_list:
          self.insert_at_end(data)

    def length_list(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 :
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length_list():
            raise Exception("Invalid index")



        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        node = Node(data, None)
        while itr:
            if count == index - 1:
                node.next = itr.next
                itr.next = node
                break
            count = count + 1
            itr = itr.next


    def remove_value(self, value):
        if self.head is None:
            return
        itr = self.head
        while itr:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
        itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(3)
    ll.insert_at_end(80)
    ll.insert_at_end(93)
    ll.print()
    ll.insert_at(1,"coucou")
    ll.print()
    ll.remove_value("coucou")
    ll.print()







