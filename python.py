# School Fees Payment System (Console Backend)
# Uses while loops and for loops as required

students = {}  
# Structure:
# students = {
#   "ST001": {
#       "name": "John",
#       "class": "S4",
#       "total_fees": 1500000,
#       "payments": [500000, 300000]
#   }
# }

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    Academic_year = input("Enter Year: ")
    total_fees = int(input("Enter Total Fees (UGX): "))

    students[student_id] = {
        "name": name,
        "class": Academic_year,
        "total_fees": total_fees,
        "payments": []
    }

    print("Student added successfully!\n")


def make_payment():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("❌ Student not found!\n")
        return

    amount = int(input("Enter payment amount (UGX): "))
    students[student_id]["payments"].append(amount)

    print("Payment recorded successfully!\n")


def view_student():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("❌ Student not found!\n")
        return

    student = students[student_id]

    total_paid = 0
    for payment in student["payments"]:   # FOR LOOP
        total_paid += payment

    balance = student["total_fees"] - total_paid

    print("\n--- STUDENT DETAILS ---")
    print("ID:", student_id)
    print("Name:", student["name"])
    print("Class:", student["class"])
    print("Total Fees:", student["total_fees"])
    print("Total Paid:", total_paid)
    print("Outstanding Balance:", balance)
    print("-----------------------\n")


def view_all_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- ALL STUDENTS SUMMARY ---")

    for student_id, student in students.items():   # FOR LOOP
        total_paid = sum(student["payments"])
        balance = student["total_fees"] - total_paid

        print(f"{student_id}  {student['name']}   Paid: {total_paid}   Balance: {balance}")

    print("-----------------------------\n")


# MAIN PROGRAM (WHILE LOOP MUST-USE)
while True:
    print("===== SCHOOL FEES PAYMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Make Payment")
    print("3. View Student Details")
    print("4. View All Students")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        make_payment()
    elif choice == "3":
        view_student()
    elif choice == "4":
        view_all_students()
    elif choice == "5":
        print(" Exiting system. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.\n")
