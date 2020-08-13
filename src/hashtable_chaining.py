from .exception import *
from .doublylinkedlist import DoublyLinkedList

#Pseudocode
#Same as in hashtable.py except that insertions have to be linkedist and lookups have to find form linkedlist
# This Hashtable implementation uses LinkedList to address Hash collision i.e. two values have same hash.
# Entry class is used to maintain key, value pair.
# each entry in hashtable is a doublelinkedlist with data of type Entry(K,V).
# Each of the doublylinkedlist can contain multiple entries for same "key".
# maintain a resize_table method since initial capacity of HashTable fixed and must grow, 
# if it needs to preserve O(1) for inserts, lookups, removals - resize the table if size of table > threshold
# For every insert: find an entry by looking up key and if entry already exists, then update and insert in bucket
# and if entry does not already exist, add entry to bucket and update the HashTable with updated bucket.

class Key():
    """Key class maintains hash of a key. This is the single place a hash is generated for all entries.
    """
    def __init__(self, key):
        self.key = key
        self.hash = hash(key)
    
    def __eq__(self, key_obj):
        if key_obj == None:
            return False
        if self.hash != key_obj.hash:
            return False
        return self.key == key_obj.key
    
    def __str__(self):
        return str(self.key)

class Entry():
    """Entry class has key and value with respective hash values.
       Instances can be used to insert into another list for hash tables.
       The 'Entries' are comparable for keys and can be converted to string format.
    """
    def __init__(self, key, value):
        if key!=None:
            self.key = Key(key)
            self.hash = self.key.hash
        self.value = value
    
    def __eq__(self, entry):
        if entry == None:
            return False
        if self.hash != entry.hash:
            return False
        return self.key == entry.key
    
    def __str__(self):
        return str(self.key) + ":" +str(self.value)


class ChainedHashTable():
    """Hash Collision by Seperate chaining mechanism, implementation of Hash table.
       There is an list of DoubleLinkedList of Entry('Key' key, value) with an index of hashed keys each with key,value pair.
       Operations supported: add, put, insert, get
    """
    def __init__(self, capacity=10, max_load_factor=0.75):
        self.table = [DoublyLinkedList(Entry(None,None), 0)] * capacity
        self.capacity = max(3, capacity) #allow a default hashtable size of >=3
        self.max_load_factor = max_load_factor
        self.threshold = int(capacity * max_load_factor)
        self.size = 0
    
    def has_key(self, key):
        """Checks if key exists in

        Args:
            key ([type]): type Key with [key, hash] pair

        Returns:
            boolean : True if key exists in Hashtable
        """
        key = Key(key)
        index = self.normalize_hash(key.hash)
        return self.bucket_seek_enrty(index, key) != None
    
    def clear(self):
        """Clear the entries of HashTable
        """
        self.table = None
        self.capacity = 0

    def resize_table(self):
        """Resize the Hashtable to preserve the time complexity for all the operations i.e. O(1).
           Hashtable grows in capacity. Default capacity is 3 unless not 
           explicitly specified during creation.
        """
        self.capacity *= 2
        self.threshold = self.capacity * self.max_load_factor
        new_table = [DoublyLinkedList(Entry(None, None), 0)] * self.capacity
        for i in range(0, len(self.table)):
            if self.table[i] != None:
                for entry in self.table[i]:
                    bucket_index = self.normalize_hash(entry.hash)
                    bucket = new_table[bucket_index] = DoublyLinkedList(None, 0)
                    bucket.add(entry)
                self.table[i].clear()
                self.table[i] = None
        self.table = new_table

    def normalize_hash(self, keyhash):
        """Hash the given key and normalize the hash value (to avoid negative hash values)
           keyhash mod capacity ( current, growing capacity of the HashTable)

        Args:
            key (object) : keyhash to be normalized

        Returns:
            positive integer: hashed index 
        """
        return keyhash % self.capacity
    
    def add(self, key, value):
        """Add a key, value pair to the Hash table.

        Args:
            key (object): raw key to be added
            value (object): corresponding value of the key
        """        
        self.insert(key, value)
    
    def put(self, key, value):
        """Put a key, value pair to the Hash table.

        Args:
            key (object): raw key to be added
            value (object): corresponding value of the key
        """
        self.insert(key, value)
    
    # Naive case (this add function does not do hash collision)
    def insert(self, key, value):
        """Insert a key, value pair to the Hash table.

        Args:
            key (object): raw key to add
            value (object): corresponding value of the key
        """
        entry = Entry(key, value)
        index = self.normalize_hash(entry.hash)
        self.bucket_insert_enrty(index, entry)
    
    def bucket_insert_enrty(self, index, entry):
        """Insert an Entry into the HashTable

        Args:
            index (hash): unnormalized key hash
            entry (Entry): Entry to be inserted

        Returns:
            [type]: [description]
        """
        bucket = self.table[index]
        if bucket == None:
            self.table[index] = bucket = DoublyLinkedList(None,0)
        existing_entry = self.bucket_seek_enrty( index, entry.key)
        if existing_entry == None:
            bucket.add(entry)
            self.size += 1
            if self.size < self.threshold:
                self.resize_table()
            #No previous value
            return None
        else:
            bucket.add(entry)
            old_val = existing_entry.value
            #existing_entry.value = entry.value
            return old_val
    
    def bucket_seek_enrty(self, index, key):
        """Seek an entry for a bucket index. Find and return the entry for specified bucketindex, key

        Args:
            index (hashed): normalized hashed bucket index
            key (Key): type Key with [key, hash]

        Returns:
            entry (Entry): return each entry for the key
        """
        if key == None:
            return None
        bucket = self.table[index]
        if bucket == None:
            return None
        for entry in bucket:
            if entry.key == key:
                return entry
        return None

    def remove(self, key):
        """Remove a key from HashTable

        Args:
            key (Key): type Key with [key, hash]

        Returns:
            value: returns value of entry removed from each bucket
        """
        if key == None:
            return None
        bucket_index = self.normalize_hash(key.hash)
        return self.bucket_remove_enrty(bucket_index, key)

    def bucket_remove_enrty(self, index, key):
        """Remove a key and also delete the corresponding bucket

        Args:
            index ([type]): hashed bucket index
            key ([type]): type Key with [key, hash]

        Returns:
            value: returns value if the key was successfully removed
        """
        entry = self.bucket_seek_enrty(self, index, key)
        if entry != None:
            linkedlist = self.table[index]
            linkedlist.remove(entry)
            self.size -= 1
            return entry.value
        else:
            return None
        
    def keys(self):
        """Get all keys from HashTables

        Returns:
            list [Key]: list of keys each of type Key with [key, hash] where hash is the unnormalized hash
        """
        keys = []
        for bucket in self.table:
            if bucket != None:
                for entry in bucket:
                    keys.add(entry.key)
        return keys
    
    def values(self):
        """Get all values in HashTable

        Returns:
            list: list of values
        """
        values = []
        for bucket in self.table:
            if bucket != None:
                for entry in bucket:
                    values.add(entry.value)
        return values

    def get(self, key):
        """Get the value of the key

        Args:
            key (object): key to look up

        Returns:
            [type]: retrieved value of the key for the bucket index
        """
        values = []
        if key == None:
            return None
        key_obj = Key(key)
        index = self.normalize_hash(key)
        bucket = self.table[index]
        if bucket == None:
            return None
        for entry in bucket:
            if entry.key == key_obj:
                values.append(entry.value)
        return values
