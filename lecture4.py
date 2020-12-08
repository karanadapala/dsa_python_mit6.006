'''
In this lecture version the concept of Heaps is covered.
We will be implementing the following concepts:
i. Max_heapify a.k.a Heapify the ds in descending Tree order.
ii. Extract_max - maximun number from the heap is extract and the rest of the heap is Heapified.
iii. Heap_Sort


A Heap is an array representation of a binary tree, where if element 'x' of the heap 'S' is at 'i' (where i starts from 1 to n), then:
  i. x's parent is at the floor of i/2 (i.e x//2)
 ii. x's left child is at 2^i
iii. x's right child is at 2^1+1

'''
from collections import deque

class Heap():
    def __init__(self, arr: list):
        self.heap = self.heapify(arr)
    '''
    Objectives:
    insert
    extract
    sort 
    '''
    def heapify(self, arr: list):
        def recursiv_swap(self, ind, arr, num):
            if ind == 1 or num < arr[(ind)//2-1]:
                temp = arr[ind-1]
                arr[ind-1] = num
                return temp
            else:
                temp = arr[ind-1]
                arr[ind-1] = recursiv_swap(self, ind//2, arr, num)
                return temp

        for i in range(1, len(arr)+1):
            if arr[(i//2)-1] < arr[i-1]:
                arr[i-1] = recursiv_swap(self, i//2, arr, arr[i-1])
        return arr

    def insert(self, num: int or float):
        return 


ds = Heap([1,2,3,4,5,6,7])
print(ds.heap) # [7, 4, 6, 1, 3, 2, 5]
