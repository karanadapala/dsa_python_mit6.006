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

    