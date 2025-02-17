# WAP to find sum of squares of first n natural numbers
def Square(n):
    return n*n
n=int(input('enter value of n'))
sum=0
for i in range(1,n+1):
    temp=Square(i)
    sum+=temp
print(sum)
print('kkkk')
