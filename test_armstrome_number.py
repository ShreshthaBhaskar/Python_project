def check_armstrome(n):
    temp=n
    str_n=str(n)
    l=len(str_n)
    sum=0
    while(temp>0):
        r=temp%10
        p=r**l
        sum=sum+p
        temp//=10
    if(sum==n):
        return True
    else:
        return False
a=int(input("Enter a value of a"))
b=int(input("Enter a value of b"))
for i in range(a,b+1):
    is_armstrome=check_armstrome(i)
    if(is_armstrome):
        print(i)