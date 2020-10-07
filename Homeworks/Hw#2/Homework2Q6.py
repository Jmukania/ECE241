# Hw#2 question 6
# Three way merge sort
# Make merge sort function that splits into 3 arrays instead of 2


def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:                # Only splits if length >1
        leftmid = len(alist)//3     # Value for first third of array
        rightmid = 2*len(alist)//3    # Value for last third third of array

        # Sections of list
        leftthird = alist[:leftmid]      # Left third
        middle = alist[leftmid:rightmid] # Middle third
        rightthird = alist[rightmid:]     # Right third

        # Will sort each third one by one...
        mergeSort(leftthird)
        mergeSort(middle)
        mergeSort(rightthird)

        # Sorts first, middle, and last third
        i = 0         # Left third tracker
        j = 0         # Middle third tracker
        k = 0         # Right third tracker
        p = 0         # Position of array tracker
        c = 0         # Number of comparisons, incremenent after going through each comparison

        # Checks that every index is valid and compares each possible combinations
        if i < len(leftthird) and j < len(middle) and k < len(rightthird):
            while i < len(leftthird) and j < len(middle) and k < len(rightthird):

                if leftthird[i] >= middle[j] and leftthird[i] >= rightthird[k]:   # If left third > both, put left third value first
                    alist[p] = leftthird[i]
                    i += 1
                elif middle[j] >= leftthird[i] and middle[j] >= rightthird[k]:    # Now if previous skipped, checks middle terms with others
                    alist[p] = middle[j]
                    j += 1
                else:
                    alist[p] = rightthird[k]        # if none are the case, must mean right third is largest
                    k += 1

                p += 1                              # Move position of array forward after comparisons
                c += 1
        # Now has to check values in between the sub-arrays and each possible combinations of those
        # Same concept as previous while except checks in between now just like 2 way merge sort
        # Check and compare left array and middle third array
        if i < len(leftthird) and j < len(middle):
            while i < len(leftthird) and j < len(middle):

                if leftthird[i] >= middle[j]:
                    alist[p] = leftthird[i]
                    i += 1
                else:                           # If not case then opposite must be true
                    alist[p] = middle[j]
                    j += 1
                p += 1                          # Move position of array forward after comparisons
                c += 1
        # Same concept now check left and right third
        if i < len(leftthird) and k < len(rightthird):
            while i < len(leftthird) and k < len(middle):
                if leftthird[i] >= rightthird[k]:
                    alist[p] = leftthird[i]
                    i += 1
                else:  # If not case then opposite must be true
                    alist[p] = rightthird[k]
                    k += 1
                p += 1                          # Move position of array forward after comparisons
                c += 1
        # Lastly... Now check middle and last ( every combination)
        # Same as Mergesort with 2, except use three different arrays
        if j < len(middle) and k < len(rightthird):
            while j < len(middle) and k < len(middle):
                if middle[j] >= rightthird[k]:
                    alist[p] = middle[j]
                    j += 1
                else:  # If not case then opposite must be true
                    alist[p] = rightthird[k]
                    k += 1
                p += 1                         # Move position of array forward after comparisons
                c += 1
        # Checks for values of sub-arrays that have not been used
        # and fills in remaining values into  array
        # Case where left third has values not already added and add it to array
        if i < len(leftthird):
            while i < len(leftthird):
                alist[p]=leftthird[i]
                i += 1
                p += 1          # Move position of array forward after comparisons

        # Case where middle third has values not already added and add it to array
        if j < len(middle):
            while j < len(middle):
                alist[p]=middle[j]
                j += 1
                p += 1      # Move position of array forward after comparisons
        # Case where left third has values not already added
        if k < len(rightthird):
            while k < len(rightthird):
                alist[p]=rightthird[k]
                k += 1
                p += 1      # Move position of array forward after comparisons

    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

