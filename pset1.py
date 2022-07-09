# Given a list of positive integers and the starting integer d, return x such that x is the smallest value greater than
# or equal to d that's not present in the list
def find_first_missing_element(arr, d):
    '''
    Inputs: 
        arr        (list(int)) | List of sorted, unique positive integer order id's
        d          (int)       | Positive integer of smallest possible value in arr
    Output: 
        -          (int)       | The smallest integer greater than or equal to d that's not present in arr
    '''
    
    first = 0
    last = len(arr) - 1
    
    def helper(first, last, d):
        midd = (first + last) // 2
        
        # if the length of the array is 0
        if (len(arr)==0):
            return d
        
        # if the length of the array is 1
        if (first == last):
            if arr[first] == d:
                return d+1
            return d
        
        # missing element in first half
        if (midd - first < arr[midd] - arr[first]):
            return helper(first, midd-1, d)
        
        # missing element in second half
        elif (last - midd < arr[last] - arr[midd]):
            return helper(midd, last, arr[midd])
        
        # missing element on edges
        else:
            if arr[first] == d:
                return arr[last] + 1
            else:
                return d
    
    return helper(first, last, d)
