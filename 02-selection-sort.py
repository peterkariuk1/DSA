def find_smallest(arr):
    smallest = arr[0] # we assume that the smallest element in the list is in the first index of the list
    smallest_index = 0 # we further store its index
    
    for i in range(1,len(arr)): # we start at 1 in the range method to improve efficiency by reducing redudancy
        if arr[i] < smallest:
          smallest = arr[i]  
          smallest_index = i
          
    return smallest_index

print(f"Index of the smallest array element: {find_smallest([3,4,5,6,7,8,12,1,2])}")
    
def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print(f"Unsorted array: {[3,4,5,6,7,8,12,1,2]}")
print(f"Sorted array: {selection_sort([3,4,5,6,7,8,12,1,2])}")