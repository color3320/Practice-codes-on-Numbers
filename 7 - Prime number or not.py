num = int(input("Enter a number - "))
flag = False
if num>1 :
    for i in range(2, num):
        if num%i==0:
            flag = True
            break
elif num == 1:
    print("Invalid")
    
if flag:
    print(num,"is not a prime number")
    print(i,"times",num//i,"is",num)

else:
    print("Prime")
    
    