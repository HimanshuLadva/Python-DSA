# A hash table is a data structure that uses hashing to store key-value pairs. It provides very fast average-case operations: O(1) for insertion, deletion, and lookup.
# Collision handing method:     
# Chaining (Separate Chaining)
# Store multiple key-value pairs at the same index using a linked list or dynamic array.
# inner implementation of hash table
class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
            
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f"key {key} is not found")
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in self.table[index]:
            if k == key:
                del self.table[index][i]

        raise KeyError(f"key {key} is not found")
    
ht = HashTable(5)
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("grape", 300)  # Might collide with apple
ht.insert("mango", 400)
print(ht.table)

from collections import defaultdict
h1 = {} # simple way to use hash table
h2 = defaultdict(int) # default value with 0
h3 = defaultdict(str) # default value with ''

arr = [1,1,2,2,2,3,3,3,3,5,5,6,6]
for x in arr:
    h2[x] += 1

print(h2)
