def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def division(x, y):
    return x / y

def multiplication(x, y):
    return x * y

print ("Gej mig ett nummer")

number1= input()
number1 = int(number1)

print("gej mig en till nummer")
number2 = input()
number2= int(number2)

print("Vad vill du göra?")
print("1. addition")
print("2. subtraktion")
print("3. division")
print("4. multiplication")

choice = input()
print("Svar")

if choice == "1":
    result = addition(number1, number2)
    print(result)
    

elif choice =="2":
    result = subtraction(number1, number2)
    print(result)

elif choice =="3":
    result = division(number1, number2)
    print(result)

elif choice =="4":
    result = multiplication(number1, number2)
    print(result)


