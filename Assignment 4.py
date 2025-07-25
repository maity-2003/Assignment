#task 1
try:
    file = open('sample.txt', 'r')
    reading_file = file.read()
    print("Reading file content :\n", reading_file )
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

#task 2
def file_operations():
    file_name = "output.txt"


    user_data = input("Enter data to write to the file: ")
    with open(file_name, "w") as file:
        file.write(user_data + "\n")
    print(f"Data successfully written to '{file_name}'.")


    user_data1 = input("Enter additional text to append: ")

    with open(file_name, "a") as file:
        file.write( user_data1 + "\n")
    print(f" Data successfully appended .")


    print(f"\n--- Final content of ' {file_name} '.")
    try:
     with open(file_name, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

file_operations()