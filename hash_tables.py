'''Collision Handling also included'''

'''Implementation of Dictionary internally''' 



class HashTable:
    def __init__(self, max_hash_table_size):
        self.data_list = [None] * max_hash_table_size

    def insert(self,key,value):
        ind = self.get_valid_ind(key)
        self.data_list[ind] = (key, value)
        
       
    def find(self,key):
        #kv = self.data_list[self.get_hash_ind(key)]
        '''Find the value with respective key'''
        ind = self.get_hash_ind(key)
        if self.data_list[ind] is None:
            return None
        else:
            while True:
                k,v = self.data_list[ind]
                if k == key:
                    return k,v
                ind=ind+1

    def update(self, key, value):
        ind = self.get_hash_ind(key)
        if self.data_list[ind] is None:
            return None
        else:
            while True:
                '''Update the key value on matching key'''
                k,v = self.data_list[ind]
                if k == key:
                    self.data_list[ind] = key,value
                    break
                ind=ind+1
        #self.data_list[self.get_hash_ind(key)] = key,value


    def listall(self):
        [print('key and value :', ele) for ele in self.data_list if ele]
        
                

    def get_hash_ind(self,key):
        num=0
        '''ord gives the integer value of a character and functions returns the index value'''
        for c in key:
            num = num + ord(c)        
        return num % len(self.data_list)
        

    def get_valid_ind(self, key):
        '''FUctions used to detect collision and remove it'''
        ind = self.get_hash_ind(key)
        while True:
            if self.data_list[ind] is None:
                return ind
            else:
                '''if collision is detected i.e. same key or key with same but jumbled characters is found then ind is incremented by one.'''
                k,v = self.data_list[ind]
                if self.data_list[ind] is None:
                    return ind
                if k == key:
                    return ind
                ind =ind+1
                if ind == len(self.data_list):
                    ind=0


    

obj = HashTable(4096)
obj.insert('Akash',6453537)
obj.insert('ketki',26352635)
obj.insert('tekki',11111)
obj.listall()
print(obj.find('Akash'))
print(obj.update('Akash',4343434))
print(obj.find('Akash'))

print(obj.find('tekki'))
print(obj.find('ketki'))
obj.update('ketki',999999)

print(obj.find('tekki'))
print(obj.find('ketki'))