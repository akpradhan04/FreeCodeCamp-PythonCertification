class HashTable:
    
    def __init__(self):
        self.collection = dict()

    def hash(self, string):
        total = 0
        for letter in string:
            total += ord(str(letter))
        return total

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.new_dic = dict()
            self.new_dic[key] = value
            self.collection[hash_value] = self.new_dic
        else:
            (self.collection[hash_value])[key] = value 
        return self.collection

    def remove(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection and len(self.collection[hash_value]) == 1 and key in self.collection[hash_value]:
            del (self.collection[hash_value])
        elif hash_value in self.collection and len(self.collection[hash_value]) > 1 and key in self.collection[hash_value]:
            del (self.collection[hash_value])[key]



    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        else:
            return


# h1 = HashTable()
# print(h1.add('cfc', 'hello'))
# # print(h1.add('fcc', 'sir'))
# # print(h1.add('abi', 'mygod'))
# h1.remove('ddd')
# # print(h1.lookup('cfc'))
# # print(h1.lookup('hero'))
