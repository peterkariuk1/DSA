def binary_search(lst,item):
    # Low and high keep track of which part of the list you'll search in. 
    low = 0
    high = len(lst)-1
    
    # While you haven't narrowed down to one element keep adding low to high.
    while low <= high:
        mid = (low + high) // 2
        guess=lst[mid]
        
    # Now we start searching for the item from here 
    # Here if guess will be strictly equal to the guess we return the mid value in the list   
        if guess == item:
            return(mid)
    
    # Here if the guess is high or low than the mid we add or subtract appropriately till we reach to the item
        elif guess > item: 
            high = mid - 1
            
        else:
            low = mid + 1
        
    return None

# TESTING THE CODE:
my_list = [1,3,4,6,7,9]
print("The terminal should print 1 after this line to display the item's index")
print(binary_search(my_list,3))
print("Successful")
    
    
 # I did this as an exercise   
def my_binary_search(lst2,item2):
    low = 0
    high = len(lst2) - 1
    
    while low <= high:
       mid = (low + high) // 2
       guess = lst2[mid]
       
       if guess == item2:
           return(mid)
       
       elif guess > item2:
           high = mid - 1
           
       else:
           low = mid + 1
        
    return None

print('hello')

list_two = [1,2,3,4,5,6,7,8,9,11,20,34,56,44,13,65,78]

print(my_binary_search(list_two,65))
           
       
        
    
    