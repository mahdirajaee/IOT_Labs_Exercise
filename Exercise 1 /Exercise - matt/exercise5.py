import datetime as dt
import statistics

class Student:
    def __init__(self, name, surname, birth_year, student_status):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.bachelor = student_status.lower() in ['b', 'bachelor']
        self.master = student_status.lower() in ['m', 'master']
        self.votes = []

    def show(self):
        print(f"Hi, I'm {self.name} {self.surname}")

    def age(self):
        print(f'I am {2024 - self.birth_year} years old')

    def save(self):
        with open('student.txt', 'w') as file_2:
            to_write = f'{self.name},{self.surname},{self.birth_year}'
            file_2.write(to_write)
        print('File is already closed... no risk of an open file.')

    def is_bachelor(self):
        if self.bachelor:
            print('The student is a bachelor.')
        else:
            print('The student is not a bachelor.')

    def is_master(self):
        if self.master:
            print('The student is a master.')
        else:
            print('The student is not a master.')

    def read_votes(self, vote_file_name):
        try:
            with open(vote_file_name, 'r') as file:
                file_content = file.read().strip()
                self.votes = [int(vote.strip()) for vote in file_content.split(',') if vote.strip().isdigit()]
            print("Votes loaded successfully:", self.votes)
        except FileNotFoundError:
            print(f"The file '{vote_file_name}' was not found.")
        except ValueError:
            print("There was an error processing the votes in the file.")

    def statistics_votes(self):
        if not self.votes:
            print("No votes to calculate statistics.")
            return
        max_vote = max(self.votes)
        min_vote = min(self.votes)
        average_votes = statistics.mean(self.votes)
        print(f'The maximum vote is {max_vote}')
        print(f'The minimum vote is {min_vote}')
        print(f'The average vote is {average_votes}')

    def as_dictionary(self):
        dictionary_student = {
            "name": self.name,
            "surname": self.surname,
            "birth_year": self.birth_year,
            "bachelor": self.bachelor,
            "master": self.master,
            "votes": self.votes
        }
        print("Student as Dictionary:", dictionary_student)
        return dictionary_student

if __name__ == '__main__':
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    birth_year = int(input('Enter your birth year: '))

    while True:
        student_status = input('Select your level of Education (bachelor, master): ').lower()
        if student_status in ['b', 'bachelor', 'm', 'master']:
            break
        else:
            print('Please enter a valid status.')

    student_a = Student(name, surname, birth_year, student_status)
    student_a.show()
    student_a.age()
    student_a.save()
    student_a.is_bachelor()
    student_a.is_master()

    vote_file_name = input('Enter the name of the file that contains the votes: ')
    student_a.read_votes(vote_file_name)
    student_a.statistics_votes()

    dictionary_student = student_a.as_dictionary()
