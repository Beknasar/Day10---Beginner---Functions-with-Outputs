from art import logo
print(logo)

#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-":subtract,
  "*": multiply,
  "/": divide,
}

num1 = int(input("What's the first number?: "))

for operation in operations:
  print(f"{operation}")
operation_symbol = input("Pick an operator from the line above: ")
num2 = int(input("What's the second number?: "))
#selecting an operation by symbol in the dictionary of operations 
calculation_function = operations[operation_symbol]
#calculating num1 and num2
answer = calculation_function(num1, num2)
#output
print(f"{num1} {operation_symbol} {num2} = {answer}")
