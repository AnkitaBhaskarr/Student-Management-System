import json

students = {}

# ---------------- FUNCTIONS ---------------- #

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 75:
        return "A"

    elif percentage >= 60:
        return "B"

    elif percentage >= 40:
        return "C"

    else:
        return "FAIL"


def add_student():

    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
        return

    try:

        eng = int(input("Enter English marks: "))
        maths = int(input("Enter Maths marks: "))
        sci = int(input("Enter Science marks: "))

    except ValueError:
        print("Invalid input! Enter numbers only.")
        return

    total = eng + maths + sci
    percentage = total / 3
    grade = calculate_grade(percentage)

    students[name] = {
        "English": eng,
        "Maths": maths,
        "Science": sci,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }

    print(name, "added successfully!")


def view_students():

    if not students:
        print("No students found!")
        return

    print("\n========== STUDENT RECORDS ==========")

    rank = 1

    sorted_students = sorted(
        students.items(),
        key=lambda x: x[1]["Percentage"],
        reverse=True
    )

    for name, data in sorted_students:

        print("\nRank:", rank)
        print("Name:", name)
        print("English:", data["English"])
        print("Maths:", data["Maths"])
        print("Science:", data["Science"])
        print("Total:", data["Total"])
        print("Percentage:", data["Percentage"])
        print("Grade:", data["Grade"])

        rank += 1


def search_student():

    name = input("Enter student name: ")

    if name in students:

        data = students[name]

        print("\nStudent Found")
        print(data)

    else:
        print("Student not found!")


def update_marks():

    name = input("Enter student name: ")

    if name not in students:
        print("Student not found!")
        return

    try:

        eng = int(input("Enter new English marks: "))
        maths = int(input("Enter new Maths marks: "))
        sci = int(input("Enter new Science marks: "))

    except ValueError:
        print("Invalid input!")
        return

    total = eng + maths + sci
    percentage = total / 3
    grade = calculate_grade(percentage)

    students[name] = {
        "English": eng,
        "Maths": maths,
        "Science": sci,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }

    print("Marks updated successfully!")


def delete_student():

    name = input("Enter student name: ")

    if name in students:

        del students[name]

        print("Student deleted!")

    else:
        print("Student not found!")


def check_result():

    name = input("Enter student name: ")

    if name in students:

        data = students[name]

        print("\nRESULT")
        print("Percentage:", data["Percentage"])
        print("Grade:", data["Grade"])

    else:
        print("Student not found!")


def show_topper():

    if not students:
        print("No students found!")
        return

    topper = max(
        students,
        key=lambda x: students[x]["Percentage"]
    )

    print("\nTOPPER")
    print("Name:", topper)
    print("Percentage:", students[topper]["Percentage"])
    print("Grade:", students[topper]["Grade"])


def class_statistics():

    if not students:
        print("No students found!")
        return

    total_students = len(students)

    avg = sum(
        s["Percentage"] for s in students.values()
    ) / total_students

    highest = max(
        s["Percentage"] for s in students.values()
    )

    lowest = min(
        s["Percentage"] for s in students.values()
    )

    print("\nCLASS STATISTICS")
    print("Total Students:", total_students)
    print("Average Percentage:", round(avg, 2))
    print("Highest Percentage:", highest)
    print("Lowest Percentage:", lowest)


def save_data():

    with open("students.json", "w") as file:

        json.dump(students, file)

    print("Data saved successfully!")


def load_data():

    global students

    try:

        with open("students.json", "r") as file:

            students = json.load(file)

    except FileNotFoundError:

        students = {}


# ---------------- MAIN PROGRAM ---------------- #

load_data()

while True:

    print("\n====== STUDENT MANAGEMENT SYSTEM ======")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Check Result")
    print("7. Show Topper")
    print("8. Class Statistics")
    print("9. Save Data")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        check_result()

    elif choice == "7":
        show_topper()

    elif choice == "8":
        class_statistics()

    elif choice == "9":
        save_data()

    elif choice == "10":

        save_data()

        print("Exiting program...")
        break

    else:
        print("Invalid choice!")