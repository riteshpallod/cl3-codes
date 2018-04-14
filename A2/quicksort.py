import threading
import xml.etree.ElementTree as X
import unittest
import time, random

def partition(array, left, right):
    #first element pivot
    pivot = array[left]
    i = left + 1
    for j in range(left+1, right+1):
        if array[j] < pivot:
            array[j],array[i] = array[i], array[j]
            i += 1
    array[left], array[i-1] = array[i-1], array[left]   
    #print('array:\t\t', array)
    return i-1

def quicksort(array, left, right):
    
    if left <= right:
        print("thead {0} is sorting {1}".format(threading.current_thread(), array[left:right]))
        q = partition(array, left, right)
    
        lthread = None
        rthread = None

        if (left < q-1):
            lthread = threading.Thread(target = lambda: quicksort(array,left,q-1))
            lthread.start()

        if (q+1 < right):
            rthread = threading.Thread(target=lambda: quicksort(array,q+1,right))
            rthread.start()

        if lthread is not None: 
            lthread.join()
        if rthread is not None: 
            rthread.join()

        '''
        thread_1 = threading.Thread(target=quicksort, args=(array, left, q-1))
        thread_2 = threading.Thread(target=quicksort, args=(array, q+1, right))
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()
        '''



root = X.parse("input.xml").getroot()
#print('array: ', root.text)
array = list(map(int, root.text.split()))
print('array: ', array)
quicksort(array,0,len(array)-1)
print(array)


'''
ignore this.
array = []
fi = open("data.txt", "r")
lines = fi.readlines()
count = 0
for line in lines:
    if count > 50000:
        break
    count += 1
    array.append(int(line))

print("numbers count: ", len(array))

for _ in range(100000):
    fi.write(random.randint(1, 1000))

start = time.time()
quicksort(array, 0, len(array)-1)
end = time.time()

print('time needed: ', end-start)
'''
