def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)
arr=[5,7,2,0]
bubble(arr)