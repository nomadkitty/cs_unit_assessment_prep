class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        self.storage = [None]*self.capacity
        self.item_stored = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.item_stored/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # prime and offset basis are based on 64bit
        FNV_prime = 1099511628211
        FNV_offset_basis = 14695981039346656037

        hash_index = FNV_offset_basis
        bytes_to_hash = key.encode()
        for byte in bytes_to_hash:
            hash_index = hash_index * FNV_prime
            hash_index = hash_index ^ byte
        return hash_index

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_index = 5381
        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            hash_index = ((hash_index << 5) + hash_index) + byte
        return hash_index

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)

        # insert into an empty spot
        if not self.storage[hash_index]:
            self.storage[hash_index] = HashTableEntry(key, value)
            self.item_stored += 1

        # linked list exists at current location
        # two situations: update value for an existing key or create a new entry for the new key
        else:
            current = self.storage[hash_index]

            while current.key != key and current.next:
                current = current.next

            # find key, update current value
            if current.key == key:
                current.value = value

            # key not found, add a entry
            else:
                current.next = HashTableEntry(key, value)
                self.item_stored += 1

        # resize if load factor is too big
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        current = self.storage[hash_index]
        # 1. nothing to delete
        if not current:
            print("The key is not found")

        # 2. 1 element, the head in the index bucket
        elif not current.next:
            self.storage[hash_index] = None
            self.item_stored -= 1
        else:
            # store a pointer to the previous node
            prev = None

            # Move to the next node if key won't match and there is a next
            while current.key != key and current.next:
                prev = current
                current = current.next

            # 3. value to delete in the end of index bucket
            if not current.next:
                prev.next = None
                self.item_stored -= 1
            # 4. value in the middle of the index bucket
            else:
                prev.next = current.next
                self.item_stored -= 1

        # resize if load factor is too small
        if self.get_load_factor() < 0.2:
            self.resize(self.capacity // 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.storage[hash_index]:
            current = self.storage[hash_index]
            while current.key is not key and current.next:
                current = current.next
            if not current.next:
                return current.value
            else:
                return current.value
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_storage = self.storage

        # initialize new hashtable
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        # loop through and add each node to new hashtable
        for item in old_storage:
            if item:
                current = item
                while current:
                    self.put(current.key, current.value)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
