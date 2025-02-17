#WAP to print neon numbers from a to b with the help of list
def check_neon(n):
    temp=n*n
    sum_digit=0
    while(temp>0):
        r=temp%10
        sum_digit+=r # sum_digit=sum_digit+r
        temp//=10 # temp=temp//10
    if(sum_digit==n):
        return True
    else:
        return False

a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
for i in range(a,b+1):
    isNeon=check_neon(i)
    if(isNeon):
        print(i)