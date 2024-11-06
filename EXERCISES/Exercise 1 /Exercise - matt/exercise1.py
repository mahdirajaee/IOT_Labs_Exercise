import datetime as dt 

class student: 
    def __init__(self, name, surname, birthYear):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear

    def get_age(self):
        return dt.datetime.now().year - self.birthYear

    def show(self):
        return f" name is :  {self.name}, and the surname is : {self.surname} and the age is : {self.get_age()} "
    
        
    
if __name__ == "__main__":
    name = input("Enter the name: ") 
    surname = input("Enter the surname: ")
    birthYear = int(input("Enter the birthyear : "))
    student1 = student(name, surname, birthYear) 
    print(student1.show()) 
    