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

    def merge_sort(self):
        def recursion(self, arr):
            if len(arr) == 1:
                return arr
            elif len(arr) == 2:
                if arr[0]<arr[1]:
                    return arr
                else:
                    return [arr[1],arr[0]]
            left_split = recursion(self, arr[:len(arr)//2])
            right_split = recursion(self, arr[len(arr)//2:])
            out_arr = []
            l_pointer = 0
            r_pointer = 0
            while l_pointer<len(left_split) and r_pointer < len(right_split):
                if left_split[l_pointer] < right_split[r_pointer]:
                    out_arr.append(left_split[l_pointer])
                    l_pointer += 1
                else:
                    out_arr.append(right_split[r_pointer])
                    r_pointer += 1
                if l_pointer == len(left_split):
                    for i in range(r_pointer,len(right_split)):
                        out_arr.append(right_split[i])
                    r_pointer = len(right_split)
                if r_pointer == len(right_split):
                    for j in range(l_pointer, len(left_split)):
                        out_arr.append(left_split[j])
                    l_pointer = len(left_split)
            return out_arr
        arr = self.arr
        sorted_arr = recursion(self, arr)
        self.arr = sorted_arr
        return
        

my_list = Lecture3([4,1,3,5,6,2])
print(my_list.arr)
my_list.insertion_sort_basic()
print(my_list.arr)
my_list2 = Lecture3([4,1,3,5,6,2])
my_list2.insertion_sort_Optimized()
print(my_list2.arr)
my_list3 = Lecture3([4,1,3,5,6,2])
my_list3.insertion_sort_Optimized()
print(my_list3.arr)