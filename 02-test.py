

def find_smallest(arr):
    # find the smallest value and its index in a given list
    smallest = arr[0] # assume the smallest element is the first element of the list
    smallest_index = 0 # store the index of the smallest element 
    
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        
    return(smallest_index)

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selection_sort([2,5,7,9,1,3]))
