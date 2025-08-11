#task1
marks = { "Alice": 85, "Bob": 90, "Charlie": 76 }
name = input("Enter the student's name: ")

if name in marks:
    student_marks = marks[name]
    print(f"Bob"
          f"{name}'s marks : {student_marks}")
else:
    print(f"Student not found.")

#task2
list=(1,2,3,4,5,6,7,8,9,10)
print("Original list : ",list)
print("Extract First Five Elements:", list[0:5])
print("Reversed Extract Elements:", list[4 ::-1])