#Define a function to perform the binary search
def binary_search(arr, target):
    #Set the initial bounds of the search
    low = 0
    high = len(arr) - 1
    
    #Keep searching until the bounds converge
    while low<= high:
        #Calculate the middle index
        mid = (low + high) // 2
        
        #check if the middle element is the target
        if arr[mid] == target:
            return mid
        
        #If the target is smaller than the middle element
        #search the left half of the list
        elif target < arr[mid]:
            high = mid - 1
        
        #If the target is larger than the middle element
        #search the right half of the list
        else:
            low = mid + 1
            
        #if the target is not found, return -1
    return  -1
    
def main():
    #create a sorted list of numbers
    numbers = [1,3,5,7,9,11,13,15]
    
    #Prompt the user tp enter a target number
    target = int(input("Enter a number to search for: "))
    
    #Use the binary search function to search for the target in the list 
    result = binary_search(numbers, target)
    
    #Check the result of the  search
    if result == -1:
        print(f"{target} is not in the list.")
    else:
        print(f"{target} is at index {result} in the list.")
        

main()