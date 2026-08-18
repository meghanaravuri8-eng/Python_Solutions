def check(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return "not a palindrome"
        left+=1
        right-=1
    return "palindrome"
s=input()
print(check(s))
           