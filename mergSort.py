





def splitTheList(listToSplit):
    '''
        Argument : take list to split it to half
        Returns : two lists which is splited
    '''
    if len(listToSplit) > 1:
        return listToSplit[:len(listToSplit)//2], listToSplit[len(listToSplit)//2:]
    else:
        print("one Item List")


def merge(left, right):
    '''
        Argument : take to list to merge them according to ordars
        Returns : one merged List
    '''
    merged = [0] * (len(left)+len(right))
    leftIndexTracker = 0
    rightIndexTracker = 0
    mergedIndexTraker = 0

    while leftIndexTracker < len(left) and rightIndexTracker < len(right):
        if left[leftIndexTracker] < right[rightIndexTracker]:
            merged[mergedIndexTraker] = left[leftIndexTracker]
            leftIndexTracker+=1
        else:
            merged[mergedIndexTraker] = right[rightIndexTracker]
            rightIndexTracker+=1
        
        mergedIndexTraker+=1
    
    while leftIndexTracker < len(left):
        merged[mergedIndexTraker] = left[leftIndexTracker]
        leftIndexTracker+=1
        mergedIndexTraker+=1

    while rightIndexTracker < len(right):
        merged[mergedIndexTraker] = right[rightIndexTracker]
        rightIndexTracker+=1
        mergedIndexTraker+=1
    
    return merged

def merggeSort(listToSort):
    ''' 
        Argument : take list to sort it using mergeSort 
        Returns : Sorted List
    '''
    #Split

    if len(listToSort) == 1:
        return listToSort
    left,right = splitTheList(listToSort)
    print(left,right,sep=" - ")
    left = merggeSort(left)
    right = merggeSort(right)
    return merge(left,right)

if __name__=='__main__':
    print("EveryThing is connected")
    List = [356,79,846,215,1,4,67,8,123,41,1]
    print(merggeSort(List))