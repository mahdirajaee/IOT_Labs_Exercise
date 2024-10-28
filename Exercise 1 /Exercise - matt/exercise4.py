import datetime as dt 

class student: 
    def __init__(self, name, surname, birthYear, degree):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear
        self.degree = degree 
        self.bachelor = degree == "bachelor" 
        self.master = degree == "master" 


    def vote(self):
        fileContent = open("studentVotes.txt").read() 
        voteList = fileContent.split(",")
        voteList = [int(i) for i in voteList]
        
   

if __name__ == "__main__":
    name = input("Enter the name: ") 
    surname = input("Enter the surname: ")
    birthYear = int(input("Enter the birthyear : "))
    degree = input("Enter the degree: ")
    student1 = student(name, surname, birthYear, degree) 
    print(student1.show()) 
    student1.save()
