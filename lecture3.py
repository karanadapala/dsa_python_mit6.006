'''
In this lecture version of insertion sort and merge sort were covered.
Optimized version of insertion sort would use binary search to swap the numbers.
'''

class Lecture3():
    def __init__(self, arr):
        self.arr = arr

    def insertion_sort_basic(self):
        def recursion_swap(self, ind, min_num):
            if ind == -1 or self.arr[ind]<min_num:
                return min_num
            else:
                max_num = self.arr[ind]
                self.arr[ind] = recursion_swap(self, ind-1, min_num)
                return max_num

        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                self.arr[i] = recursion_swap(self, i-1, self.arr[i])
        # worst case time complexity O(n^2), space Complexity O(n^2)
        return

    def insertion_sort_Optimized(self):
        def binary_search(self, arr, low, high, x): 
            if high >= low: 
                mid = (high + low) // 2
                if mid == 0 and x < arr[mid]:
                    return 0

                elif arr[mid] < x < arr[mid+1]: 
                    return mid+1

                elif low+1 == high-1 and arr[low] < x < arr[high-1]: 
                        return high-1

                elif arr[mid] > x: 
                    return binary_search(self, arr, low, mid - 1, x) 
        
                elif arr[mid] < x: 
                    return binary_search(self, arr, mid + 2, high, x) 

        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                temp = self.arr[i]
                temp_ind = i
                next_ind = binary_search(self, self.arr, 0, i, temp)
                while  temp_ind != next_ind:
                    self.arr[temp_ind] = self.arr[temp_ind-1]
                    temp_ind -= 1
                self.arr[next_ind] = temp
        # worst case time complexity O(n^2), space Complexity O(nlogn)
        return


my_list = Lecture3([4,1,3,5,6,2])
print(my_list.arr)
my_list.insertion_sort_basic()
print(my_list.arr)
my_list2 = Lecture3([4,1,3,5,6,2])
my_list2.insertion_sort_Optimized()
print(my_list2.arr)
