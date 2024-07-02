class Classroom:
    def __init__(self, id, students):
        self.id = id
        self.students = list() #contains student ID integers

    def __str__(self):
        return "Classroom #%s" % (self.id)

    def getStudents(self):
        return self.students

    def addStudent(self, student):
        self.students.append(student)

    def removeStudent(self, student):
        self.students.remove(student)