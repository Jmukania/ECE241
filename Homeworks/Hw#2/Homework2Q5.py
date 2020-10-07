# Hw#2 Question 5
# Find left most and right most child recursive function

def findLeftMost(list,index):    # Finds leftmost child; Needs array list and index of top parent
    n = len(list)           # Length of array
    l= 2*index + 1          # Current Left child
    nextL = l*2 + 1         # Next left child

    if nextL < n:       # Checks to see if next left child is less than length of array
        index = l       # Make new parent index child and continue
        return findLeftMost(list,index)
    else:               # If next child > length of array, return current left most child
        return l, list[l]

def findRightMost(list,index):  # Finds right most child; Needs array list and index of root parent
    n = len(list)  # Length of array
    r = 2 * index + 2  # Right child
    nextR = r * 2 + 2  # Finds next right child

    if nextR < n:  # Checks to see if right left child is less than length of array
        index = r  # Make new parent index child and continue
        return findRightMost(list, index)
    else:  # If next child > length of array, return current left most child
        return r, list[r]

list = [5,10,9,6,8,3,1,4,2,7]       # Given list
print("Left most child index and value:",findLeftMost(list,0))
print("Right most child index and value:",findRightMost(list,0))