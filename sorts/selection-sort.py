class Solution: 
    def selectionSort(self, arr):
        #goal: sort arr on it self, no new list. 

        for i in range(len(arr)):
            min_i = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_i]:
                    min_i = j
            #swap
            arr[i] , arr[min_i] = arr[min_i], arr[i]
        
        return arr