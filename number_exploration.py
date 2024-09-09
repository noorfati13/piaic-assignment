name=input("Enter your name:")
n1=int(input("Enter your first favorite number:"))
n2=int(input("Enter your second favorite number:"))
n3=int(input("Enter your third favorite number:"))
print("Hello,",name,"! Let's explore your favorite numbers:")
if (n1 % 2 == 0):
    print("The number" ,n1 ,"is an even number")
else:
    print("The number" ,n1 ,"is an odd number")     
if (n2 % 2 == 0):
    print("The number" ,n2 ,"is an even number")
else:
    print("The number" ,n2 ,"is an odd number")     
if (n3 % 2 == 1):
    print("The number" ,n3 ,"is an odd number")   
else: 
     print("The number" ,n3 ,"is an even number")                 
print("The number",n1,"and its square:",(n1,n1*n1))
print("The number",n2,"and its square:",(n2,n2*n2))
print("The number",n3,"and its square:",(n3,n3*n3))
summ=n1+n2+n3
print("Amazing! The sum of your favorite numbers is:", summ)

if (summ % 2 == 1 or summ % 3 == 0):
   print("Wow,",summ,"is a prime number!") 
else:
    print("Wow,",summ,"is a composite number")   


        
