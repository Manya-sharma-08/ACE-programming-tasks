# Student result analyzer Project - medium task 1

import pandas as pd

students = []

# making a user defined function for the grading system

def grade(marks, student):

    if marks >= 90:
        student["grade"] = "A+"
        print("Grade: A+")

    elif marks >= 80:
        student["grade"] = "A"
        print("Grade: A")

    elif marks >= 70:
        student["grade"] = "B"
        print("Grade: B")

    elif marks >= 60:
        student["grade"] = "C"
        print("Grade: C")

    elif marks >= 50:
        student["grade"] = "D"
        print("Grade: D")

    else:
        student["grade"] = "F"
        print("Grade: F")

# making a user defined function for adding students using for loop and while loop for checking critera

def add_students():

    n = int(input("Enter the number of students: "))

    for i in range(n):

        print("\nStudent", i + 1)

        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

       # using while loop because using if statement will still run the rest of the code despite it being wrong
        
        while marks < 0 or marks > 100:

            print("Invalid marks.")
            print("Marks should be between 0 and 100.")

            marks = int(input("Enter marks again: "))

        student = {
            "name": name,
            "marks": marks
        }

        grade(marks, student)

        students.append(student)

        print("Student added successfully.")

 # making user defined function to display the report

def display_report():

    if len(students) == 0:

        print("No student data available.")

    else:

        print("\n-------------------------------------")
        print("       STUDENT RESULT REPORT"         )
        print("-------------------------------------")

        total = 0
        passed = 0
        failed = 0

        high = students[0]
        low = students[0]

        for student in students:

            print("\nName  :", student["name"])
            print("Marks :", student["marks"])
            print("Grade :", student["grade"])

            total = total + student["marks"]

            if student["marks"] > high["marks"]:
                high = student

            if student["marks"] < low["marks"]:
                low = student

            if student["marks"] >= 40:
                passed = passed + 1
            else:
                failed = failed + 1

        avg = total / len(students)
        percentage = (passed / len(students)) * 100

        print("\n------------ SUMMARY ---------------")

        print("Class Average:", round(avg, 2))

        print("Highest Marks:", high["marks"])
        print("Student:", high["name"])

        print("Lowest Marks:", low["marks"])
        print("Student:", low["name"])

        print("Students Passed:", passed)
        print("Students Failed:", failed)

        print("Pass Percentage:", round(percentage, 2), "%")

        print("---------------------------------")

# after making the summary for highest, lowest, passed, failed, pass percentage and average of the class
# making a user defined function to save the report in a csv file using pandas in built function

def save_report():

    report = []

    for student in students:

        report.append({
            "Name": student["name"],
            "Marks": student["marks"],
            "Grade": student["grade"]
        })

    df = pd.DataFrame(report)

    df.to_csv("student_result.csv", index=False)

    print("\nReport saved successfully.")
    print("File name: student_result.csv")


print("-----------------------------------")
print("      STUDENT RESULT ANALYZER      ")
print("-----------------------------------")

#using all the function we made

add_students()

print("\nAll student records have been added.")

print("Generating result report...")

display_report()

print("\nSaving report...")

save_report()

print("\nProgram completed successfully.")

# End of code