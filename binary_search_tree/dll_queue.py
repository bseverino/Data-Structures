from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if len(self.storage) == 0:
            return
        return self.storage.remove_from_head()

    def len(self):
        return len(self.storage)
