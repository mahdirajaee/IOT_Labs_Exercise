import time

class student: 
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age 


    def birthYear(self):
        return 2024 - self.age

    def show(self):
        return f" name is :  {self.name}, and the surname is : {self.surname} and the age is : {self.age} "
    
        