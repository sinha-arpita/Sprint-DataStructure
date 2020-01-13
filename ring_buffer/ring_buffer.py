from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()


    def append(self, item):

        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.writePtr = self.storage.head
            return

        self.writePtr.value = item
        self.writePtr = self.writePtr.next
        if self.writePtr == None:
            self.writePtr = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node and node.value != None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.currentPtr = 0

    def append(self, item):
        self.storage[self.currentPtr] = item
        self.currentPtr += 1
        self.currentPtr = self.currentPtr % (len(self.storage))

    def get(self):
        items = []
        for item in self.storage:
            if item:
                items.append(item)

        return items
