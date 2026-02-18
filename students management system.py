students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added ✅")

def view_students():
    if not students:
        print("No students found ❌")
    else:
        for roll, data in students.items():
            print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")

def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted ✅")
    else:
        print("Student not found ❌")

def menu():
    while True:
        print("\n1.Add 2.View 3.Delete 4.Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()
