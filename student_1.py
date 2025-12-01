#The student class inherits from Person and it has two additional attributes major and grades. Both attributes have getters and setters.
#In addition, there are two methods which are crucial for the implementation of polymorphism turn_to_gpa and display_info.
#This class also calculates the average grade of a student.
from person import Person

class Student(Person):
    """Represents a student with basic information."""

    def __init__(self, name, id, email, major, grades):
        super().__init__(name, id, email)
        self._major = major
        self._grades = grades if grades else {}  #Ensures new empty dictionary is created

    def __lt__(self, other):
        """Compares students by gpa then by name"""
        if self.turn_to_gpa() != other.turn_to_gpa():
            return self.turn_to_gpa() < other.turn_to_gpa()
        return self._name < other._name

    def get_major(self):
        """Return the major of the student."""
        return self._major

    def get_grades(self):
        """Return the grades of the student."""
        return self._grades

    def set_major(self, major):
        """Set the major of the student."""
        if len(major) == 0 or not major.isalpha():  # Checks if string is empty or if it contains digits
            print("You must enter a valid major")
        else:
            self._major = major

    def add_course_grade(self, course_name, grade):
        """Add a course grade to the student."""
        if grade < 0 or grade > 100:
            print("You must enter a valid grade")
        else:
            self._grades[course_name] = grade

    def update_grade(self, course_name, updated_grade):
        """Update the grade of the student."""
        if course_name not in self._grades:
            print("Course name not found")
        elif updated_grade < 0 or updated_grade > 100:
            print("You must enter a valid grade")
        else:
            self._grades[course_name] = updated_grade

    def calculate_avg(self):
        """Calculate the average grade of the student."""
        if not self._grades:
            return 0.00
        else:
            return sum(self._grades.values()) / len(self._grades)

    def turn_to_gpa(self):
        """Convert average to GPA."""
        avg = self.calculate_avg()
        if avg < 0 or avg > 100:
            print("Invalid average!")
        else:
            if avg >= 90:
                return 4.00
            elif avg >= 80:
                return 3.00
            elif avg >= 70:
                return 2.00
            elif avg >= 60:
                return 1.00
            else:
                return 0.00

    def display_info(self):
        """Display the information of the student."""
        student_info = super().display_info()
        grades_info = ("\n".join([f" {course}: {grade}" for course, grade in self._grades.items()])
                       or " No courses recorded.")
        return (
            f"{student_info}, Major: {self._major}, Grades:\n{grades_info}\n"
            f"GPA: {self.turn_to_gpa():.2f}"
        )