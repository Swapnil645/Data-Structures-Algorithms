class sorting:
    def __init__(self,data):
        self.data_list = data
    
    def buble_sort(self):
        '''Time complexity is more'''
        data = self.data_list
        for __ in enumerate(data):
            for ind in range(len(data)-1):
                if data[ind]>data[ind+1]:
                    data[ind],data[ind+1] = data[ind+1],data[ind]
        return data




    def merge_sort(self,data):
        '''Fastest sort'''
        if len(data)<=1:
            return data
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        leftsorted,rightsorted = self.merge_sort(left),self.merge_sort(right)
        sorted = self.merge(leftsorted,rightsorted)
        return sorted

    def merge(self,left,right):
        i,j=0,0
        merged = []
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                merged.append(left[i])
                i=i+1
            else:
                merged.append(right[j])
                j=j+1

        merged = merged + left[i:]
        merged = merged + right[j:]

        return merged




test0 = {'input':{'nums':[4, 2, 6, 3, 4, 6, 2, 1]},'output':[1,2,2,3,4,4,6]}
test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}
test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

test5 = {
    'input': {
        'nums': []
    },
    'output': []
}

test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

import random
#   from jovian.pythondsa import evaluate_test_cases

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}


data = [test0,test1,test2,test3,test4,test5,test6,test7]
for  ele in data:
    obj = sorting(ele['input']['nums']).buble_sort()
    print(obj)

print('merge sort')
for  ele in data:
    obj = sorting(ele['input']['nums']).merge_sort(ele['input']['nums'])
    print(obj)



