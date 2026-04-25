#student grade tracker
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def is_passing(self):
        return self.get_average() >= 60

    def display_report(self):
        avg = self.get_average()
        status = "Passing" if self.is_passing() else "Failing"

        print("Student:", self.name)
        print("ID:", self.student_id)
        print("Grades:", self.grades)
        print("Average:", round(avg, 2))
        print("Status:", status)


# Test
s = Student("Alice", "S001")
s.add_grade(85)
s.add_grade(90)
s.add_grade(78)

s.display_report()