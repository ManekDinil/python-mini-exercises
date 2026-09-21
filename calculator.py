def calculator(a,b,operation):
  try:
    if operation == 'add':
      return a+b
    elif operation == 'subtract':
      return a-b
    elif operation == 'multiply':
      return a*b
    elif operation == 'divide':
      return a/b
    else:
      return "Invalid operation"
  except ZeroDivisionError as e:
    return "Error: cannot divide by zero!"
  except Exception as e:
    return f"Error: an unexpected error occurred: {e}"

print(calculator(2,0,'divide'))
print(calculator(5,6,'multiply'))