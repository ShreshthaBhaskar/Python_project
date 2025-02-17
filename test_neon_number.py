def check_neon(n):
    temp=n*n
    sum=0
    while(temp>0):
        r=temp%10
        sum=sum+r
        temp=temp//10
    if(sum==n):
        return True
    else:
        return False
a=int(input("Enter a value of a"))
b=int(input("Enter a value of b"))
for i in range(a,b+1):
    is_neon=check_neon(i)
    if(is_neon):
        print(i)