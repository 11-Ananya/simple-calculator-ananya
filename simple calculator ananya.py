a=int(input("enter number"))
b=int(input("enter number"))
choice=input("enter your choice +,-,*,/")
if choice=="+":
    print(a+b)
elif choice=="-":
    print(a-b)
elif choice=="*":
    print(a*b)
elif choice=="/":
    print(a/b)
else:
    print("invalid choice")
