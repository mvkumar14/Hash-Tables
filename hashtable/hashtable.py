class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def delete(self, delete_key):
        """
        look through the linked list and delete
        a value. If the first value is the one that
        should be deleted return a reference to the second
        value 
        Outer functions must reassign values if the return
        of this function isn't None.
        """
        pass
    
    def retreive(self, retreive_key):
        """
        look through the linked list and return 
        key value if the key exists, else return None
        """
        pass

    


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

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
        """

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        
    def _ll_search(self,key):
        """
        Input a reference to a linked list 

        And the type of operation 
        you can:
        1) return a value
        2) delete a value
        if the key doesn't exist (in either case)
        then return None, and print out a message
        saying that key doesn't exist. 
        """
        valid_operations = ['delete','d','retreive','r']
        if operation not in valid_operations:
            print("internal function _ll_search was not given a valid operation")
            return None
        no_key_message = "That key isn't in this hash table"
        ll = self.storage[ll_index]

        # 0 items (delete and retreive return the same thing)
        if ll is None:
            print(no_key_message)
            # delete doesn't expect return
            # retreive expects a None
            return None

        # 1+ items
        else: # if you have a linked list stored in the index location
            ll_prev = None
            while ll is not None:
                if ll.key == key:
                    # DELETE (no return, but print success/fail)
                    if operation == "delete" or operation == 'd':
                        if ll_prev == None: # if its the first item in the linked list
                            self.storage[ll_index] = ll.next
                        else: # if it is the second item onwards:
                            ll_prev.next = ll.next # point to the 
                        return None

                    # RETREIVE (return item, and print fail if no key)
                    else: # if it is retreive 
                        return ll.value

                ll_prev = ll
                ll = ll.next
            # if it gets out of the while without returning a value
            print(no_key_message)
            return None
    
        

            


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
