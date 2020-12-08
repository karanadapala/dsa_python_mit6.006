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