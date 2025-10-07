num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
choice=input("Enter choice (+,-,*,/)")

<<<<<<< HEAD
<<<<<<< HEAD
=======
def miltiply (a, b):
    return a * b
=======
def divide (a, b):
    return a / b
>>>>>>> origin/Div

>>>>>>> origin/Mul
if choice=='+':
    print(f"Result:{add(num1,num2)}")
elif choice=='-':
    print(f"Rrsult:{subtract(num1,num2)}")
elif choice=='*':
    print(f"Result:{miltiply(num1,num2)}")
elif choice=='/':
    print(f"Result:{divide(num1,num2)}")
else:
    print("Invalid input")