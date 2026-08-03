def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        start=arr[i]
        j=i-1
        while j>=0 and arr[j]>start:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=start
arr=[3,2,1]
insertion(arr)
print(arr)