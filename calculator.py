#function to perform addition
def add(x,y):
    return (x+y)
#function to perform subtraction
def sub(x,y):
    return (x-y)
#function to perform multiplication
def mul(x,y):
    return (x*y)
#function to perform division
def div(x,y):
    return (x/y)
#Main program
while True:
    print("MENU")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")
    user_input=int(input("Enter your choice:"))
    if user_input == 5:
        break
    if user_input not in [1,2,3,4,5]:
        print('Invalid input - please enter a valid operation.')
        continue
    #input for two numbers
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    if user_input == 1:
        print("Result:",add(num1,num2))
    elif user_input == 2:
        print("Result:",sub(num1,num2)) 
    elif user_input == 3:
        print("Result:",mul(num1,num2)) 
    elif user_input == 4:
        print("Result:",div(num1,num2)) 
    '''elif user_input == 5:
        break
    elif user_input not in [1,2,3,4,5]:
        print('Invalid input - please enter a valid operation.')
        continue '''   
    



