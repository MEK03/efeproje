# FIND STUDENTS WHO HAVE PASS THE AVERAGE SCORE
class Student :

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


student1 = Student ("Jack",20,input("Enter the score for first student:"))
student2 = Student ("Jordan",23,input("Enter the score for second student:"))
student3 = Student ("Harry",19,input("Enter the score for third student:"))

avg  = (int(student1.score)+int(student2.score)+int(student3.score)) / 3
print("Average score is : "+str(avg))

if int (student1.score)>avg:
    print(student1.name + ": PASS")
else:
    print(student1.name + ": FAİLED")

if int (student2.score)>avg:
    print(student2.name + ": PASS")
else:
    print(student2.name + ": FAILED")

if int (student3.score)>avg:
    print(student3.name + ": PASS")
else:
    print(student3.name + ": FAILED")

