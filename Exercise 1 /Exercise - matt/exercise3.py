import datetime as dt 

class student: 
    def __init__(self, name, surname, birthYear, degree):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear
        self.degree = degree 
        self.bachelor = degree == "bachelor" 
        self.master = degree == "master" 


    def get_age(self):
        return dt.datetime.now().year - self.birthYear

    def show(self):
        return f" name is :  {self.name}, and the surname is : {self.surname} and the age is : {self.get_age()}, and the degree is : {self.degree} "
    

    def save(self):
        f = open("student.txt", "a") 
        f.write(f" name is :  {self.name}, and the surname is : {self.surname} and the age is : {self.get_age()}, and the degree is : {self.degree} \n")
    
    def isbachelor(self):
        if self.degree :
            print("This student is a bachelor student")
        else:
            print("This student is not a bachelor student")
        return True 
    
    def ismaster(self):
        if self.degree :
            print("This student is a master student")
        else:
            print("This student is not a master student")
        return True


if __name__ == "__main__":
    name = input("Enter the name: ") 
    surname = input("Enter the surname: ")
    birthYear = int(input("Enter the birthyear : "))
    degree = input("Enter the degree: ")
    student1 = student(name, surname, birthYear, degree) 
    print(student1.show()) 
    student1.save()
