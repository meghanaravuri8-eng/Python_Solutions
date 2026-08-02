arr=list(map(int,input().split()))
target=int(input())
found=-1
for i in range(len(arr)):
    if arr[i]==target:
        found=i
print(found)