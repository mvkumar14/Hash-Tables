from hashtable import HashTableEntry,HashTable

ht = HashTable(4)
a = ht.storage
print(len(a))
ht.resize()
a = ht.storage
print(len(a))

# region HashTableEntry Test
"""
he = HashTableEntry('1','value')
# print(he)


# MULTIPLE ENTRIES
he = HashTableEntry('1','1')
he.next = HashTableEntry('2','2')
he.next.next = HashTableEntry('3','3')
he.next.next.next = HashTableEntry('4','4')

he_second = he.next
he_third = he.next.next

# delete first key
# self.assertTrue(he.delete('1') == he_second)
new = he.delete('1')
print(new)
print('^deleted:')
while new.next:
    print(he)
    he = he.next

# delete non-first key
# self.assertTrue(he.delete('3') == he_second)
he.delete('3')
while he.next:
    print(he)
    he = he.next
"""
# endregion

# region ll_search() function (inside HashTable)
"""
def _ll_search(self,key):

        '''
        Input a reference to a linked list 

        And the type of operation 
        you can:
        1) return a value
        2) delete a value
        if the key doesn't exist (in either case)
        then return None, and print out a message
        saying that key doesn't exist. 
        '''
        valid_operations = ['delete','d','retreive','r']
        if operation not in valid_operations:
            print("internal function _ll_search was not given a valid operation")
            return None
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
"""
# endregion
