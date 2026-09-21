def file_reader(file_path):
  try:
    with open(file_path,"r") as file:
      content = file.read()
      print(f"Contents of {file_path}:")
      print(content)
  except FileNotFoundError:
    print (f"Error occurred: {file_path} does not exist")
  except PermissionError:
    print (f"Error occurred: no permission to access {file_path}")
  except Exception as e:
    print ("an unexpected error occurred: {e}")

with open("test_document.txt","w") as f:
  f.write("Hi this is a test document for reading files.")

file_reader("test_document.txt")
file_reader("unknown.txt")
