class LinkedPair:
    """Linked List hash table key/value pair"""

    def __init__(self, key, value):
        """Constructor for the creation of a node in a Linked List chain"""
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """A hash table with `capacity` buckets that accepts string keys"""

    def __init__(self, capacity):
        """Constructor to create a new instance of this class with the starting size"""
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """Hash an arbitrary key and return an integer"""
        # OPTIONAL STRETCH: You may replace the Python hash with DJB2 as a stretch goal
        return hash(key)

    def _hash_djb2(self, key):
        """Hash an arbitrary key using DJB2 hash"""
        # OPTIONAL STRETCH: Research and implement DJB2
        pass

    def _hash_mod(self, key):
        """Take an arbitrary key and return a valid integer index within the storage capacity of the hash table"""
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """Store the value with the given key. Hash collisions should be handled with: Linked List chaining"""
        index = self._hash_mod(key)
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            last_node = self.storage[index]
            while last_node.next is not None:
                if last_node.key == key:
                    last_node.value = value
                    return
                last_node = last_node.next
            last_node.next = LinkedPair(key, value)

    def remove(self, key):
        """Remove the value stored with the given key. Print a warning if the key is not found"""
        index = self._hash_mod(key)
        value = self.storage[index]
        if value is not None:
            node = self.storage[index]
            while node is not None:
                if node.key == key:
                    node = node.next
        print(f'An element with key {key} cannot be found!')

    def retrieve(self, key):
        """Retrieve the value stored with the given key. Return None if the key is not found"""
        index = self._hash_mod(key)
        value = self.storage[index]
        if value is not None:
            node = self.storage[index]
            while node is not None:
                if node.key == key:
                    return node.value
                node = node.next
        return None

    def resize(self):
        """Doubles the capacity of the hash table and rehash all key/value pairs"""
        self.capacity *= 2
        temp_storage = [None] * self.capacity
        for i in range(len(self.storage)):
            node = self.storage[i]
            while node is not None:
                index = self._hash_mod(node.key)
                node_to_add = temp_storage[index]
                if node_to_add is not None:
                    while node_to_add.next is not None:
                        node_to_add = node_to_add.next
                temp_storage[index] = LinkedPair(node.key, node.value)
        self.storage = temp_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
