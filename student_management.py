
students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found:", student)
            return

    print("Student not found.")


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
