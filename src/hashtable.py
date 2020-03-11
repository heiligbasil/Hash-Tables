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
        self.key_count = 0

    def _get_load_factor(self):
        return self.key_count / self.capacity

    def _hash(self, key):
        """Hash an arbitrary key and return an integer"""
        # OPTIONAL STRETCH: You may replace the Python hash with DJB2 as a stretch goal
        # return hash(key)
        return self._hash_djb2(key)

    def _hash_djb2(self, key):
        """Hash an arbitrary key using DJB2 hash"""
        # OPTIONAL STRETCH: Research and implement DJB2
        hash_grotto = 5381
        for k in key:
            hash_grotto = ((hash_grotto << 5) + hash_grotto) + ord(k)
        return hash_grotto & 0xFFFFFFFF

    def _hash_mod(self, key):
        """Take an arbitrary key and return a valid integer index within the storage capacity of the hash table"""
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """Store the value with the given key. Hash collisions should be handled with: Linked List chaining"""
        index = self._hash_mod(key)
        node = self.storage[index]
        if node is None:  # Empty bucket, so add the value here
            self.storage[index] = LinkedPair(key, value)
            self.key_count += 1
        elif node.key == key:  # Replace bucket at head-level with new value
            node.value = value
        else:  # Try to find the key within the linked list chain
            while node.next is not None:
                node = node.next
                if node.key == key:
                    node.value = value
                    return
            node.next = LinkedPair(key, value)
            self.key_count += 1  # load_factor = self._get_load_factor()  # if load_factor < 0.2 or load_factor > 0.8:  #     self.resize()

    # def insert_guided_lecture(self, key, value):
    #     index = self._hash_mod(key)
    #     if self.storage[index] is not None:
    #         print("ERROR: Key in use")
    #     else:
    #         self.storage[index] = value

    def remove(self, key):
        """Remove the value stored with the given key. Print a warning if the key is not found"""
        index = self._hash_mod(key)
        node = self.storage[index]
        node_before = None
        if node:
            while node:
                if node.key == key:
                    if node_before:
                        node_before.next = node.next
                    elif node.next:
                        self.storage[index] = node.next
                    else:
                        self.storage[index] = None
                    self.key_count -= 1
                    return
                node_before = node
                node = node.next
        print(f"An element with key '{key}' cannot be found!")

    # def remove_guided_lecture(self, key, value):
    #     index = self._hash_mod(key)
    #     if self.storage[index] is not None:
    #         self.storage[index] = None
    #     else:
    #         print("WARNING: Key not found")

    def retrieve(self, key):
        """Retrieve the value stored with the given key. Return None if the key is not found"""
        index = self._hash_mod(key)
        node = self.storage[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    # def retrieve_guided_lecture(self, key):
    #     index = self._hash_mod(key)
    #     return self.storage[index]

    def resize(self):
        """Doubles the capacity of the hash table and rehash all key/value pairs"""
        load_factor = self._get_load_factor()
        if load_factor < 0.2:
            self.capacity //= 2
        elif load_factor > 0.7:
            self.capacity *= 2
        else:
            print(f'Resizing unnecessary due to a load factor of {load_factor}:.2f')
            return
        temp_storage = [None] * self.capacity
        for i in range(len(self.storage)):
            node = self.storage[i]
            while node is not None:
                index = self._hash_mod(node.key)
                node_to_add = temp_storage[index]
                if node_to_add is None:
                    temp_storage[index] = LinkedPair(node.key, node.value)
                else:
                    while node_to_add is not None:
                        if node_to_add.next is None:
                            node_to_add.next = LinkedPair(node.key, node.value)
                            break
                        node_to_add = node_to_add.next
                node = node.next
        self.storage = temp_storage

    # def resize_guided_lecture(self):
    #     old_storage = self.storage.copy()
    #     self.capacity *= 2
    #     self.storage = [None] * self.capacity
    #     for bucket_item in old_storage:
    #         self.insert_guided_lecture("dummy", bucket_item)


if __name__ == "__main__":
    ht = HashTable(65)

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
