import pandas as pd
import numpy as np


students = pd.DataFrame(columns=['Name', 'RollNo', 'Marks1', 'Marks2'])

def add_student(name, rollno, marks1, marks2):
    global students
    new_student = pd.DataFrame([[name, rollno, marks1, marks2]], columns=['Name', 'RollNo', 'Marks1', 'Marks2'])
    students = pd.concat([students, new_student], ignore_index=True)
    print("Student added successfully.")

def input_student():
    print("Enter student details:")
    name = input("Name: ")
    rollno = int(input("RollNo: "))
    marks1 = float(input("Marks in Subject 1: "))
    marks2 = float(input("Marks in Subject 2: "))
    add_student(name, rollno, marks1, marks2)

def display_all():
    if students.empty:
        print("The student list is empty.")
    else:
        print("Student List:")
        print(students)

def search_student(rollno):
    result = students[students['RollNo'] == rollno]
    if not result.empty:
        print("Student Found:")
        print(result)
    else:
        print("No student found with the given RollNo.")

def delete_student(rollno):
    global students
    if rollno in students['RollNo'].values:
        students = students[students['RollNo'] != rollno]
        print("Student deleted.")
    else:
        print("No student found with the given RollNo.")

def update_rollno(old_rollno, new_rollno):
    global students
    if old_rollno in students['RollNo'].values:
        students.loc[students['RollNo'] == old_rollno, 'RollNo'] = new_rollno
        print("RollNo updated.")
    else:
        print("No student found with the given RollNo.")

def calculate_averages():
    if not students.empty:
        students['Average'] = np.mean(students[['Marks1', 'Marks2']].astype(float), axis=1)
        print("Averages calculated and added to the list.")
        print(students)
    else:
        print("No students to calculate averages.")

def highest_marks():
    if not students.empty:
        max_marks = np.max(students[['Marks1', 'Marks2']].astype(float))
        print("Highest marks across all students:", max_marks)
    else:
        print("No students to find the highest marks.")

def lowest_marks():
    if not students.empty:
        min_marks = np.min(students[['Marks1', 'Marks2']].astype(float))
        print("Lowest marks across all students:", min_marks)
    else:
        print("No students to find the lowest marks.")


while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by RollNo")
    print("4. Delete Student by RollNo")
    print("5. Update RollNo")
    print("6. Calculate Averages")
    print("7. Find Highest Marks")
    print("8. Find Lowest Marks")
    print("9. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        input_student()
    elif choice == 2:
        display_all()
    elif choice == 3:
        rollno = int(input("Enter RollNo to search: "))
        search_student(rollno)
    elif choice == 4:
        rollno = int(input("Enter RollNo to delete: "))
        delete_student(rollno)
    elif choice == 5:
        old_rollno = int(input("Enter old RollNo: "))
        new_rollno = int(input("Enter new RollNo: "))
        update_rollno(old_rollno, new_rollno)
    elif choice == 6:
        calculate_averages()
    elif choice == 7:
        highest_marks()
    elif choice == 8:
        lowest_marks()
    elif choice == 9:
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
