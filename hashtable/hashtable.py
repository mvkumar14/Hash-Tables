class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.no_key_message = "That key isn't in this hash table"

    def __str__(self):
        return str(self.key) + "," + str(self.value)

    def delete(self, delete_key, ll_prev=None, ll_first= None):
        """
        look through the linked list and delete
        a value. If the first value is the one that
        should be deleted return a reference to the second
        value 
        Outer functions must reassign values if the return
        of this function isn't None.

        This function returns 
        0 if key doesn't exist
        and a pointer to the first
        item of an ll with that key deleted if
        The key exists
        3 cases:
        1) key only ll value
            return None 
        2) key is first (of many) ll value
            return second key
        3) key is non-first
            have previous key point to next key
            return first key
        """
        if ll_first == None:
            ll_first = self

        if delete_key == self.key: # if the key to delete is the current key
            if ll_prev is not None: # value in middle of ll
                ll_prev.next = self.next
                return ll_first
            else: # first value of ll
                if self.next: # if you have another value
                    return self.next
                else: # if there are no other values
                    return None

        if self.next: # exists
            return self.next.delete(delete_key,self,ll_first)
        else: # if self.next == None
            print(self.no_key_message)
            return 0
        
    
    def retreive(self, retreive_key):
        """
        look through the linked list and return 
        key value if the key exists, else return None
        This doesn't modify the ll at all so it doesn't
        have to worry about location of item in ll

        Deal with empty values (a none) outside this ll
        So when this is called there is at least one value
        """
        ll = self
        while ll is not None:
            if retreive_key == ll.key:
                return ll.value
            ll = ll.next

        return None

    


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self,capacity):
        self.storage = [None]*capacity
        self.capacity = capacity
        self.current_amount = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        pass

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash_val = 5381
        my_bytes = key.encode() # get the bytes
        for val in my_bytes:
            hash_val = hash_val * 33 + val
        return hash_val

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.

        This method doesn't currently account for puts that are actually
        updates. (when the key is exactly the same istead of a collision)
        does it need to ? 
        Would you ever accidentally put in a value that already exists in the table? 
        The that you retreive, however makes sure that the most recently placed
        value is what is returned. so maybe its okay, and its just a matter 
        of efficieny?
        """
        new_val = HashTableEntry(key,value)
        li = self.hash_index(key)
        if self.storage[li]:
            new_val.next = self.storage[li]
            self.storage[li] = new_val
        else:
            self.storage[li] = new_val
        self.current_amount += 1 
        if self.current_amount > 0.7*self.capacity:
            self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        li = self.hash_index(key)
        if self.storage[li]:
            self.storage[li] = self.storage[li].delete(key)
        else:
            print("that key isn't in the hashtable")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        li = self.hash_index(key)
        if self.storage[li]:
            return self.storage[li].retreive(key)
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.capacity = self.capacity * 2
        new_storage = HashTable(self.capacity)
        for position in self.storage:
            if position: # if it isn't None
                ll = position
                while ll: 
                    new_storage.put(ll.key,ll.value)
                    ll = ll.next 
        self.storage = new_storage.storage
        # print(len(self.storage))
        pass

    
    
        

            


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
