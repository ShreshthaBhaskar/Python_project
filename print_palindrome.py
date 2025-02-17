#WAP to print palindrome number from a to b
def check_palindrome(n):
   temp=n
   rev=0
   while(temp>0):
     r=temp%10
     rev=rev*10+r
     temp=temp//10
   if(n==rev):
       return True
   else:
       return False
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=[]
for i in range(a,b+1):
    is_palindrome=check_palindrome(i)
    if(is_palindrome):
      c.append(i)
print(c)