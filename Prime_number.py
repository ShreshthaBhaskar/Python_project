#WAP to print prime number a to b
def prime_number(n):
    if(n==1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
a=int(input("Enter a value of a"))
b=int(input('Enter a value of b'))
c=[]
for i in range(a,b+1):
    is_prime=prime_number(i)
    if(is_prime):
      c.append(i)
print(c)