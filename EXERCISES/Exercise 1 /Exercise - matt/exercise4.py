import datetime as dt

class Student:
    def __init__(self, name, surname, birth_year, degree):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.degree = degree.lower()
        self.bachelor = self.degree == "bachelor"
        self.master = self.degree == "master"
        self.votes = []

    def get_age(self):
        return dt.datetime.now().year - self.birth_year

    def show(self):
        return (f"Name: {self.name}, Surname: {self.surname}, "
                f"Age: {self.get_age()}, Degree: {self.degree}")

    def save(self):
        with open("student.txt", "a") as f:
            f.write(f"{self.show()}\n")

    def is_bachelor(self):
        return self.bachelor

    def is_master(self):
        return self.master

    def read_votes(self, filename="studentVotes.txt"):
        try:
            with open(filename) as f:
                file_content = f.read().strip()
                votes_list = file_content.split(',')
                self.votes = [int(vote.strip()) for vote in votes_list if vote.strip().isdigit()]
                print("Votes loaded successfully:", self.votes)
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except ValueError:
            print("There was an error processing the votes in the file.")

    def get_average_vote(self):
        return sum(self.votes) / len(self.votes) if self.votes else 0

    def get_max_vote(self):
        return max(self.votes) if self.votes else None

    def get_min_vote(self):
        return min(self.votes) if self.votes else None

if __name__ == "__main__":
    name = input("Enter the name: ")
    surname = input("Enter the surname: ")
    birth_year = int(input("Enter the birth year: "))
    degree = input("Enter the degree: ")
    
    student1 = Student(name, surname, birth_year, degree)
    print(student1.show())
    student1.save()
    
    # Read votes from file
    student1.read_votes()
    
    # Calculate and print average, max, and min votes
    print("Average Vote:", student1.get_average_vote())
    print("Max Vote:", student1.get_max_vote())
    print("Min Vote:", student1.get_min_vote())
