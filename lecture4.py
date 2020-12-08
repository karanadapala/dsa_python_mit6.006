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
        self.arr = self.heapify(arr)

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

        for i in range(2, len(arr)+1):
            if arr[(i//2)-1] < arr[i-1]:
                arr[i-1] = recursiv_swap(self, i//2, arr, arr[i-1])
        return arr

    def insert(self, num: int or float):
        self.arr.append(num)
        self.arr = self.heapify(self.arr)
        return

    def extract_max(self):
        if len(self.arr) == 0:
            return 'nothing in heap :('
        maxx = self.arr[0]
        if len(self.arr) > 2:
            if self.arr[1] > self.arr[2]:
                self.arr[0] = self.arr[1]
                self.arr.pop(1)
            else:
                self.arr[0] = self.arr[2]
                self.arr.pop(2)
            self.arr = self.heapify(self.arr)
        elif len(self.arr)==2:
            self.arr = self.arr[1:]
        return maxx

    def sort(self):
        lt = len(self.arr)
        init = 0
        out_arr = []
        while init < lt:
            out_arr.append(self.extract_max())
            init += 1
        self.arr = out_arr # Already in descending order --> no need to Heapify.
        return out_arr

heap = Heap([1,2,3,4,5,6,7])
print(heap.arr) # [7, 4, 6, 1, 3, 2, 5]
heap.insert(8)
print(heap.arr) # [8, 7, 6, 4, 3, 2, 5, 1]
print(heap.extract_max()) # 8
print(heap.arr) # [7, 6, 5, 3, 2, 4, 1]
print(heap.sort()) # [7, 6, 5, 4, 3, 2, 1]
print(heap.arr) # [7, 6, 5, 4, 3, 2, 1]
