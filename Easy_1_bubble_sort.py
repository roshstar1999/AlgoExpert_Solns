def bubbleSort(array):
    length = len(array)
    isSorted=False
    while not isSorted:
        isSorted=True
        for i in range (length-1):
            
            if(array[i]>array[i+1]):
                t=array[i]
                array[i]=array[i+1]
                array[i+1]=t
                isSorted=False
        length-=1
    return array
                
    
#array = [2,3,4,5,6,7,5]
#print(bubbleSort(array)) 
