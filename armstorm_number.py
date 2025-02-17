# Wap to print armstorm numbers from a to b
def check_armstorm(n):
    temp=n
    str_n=str(n)
    l=len(str_n)
    digit_sum=0
    while(temp>0):
        r=temp%10
        p=r**l
        digit_sum+=p
        temp//=10
    if(digit_sum==n):
        return True
    else:
        return False
a=int(input("Enter a value of a"))
b=int(input("Enter a value of b"))
for i in range(a,b+1):
    temp1=check_armstorm(i)
    if(temp1):
        print(i)