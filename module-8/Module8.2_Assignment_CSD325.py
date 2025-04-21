
# Scott Macioce
# Module 8.2 - Student JSON Program
# Purpose: Load, display, update, and save student records using JSON

import json

def print_students(student_list):
    """Print each student in the formatted style."""
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load the existing student list
with open('student.json', 'r') as f:
    students = json.load(f)

# Notify user and display original list
print("Original Student List:")
print_students(students)

# Add a fictional student (your data here)
new_student = {
    "F_Name": "Scott",
    "L_Name": "Macioce",
    "Student_ID": 99999,
    "Email": "scottmacioce@gmail.com"
}
students.append(new_student)

# Notify user and display updated list
print("\nUpdated Student List:")
print_students(students)

# Save updated list back to student.json
with open('student.json', 'w') as f:
    json.dump(students, f, indent=4)

# Notify user file was updated
print("\nThe student.json file has been updated.")
