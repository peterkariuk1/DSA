def binary_search(lst,item):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        print(f"Cheecking the middle list item: {mid} and the guess is: {guess}")
        if guess == item:
            return(mid)
        
        elif guess > item:
            high = mid - 1
            
        else:
            low = mid + 1
            
    return None


my_list = [20,29,35,43,56,78,88,89,93]
print(f"The length of the list tested here is: {len(my_list)}")

print(f"Here is the result for the binary search for item 43 in the array: {my_list} => {binary_search(my_list,43)}")
print(binary_search(my_list,29))