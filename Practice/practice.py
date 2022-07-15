def checkAmstrong(n):
    amg=0
    temp=n
    while n>0:
        amg=amg+pow(n%10,3)
        n=n//10
    print(amg)
    if temp==amg :
        print("It is an amstrong number")
    else:
        print("It is not an amstrong number")
        # return amg
# checkAmstrong(173)
# print(15//10)
sum=0
for i in range(1,101):
    sum=sum+i
# print(sum)

a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)
