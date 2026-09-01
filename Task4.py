#1. taking input of a filename from user
filename=input("Enter the Filename: ")

#2. Trying to open and read the file
try:
    with open (filename, 'r') as file:
        lines=file.readlines()

#3. Handling FileNotFoundError and PermissionError
except FileNotFoundError:
    print("Error: File Not Found!")

except PermissionError:
    print("Error: Permission Denied!")

#4. If successfully opened, printing the first 3 lines
else:
    print("First 3 Lines of the File: ")
    for line in lines[:3]:
        print(line.strip())

#5. Finally priting "File Operation Attempted"
finally:
    print("File Operation Attempted!")