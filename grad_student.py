#Graduate student inherits from Student and has an additional attribute thesis_title, provided with getters and setters.
#As mentioned here turn_to_gpa and display_info are overriden, demonstrating polymrphism.
from student_1 import Student

class GraduateStudent(Student):
    """Represents a graduate student."""

    def __init__(self, name, id, email, major, thesis_title, grades):
        super().__init__(name, id, email, major, grades)
        self._thesis_title = thesis_title

    def get_thesis_title(self):
        """Return the thesis title of the graduate student."""
        return self._thesis_title

    def set_thesis_title(self, thesis_title):
        """Set the thesis title of the graduate student."""
        if len(thesis_title) == 0 or not thesis_title.isalpha():  # Check if thesis title is empty and if it has any digits
            print("You must enter a thesis title")
        else:
            self._thesis_title = thesis_title

    def turn_to_gpa(self):
        """Convert average to GPA."""
        avg = self.calculate_avg()
        if avg < 0 or avg > 100:
            print("Invalid average!")
        else:
            if avg >= 96:
                return 4.00
            elif avg >= 90:
                return 3.67
            elif avg >= 86:
                return 3.30
            elif avg >= 83:
                return 3.00
            elif avg >= 80:
                return 2.67
            elif avg >= 76:
                return 2.30
            elif avg >= 73:
                return 2.00
            elif avg >= 70:
                return 1.67
            elif avg >= 65:
                return 1.33
            elif avg >= 60:
                return 1.00
            else:
                return 0.00

    def display_info(self):
        """Display the information of the graduate student."""
        graduate_student_info = super().display_info()
        return f"{graduate_student_info}\nResearch Topic: {self._thesis_title}"