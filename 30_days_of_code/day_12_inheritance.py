class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        self.letters = ['O', 'E', 'A', 'P', 'D', 'T']
        self.avarages = [100, 90, 80, 70, 55, 40, 0]
        self.grade = sum(self.scores) / len(self.scores)
        for i in range(len(self.avarages) - 1):
            if self.avarages[i+1] <= self.grade <= self.avarages[i]:
                return self.letters[i]
            
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
