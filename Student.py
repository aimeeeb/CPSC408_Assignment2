# Created by Aimee Bowen
# Student ID: 2277842
# Email: bowen126@mail.chapman.edu
# Description: Student object class that stores data for name, gpa, major, and adviser.
# It includes simple GET functions for returning student variables.


class Student:

    def __init__(self, firstName, lastName, gpa, major, adviser):
        self.firstName = firstName
        self.lastName = lastName
        self.gpa = gpa
        self.major = major
        self.adviser = adviser
        self.isDeleted = False

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getMajor(self):
        return self.major

    def getGPA(self):
        return self.gpa

    def getAdviser(self):
        return self.adviser

    def getIsDeleted(self):
        return self.isDeleted

    def getStudent(self):
        return self.getFirstName(), \
               self.getLastName(), \
               self.getGPA(), \
               self.getMajor(), \
               self.getAdviser(), \
               self.getIsDeleted()
