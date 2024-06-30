import csv

#from main import studentTable


# def allowPairing(HashTable, studentID1, studentID2):
#     Student.removeBadPair(Student.getStudent(studentID1, HashTable), studentID2)
#
#
# def disallowPairing(HashTable, studentID1, studentID2):
#     Student.addBadPair(Student.getStudent(studentID1, HashTable), studentID2)


class Student:
    def __init__(self, id, first_name, last_name, rLevel, ethnicity, dyslexia, sped, esl, citizenship):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.rLevel = rLevel
        self.ethnicity = ethnicity
        self.dyslexia = dyslexia
        self.sped = sped
        self.esl = esl
        self.citizenship = citizenship
        self.dPairs = set()  #Disallowed pairings

    def __str__(self):
        return "%s: %s, %s" % (self.id, self.last_name, self.first_name)

    def getStudent(studentID, HashTable):
        return HashTable.search(studentID)

    # def getAlldata(self):
    #     return ""

    def printDPairs(self, HashTable):
        for x in self.dPairs:
            print(Student.getStudent(x, HashTable))

    def addBadPair(student, otherStudentId):
        student.dPairs.add(otherStudentId)

    def removeBadPair(self, otherStudentId):
        self.dPairs.remove(otherStudentId)

