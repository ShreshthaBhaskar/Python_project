#WAP to find sum of positive numbers and product of negative numbers in a list
a=eval(input("Enter a list"))
b=[]
sum=0
mul=1
for i in a:
    if(i>0):
        sum=sum+i
    else:
        mul=mul*i
print(sum)
print(mul)