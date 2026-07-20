
# for i in range(1, 6):
#     name = input(f"enter student{i} name: ")
#     roll_num = input(f"enter roll number of student{i}: ")
#     marks_input = input("enter 5 subject marks separated by spaces: ")
#     marks = [int(x) for x in marks_input.split()]

#     if len(marks) != 5:
#         print("Please enter exactly 5 marks")
#         continue

#     if all(0 <= mark <= 100 for mark in marks):
#         total_marks = sum(marks)
#         percentage = total_marks / 5
#         print(f"Total marks for {name}: {total_marks}")
#         print(f"Percentage for {name}: {percentage:.2f}%")
#     else:
#         print("invalid, ask again")
# if percentage>=90:
#     print("grade A+")
# elif percentage>=80:
#     print("grade A")
# elif percentage>=70:
#     print("grade B")
# elif percentage>60:
#     print("grade c")
# elif percentage>50:
#     print("grade D")
# else:
#     print("fail")

# # -------------------------------
# # Student Management System
# # -------------------------------

students = []
subjects = 5

# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "Fail"
    else:
        return "Fail"

# Input details of 5 students
for i in range(5):

    print("\n==============================")
    print("Enter Details of Student", i + 1)
    print("==============================")

    name = input("Enter Student Name : ")
    roll = input("Enter Roll Number : ")

    marks = []

    # Input marks of 5 subjects
    for j in range(subjects):
        while True:
            mark = int(input(f"Enter marks of Subject {j+1} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid Marks! Please enter marks between 0 and 100.")

    total = sum(marks)
    percentage = total / subjects
    grade = calculate_grade(percentage)

    # Store student record
    student = [
        name,
        roll,
        marks,
        total,
        percentage,
        grade
    ]

    students.append(student)

# -------------------------------
# Display Student List
# -------------------------------

print("\n\n==============================")
print("Students Data (List Format)")
print("==============================")

for student in students:
    print(student)

# -------------------------------
# Student Report
# -------------------------------

print("\n\n===============================================================")
print("{:<15} {:<10} {:<25} {:<8} {:<10} {:<8}".format(
    "Name", "Roll", "Marks", "Total", "Percentage", "Grade"))
print("===============================================================")

for student in students:
    print("{:<15} {:<10} {:<25} {:<8} {:<10.2f} {:<8}".format(
        student[0],
        student[1],
        str(student[2]),
        student[3],
        student[4],
        student[5]
    ))

print("===============================================================")
