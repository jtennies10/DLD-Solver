"""
Defines the DirectHashTable, which uses a dictionary to store
hash buckets. Since in a direct hash table the key is the index,
a dictionary is in essence a direct hash table.
"""
class DirectHashTable:

    """
    Initializes the table with an empty dictionary
    """
    def __init__(self, table = {}):
        self.table = table
        self.current = 1

    """
    Adds an element to the table
    """
    def add_element(self, key, value):
        self.table[key] = value

    """
    Removes an element from the table,
    returning True if successful and false if not
    """
    def remove_element(self, key, value):
        if(self.table.pop(key, None) is not None):
            return True
        else:
            return False

    """
    Returns the element from the table or None if not found
    """
    def search(self, key):
        return self.table.get(key, None)

    """
    Updates an element returning True if successful
    and False if not
    """
    def update_element(self, key, new_value):
        if(self.table.get(key, None) is not None):
            self.table[key] = new_value
            return True
        else:
            return False

    def size(self):
        return len(self.table)

    def copy(self):
        return self.table.copy()

    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        if(self.current <= len(self.table)):
            self.current += 1
            return self.table[self.current - 1]
        raise StopIteration

    def __str__(self):
        elements_as_str = ''
        for element in self.table:
            elements_as_str += (str(self.table[element]) + '\n')
        
        return elements_as_str