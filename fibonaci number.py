n=int(input("enter the number:"))
count=0
n1=0
n2=1
if n<0:
    print("enter postive values")
elif n==0:
    print("enter postive value:")
elif n==1:
    print("entered one:", n1)
elif n==2:
    print("entered 2:", n2)
else:
    print("fibanoci sequence")
    for i in range(n):
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1


