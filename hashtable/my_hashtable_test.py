import unittest
from hashtable import HashTableEntry

class TestHashll(unittest.TestCase):

    def ll_delete_test(self):
        # ONE ENTRY 
        he = HashTableEntry('1','1')

        # delete key that doesn't exist
        return_value = he.delete('2')
        self.assertTrue(return_value == 0)
        
        # delete only key
        return_value = he.delete('1')
        self.assertTrue(return_value == None)

        # MULTIPLE ENTRIES
        he = HashTableEntry('1','1')
        he.next = HashTableEntry('2','2')
        he.next.next = HashTableEntry('3','3')
        he.next.next.next = HashTableEntry('4','4')

        he_second = he.next
        he_third = he.next.next

        # delete first key
        self.assertTrue(he.delete('1') == he_second)
        while he.next:
            print(he)
            he = he.next

        # delete non-first key
        self.assertTrue(he.delete('3') == he_second)
        while he.next:
            print(he)
            he = he.next


if __name__ == '__main__':
    unittest.main()