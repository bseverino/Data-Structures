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
        # List of individual key value pairs
        self.cache = DoublyLinkedList()
        # Dictionary of all key value pairs
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get_max(self):
        current = self.head
        max = self.head.value
        while (current is not None):
            if current.value > max:
                max = current.value
            current = current.next
        return max

    def get(self, key):
        # Check if key exists
        if key not in self.storage:
            return
        # Find the node, then move it to the top
        current = self.cache.head
        while current.value['key'] != key:
            current = current.next
        self.cache.move_to_front(current)
        # Return the value from storage
        return self.storage[key]

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
            self.cache.head.value['value'] = value
            self.storage[key] = value
        # If key doesn't exist
        else:
            # Check if cache is full, then delete the oldest value
            if self.size == self.limit:
                del self.storage[self.cache.tail.value['key']]
                self.cache.remove_from_tail()
            # Add node to cache and storage
            self.cache.add_to_head({'key': key, 'value': value})
            self.storage[key] = value
            self.size = len(self.cache)
            print('set')
