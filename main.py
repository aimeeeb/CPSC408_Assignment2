# Created by Aimee Bowen
# Student ID: 2277842
# Email: bowen126@mail.chapman.edu
# Description: Main file for editing the student database.
# It includes functions that add, edit, delete, or query students and takes in user inputs to run the functions.

import sqlite3
import pandas as pd
from pandas import DataFrame
from Student import Student

# ESTABLISH DATABASE CONNECTION
conn = sqlite3.connect('assignment2')
c = conn.cursor()

# FUNCTIONS
def printData(queryString, tuple): # FUnction uses DataFrame to print results
    c.execute(queryString, tuple)
    all_rows = c.fetchall()
    df = DataFrame(all_rows, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdviser'])
    if not all_rows:
        print("Student does not exist.")
    else:
        print(df)

def addStudent(stu): # gets Student object and adds it to database
    c.execute("INSERT INTO Student('FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdviser', 'isDeleted')"
              "VALUES (?, ?, ?, ?, ?, ?)", stu.getStudent())
    print("Student added.")
    query = 'SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdviser FROM Student WHERE StudentId = ?'
    studentId = c.lastrowid
    printData(query, (studentId,))

def editStudent(number): # gets 1 or 2 and edits Major or FacultyAdviser, respectively
    if number == 1:
        studentId = input("Enter student's ID: ")
        newMajor = input("Enter new major: ")
        c.execute('UPDATE Student SET Major = ? WHERE StudentId = ?', (newMajor, studentId,))
    elif number == 2:
        studentId = input("Enter student's ID: ")
        newAdviser = input("Enter new adviser: ")
        c.execute('UPDATE Student SET FacultyAdviser = ? WHERE StudentId = ?', (newAdviser, studentId,))
    else:
        print("Invalid input. Operation cancelled.")
        return
    print("Update made.")
    printData('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdviser FROM Student WHERE StudentId = ?', (studentId,))

def searchByMajor(): # asks for Major and prints results
    major = '%' + input("Major: ") + '%'
    query = "SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdviser FROM Student WHERE Major LIKE ?"
    printData(query, (major,))

def searchByGPA(): # asks for GPA and prints results
    gpa = input("GPA: ")
    query = "SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdviser FROM Student WHERE GPA = ?"
    printData(query, (gpa,))

def searchByAdviser(): # asks for FacultyAdviser and prints results
    adviser = '%' + input("Adviser: ") + '%'
    query = "SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdviser FROM Student WHERE FacultyAdviser LIKE ?"
    printData(query, (adviser,))

def searchByWhat(): # decides whether user is searching by Major, GPA, or Adviser and calls proper function
    choice = int(input("Would you like to search by 1. Major, 2. GPA, or 3. Advisor? Input number: "))
    if choice == 1:
        searchByMajor()
    elif choice == 2:
        searchByGPA()
    elif choice == 3:
        searchByAdviser()
    else:
        print("Invalid input. Operation cancelled.")
        return



# LOOP FOR RUNNING ACTIONS
action = 0

while action != 6:
    # print options
    print("\nOptions:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Edit Student's Major or Adviser")
    print("4. Remove Student")
    print("5. Search for Students by Major, GPA, or Advisor")
    print("6. Exit\n")
    # user selection
    action = int(input("What would you like to do? (Type number): "))

    # run actions
    if action == 1:
        # print all students
        printData('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdviser FROM Student WHERE isDeleted = FALSE', ())
    elif action == 2:
        # create student and calls addStudent()
        firstName = input("Student's First Name: ")
        lastName = input("Student's Last Name: ")
        gpa = input("Current GPA: ")
        major = input("Major: ")
        adviser = input("Faculty Adviser: ")
        newStudent = Student(firstName, lastName, gpa, major, adviser)
        addStudent(newStudent)
    elif action == 3:
        # asks for for editing choice and calls editStudent()
        edit = int(input("Input 1 for Major and 2 for Adviser: "))
        editStudent(edit)
    elif action == 4:
        # asks for Id and prints Student
        id = input("Input student ID: ")
        printData('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdviser FROM Student WHERE StudentId = ?', (id,))
        # confirmation before deleting
        confirm = input('Are you sure you want to deleted this student? Y/N: ')
        if confirm.upper() == "Y":
            c.execute('UPDATE Student SET isDeleted = TRUE WHERE StudentId = ?', (id,))
            print("Student deleted.")
        else: # if they input something other than Y, exit
            print("Operation cancelled.")
    elif action == 5:
        # searches using searchByWhat()
        searchByWhat()
    elif action == 6:
        # exits
        print("Thank you, good-bye.")
    else:
        # if input is anything but 1-6, loop starts again
        print("Invalid input, try again.")


# COMMIT CHANGES TO DATABASE
conn.commit()
