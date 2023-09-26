def add(num1, num2):
    result = float(num1) +float(num2)
    print(result)

def subtract(num1,num2):
     result = float(num1) - float(num2)
     print(result)

def multiply(num1,num2):
    result = float(num1) * float(num2)
    print(result)

def divide(num1,num2):
    result = float(num1) / float(num2)
    print(result)

input1 = input ("enter a number")
input2 = input ("enter a number")
inputcalc = input ("enter a calculation")
if inputcalc == "add":
    add (input1, input2)
if inputcalc == "subtract":
    subtract (input1, input2)
if inputcalc =="divide":
    divide (input1, input2)
if inputcalc == "multiply":
    multiply (input1, input2)

