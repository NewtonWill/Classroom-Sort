import csv
from student import Student
from classroom import Classroom
import hashTable


def getNumClassrooms() -> int:
    while True:
        try:
            user_input = input("Please enter the number of classrooms: ")
            input_value = int(user_input)
            if input_value <= 2:
                raise ValueError("The number must be greater than 2")
            return input_value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def allowPairing(studentID1, studentID2):
    Student.removeBadPair(studentTable.search(studentID1), studentID2)
    Student.removeBadPair(studentTable.search(studentID2), studentID1)


def disallowPairing(studentID1, studentID2):
    Student.addBadPair(studentTable.search(studentID1), studentID2)
    Student.addBadPair(studentTable.search(studentID2), studentID1)

def addStudentToClass(classroomID, studentID):
    #classTable.search(classroomID).students.append(studentID)
    Classroom.addStudent(classTable.search(classroomID), studentID)

def removeStudentFromClass(classroomID, studentID):
    Classroom.removeStudent(classTable.search(classroomID), studentID)

def goodStudentPairing(studentID1, studentID2):
    if studentID2 in studentTable.search(studentID1).dPairs:
        #print('bad pairing detected')
        return False
    else:
        #print('no bad pairing detected')
        return True
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
        return studentID


def loadClassrooms(nClassrooms):
    classID = 0
    for i in range(nClassrooms):
        print('Classroom ' + str(i) + ' loaded')
        cID = int(classID)
        c = Classroom(i, None)
        classTable.insert(cID, c)
        classID += 1

def sortAlg(nClassrooms, nStudents):
    rejected = list()
    for sID in range(nStudents):
        if placeToClusters(studentTable.search(sID)) is False:
            rejected.append(sID)

    for sID in rejected:
        room_tuples = []
        for c in range(nClassrooms):
            length = len(Classroom.getStudents(classTable.search(c)))
            room_tuples.append((c, length))
        smallToLarge = sorted(room_tuples, key=lambda room: room[1])
        if not attemptSortToSmallest(smallToLarge, sID):
            print("WARNING: Student " + str(studentTable.search(sID)) + " not sorted")

def attemptSortToSmallest(sortedClassTuple, sID):
    for c in sortedClassTuple:
        if goodRoomPairing(c[0], sID):
            addStudentToClass(c[0], sID)
            return True
    return False

def placeToClusters(s):
    if s.rLevel == 'GT':
        if goodRoomPairing(0, s.id):
            addStudentToClass(0, s.id)
            return True
    elif s.dyslexia == 'Yes':
        if goodRoomPairing(1, s.id):
            addStudentToClass(1, s.id)
            return True
    elif s.sped == 'Yes':
        if goodRoomPairing(2, s.id):
            addStudentToClass(2, s.id)
            return True
    return False

def goodRoomPairing(roomID, studentID):
    for i in classTable.search(roomID).students:
        if not goodStudentPairing(i, studentID):
            return False
    return True



studentTable = hashTable.ChainingHashTable(1)
classTable = hashTable.ChainingHashTable(1)

numClassrooms = getNumClassrooms()
numStudents = loadStudentData()
loadClassrooms(numClassrooms)

sortAlg(numClassrooms, numStudents)


for classroom in range(numClassrooms):
    Classroom.printAllStudents(classTable.search(classroom))



# addStudentToClass(0, 80)
# print(classTable.search(0).students)




# print("student 94 bad pairs: ")
# Student.printDPairs(studentTable.search(94), studentTable)
#
# print("student 95 bad pairs: ")
# Student.printDPairs(studentTable.search(95), studentTable)
