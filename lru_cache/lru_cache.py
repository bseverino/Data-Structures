from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        # List of key/value tuples in order of most recently used
        self.dll = DoublyLinkedList()
        # Dictionary of all key value pairs
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # Check if key exists
        if key not in self.storage:
            return
        # Find the node, then move it to the top
        current = self.dll.head
        while current.value[0] != key:
            current = current.next
        self.dll.move_to_front(current)
        # Return the value from storage
        return current.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # Check if key exists, then overwrite it
        if key in self.storage:
            self.get(key)
            self.dll.head.value = (key, value)
            self.storage[key] = value
        # If key doesn't exist
        else:
            # Check if dll is full, then delete the oldest value
            if self.size == self.limit:
                del self.storage[self.dll.tail.value[0]]
                self.dll.remove_from_tail()
            # Add node to dll and storage
            self.dll.add_to_head((key, value))
            self.storage[key] = value
            self.size = len(self.dll)
