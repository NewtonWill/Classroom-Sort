import csv
from student import Student
from classroom import Classroom
import hashTable


def getNumClassrooms() -> int:
    while True:
        try:
            user_input = input("Please enter the number of classrooms: ")
            input_value = int(user_input)
            if input_value <= 0:
                raise ValueError("The number must be greater than 0")
            return input_value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def allowPairing(studentID1, studentID2):
    Student.removeBadPair(studentTable.search(studentID1), studentID2)
    Student.removeBadPair(studentTable.search(studentID2), studentID1)


def disallowPairing(studentID1, studentID2):
    Student.addBadPair(studentTable.search(studentID1), studentID2)
    Student.addBadPair(studentTable.search(studentID2), studentID1)


def loadStudentData():
    #Function used to load students from csv into memory
    with open('students.csv') as studentList:
        studentData = csv.reader(studentList, delimiter=',')
        next(studentData)  # skip header
        studentID = 0
        for attribute in studentData:
            sID = int(studentID)
            lastname = attribute[0]
            firstname = attribute[1]
            ethnicity = attribute[2]
            dyslexia = attribute[3]
            rLevel = attribute[4]
            sped = attribute[5]
            eslLevel = attribute[6]
            bGrade = attribute[7]

            # student object
            s = Student(sID, firstname, lastname, rLevel, ethnicity, dyslexia, sped, eslLevel, bGrade)
            #print(s)

            # insert it into the hash table
            studentTable.insert(sID, s)
            studentID = studentID + 1


def loadClassrooms():
    classID = 0
    for i in range(numClassrooms):
        print('Classroom ' + str(i) + ' loaded')
        cID = int(classID)
        c = Classroom(i, None)
        classTable.insert(cID, c)
        classID += 1


studentTable = hashTable.ChainingHashTable(1)
classTable = hashTable.ChainingHashTable(1)
numClassrooms = getNumClassrooms()
loadStudentData()
loadClassrooms()


classTable.search(0).students.append(80)
print(classTable.search(0).students)





# print(studentTable.search(94))
# print(studentTable.search(95))
# print(studentTable.search(96))


# disallowPairing(94, 95)
#
# print("student 94 bad pairs: ")
# Student.printDPairs(studentTable.search(94), studentTable)
#
# print("student 95 bad pairs: ")
# Student.printDPairs(studentTable.search(95), studentTable)
