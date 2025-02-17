#WAP to check weather a string contains any special character or not
a=input("Write a sentence")
check=False
for i in a:
    if i in '!@#$%^&*?':
        check=True
        break
if(check):
    print('yes')
else:
    print('no')



# n=6
# list=[4,-4,3,-5,-1,2]
# output
# step1-> 4    ->count->1
# step2 ->-4
# step3 ->3(7) ->count->2
# step4->-5(2) ->count->3
# step5-> -1(1) -> count->4
# step6->2(3) -> count ->5
# output -> 5