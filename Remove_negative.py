#WAP to remove negative numbers from a list
a=eval(input("Enter a list"))
b=[]
for i in a:
    if(i>0):
        b.append(i)
print(b)