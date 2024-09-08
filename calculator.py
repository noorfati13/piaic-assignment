#Calculator
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print("Enter\n1 for Add\n2 for Subtract\n3 for Multiply\n4 for divide")
choice=int(input("Enter your choice:"))
if choice == 1:
    print(n1+n2)
elif choice == 2:
    print(n1-n2)
elif choice == 3:
    print(n1*n2)
elif choice == 4:
    print(n1/n2)
else:
    print("Try Again")    