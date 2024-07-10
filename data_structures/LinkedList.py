class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_begining(data)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)

        itr = self.head

        for _ in range(index - 1):
            itr = itr.next

        node = Node(data, itr.next)
        itr.next = node

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head

        for i in range(index - 1):
            itr = itr.next

        if index == self.get_length() - 1:
            itr.next = None
        else:
            itr.next = itr.next.next

    def insert_values(self, data_list):
        for i in data_list:
            self.insert_at_end(i)

    def print(self):
        itr = self.head
        data = []
        while itr:
            data.append(itr.data)
            itr = itr.next

        print('---->'.join(map(str, data)))


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(1, "blueberry")
    ll.remove_at(2)
    ll.print()

    ll = LinkedList()
    ll.insert_values([45, 7, 12, 567, 99])
    ll.insert_at_end(67)
    ll.print()
