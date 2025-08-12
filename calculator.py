class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b
#*************************************************************************
   
class Scientific(Calculator):
  def power(self):
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent number: "))
    result = 1
    while exponent != 0:
      result *= base
      exponent-=1
    print("Answer = " + str(result))
scientific =Scientific()
scientific.power()
#create a calculator object
my_cl = Calculator()
#***************************************************************************

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: exit")
    
    ch = int(input("Select operation: "))
    
    #Make sure the user have entered the valid choice
    if ch in (1, 2, 3, 4):
        
        #first check whether user want to exit
        if(ch == 4):
            break
        
        #If not then ask fo the input and call appropiate methods        
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if(ch == 1):
            print(a, "+", b, "=", my_cl.add(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", my_cl.subtract(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", my_cl.multiply(a, b))
        elif(ch == 4):
           print(a, "*", b, "=", my_cl.power())


    
    else:
        print("Invalid Input")

