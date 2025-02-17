def prime_number(n):
    if(n==1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
for i in range(a,b+1):
    is_prime=prime_number(i)
    if(is_prime):
      print(i)