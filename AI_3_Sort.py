def printArr(arr):
    for x in arr:
        print(x)
        print("  ")

def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        flag = False
        for j in range(0, n - i - 1):
            if arr[j+1] < arr[j]:
                flag = True
                arr[j+1] , arr[j] = arr[j] , arr[j+1]
        if not flag:
            break

def mergeSort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        L = arr[:r]
        R = arr[r:]
        mergeSort(L)
        mergeSort(R)
        
        i , j, k = 0, 0 , 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1
        
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1      
            
def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]      

if __name__ == "__main__":
    n = int(input("Enter the size of Array >> "))
    arr = [0] * n
    
    for i in range(n):
        arr[i] = int(input(f"Enter Value for index {i} >> "))
    
    ch = int(input("Choose the Algorithm for Sorting \n1.Bubble Sort \n2.Merge Sort \n3.Selection Sort >> "))

    print("Array before Sorting")
    printArr(arr)

    if ch == 1:
        bubbleSort(arr)        
    elif ch == 2:
        mergeSort(arr)
    elif ch == 3:
        selectionSort(arr)
    
    print("Array after sorting")
    printArr(arr)