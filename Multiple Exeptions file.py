
try:
     num1, num2 =eval(input("Enter two numbers, seprated by a comma:"))
     result = num1 / num2
     print("result is",result)

except ZeroDivisionError:
     print("Error! Division by zero is not allowed.")
except SyntaxError:
      print("Error! Invalid input. Please enter two numbers separated by a comma.")
except:
       print("Wrong input")
else:
       print("No Execptions")
finally:
       print("This will execute no matter what")