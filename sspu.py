import matplotlib.pyplot as plt 

#student score plotting utility v0.1.2
#delivered by yours truly @anchrone

msgOne = input("I plot student scores!")
peopleLimit = int(input("How many people do you have in class? Please input digits: "))
names  =   []
scores =   []

#listing names and scores

for a in range(0,peopleLimit):
    fName = str(input("Name of the student: "))
    names.append(fName)
    studentScore = int(input("Score of this student: "))
    scores.append(studentScore)

plt.scatter(names,scores)
plt.plot(names,scores)
plt.xlim(-1,peopleLimit)
plt.ylim(0,100)

plt.xlabel("student names")
plt.ylabel("%")
plt.title("Student score plotting utility")
plt.legend()
plt.show()
