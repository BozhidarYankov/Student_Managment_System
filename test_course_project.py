#Here are all of the unit tests for every class that is provided.
import unittest
from course_project import Person, Student, GraduateStudent


class TestPerson(unittest.TestCase):
    """Test the Person class."""

    def setUp(self):
        """Set up the tests."""
        self.person = Person("Ivan", "123456789", "ivan@gmail.com")

    def test_get_name(self):
        """Test the get_name method."""
        self.assertEqual(self.person.get_name(), "Ivan")

    def test_get_id(self):
        """Test the get_id method."""
        self.assertEqual(self.person.get_id(), "123456789")

    def test_get_email(self):
        """Test the get_email method."""
        self.assertEqual(self.person.get_email(), "ivan@gmail.com")

    def test_set_name(self):
        """Test the set_name method."""
        self.person.set_name("Ivan")
        self.assertEqual(self.person.get_name(), "Ivan")

    def test_set_name_empty(self):
        """Test the set_name_ method when empty."""
        original_name = self.person.get_name()#Check for empty name
        self.person.set_name("")
        self.assertEqual(self.person.get_name(), original_name)

    def test_set_name_digits(self):
        """Test the set_name method with digits."""
        original_name = self.person.get_name()
        self.person.set_name("123456789")
        self.assertEqual(self.person.get_name(), original_name)

    def test_set_name_lowercase(self):
        """Test the set_name method when the first letter is lowercase."""
        original_name = self.person.get_name()
        self.person.set_name("ivan")
        self.assertEqual(self.person.get_name(), original_name)


    def test_set_id(self):
        """Test the set_id method."""
        self.person.set_id("123456789")
        self.assertEqual(self.person.get_id(), "123456789")

    def test_set_id_empty(self):
        """Test the set_id method when empty."""
        original_id = self.person.get_id()#Check for empty id
        self.person.set_id("")
        self.assertEqual(self.person.get_id(), original_id)

    def test_set_id_alphabetic(self):
        """Test the set_id method with alphabetic."""
        original_id = self.person.get_id()
        self.person.set_id("IVV1234")
        self.assertEqual(self.person.get_id(), original_id)

    def test_set_email(self):
        """Test the set_email method."""
        self.person.set_email("ivan@gmail.com")
        self.assertEqual(self.person.get_email(), "ivan@gmail.com")

    def test_set_email_empty(self):
        """Test the set_email method when empty."""
        original_email = self.person.get_email()#Check for empty email
        self.person.set_email("")
        self.assertEqual(self.person.get_email(), original_email)

    def test_set_email_without_gmail(self):
        """Test the set_email method when it doesn't end with @gmail."""
        original_email = self.person.get_email()
        self.person.set_email("ivan@gmail.www")
        self.assertEqual(self.person.get_email(), original_email)

    def test_display_info(self):
        """Test the display_info method."""
        expected = "Name: Ivan, ID: 123456789, Email: ivan@gmail.com"
        self.assertEqual(self.person.display_info(), expected)


class TestStudent(unittest.TestCase):
    """Test the Student class."""

    def setUp(self):
        """Set up the tests."""
        self.student = Student("John", "123456789", "john@gmail.com", "ComputerScience", {"COS3040": 95, "MAT2020": 88})
        self.student_no_grades = Student("Jane", "987654321", "jane@gmail.com", "Mathematics", {})

    def test_get_major(self):
        """Test the get_major method."""
        self.assertEqual(self.student.get_major(), "ComputerScience")

    def test_get_grades(self):
        """Test the get_grades method."""
        expected_grades = {"COS3040": 95, "MAT2020": 88}
        self.assertEqual(self.student.get_grades(), expected_grades)

    def test_set_major_valid(self):
        """Test set_major with valid input."""
        self.student.set_major("Physics")
        self.assertEqual(self.student.get_major(), "Physics")



    def test_set_major_empty(self):
        """Test set_major with empty string."""
        original_major = self.student.get_major()
        self.student.set_major("")
        self.assertEqual(self.student.get_major(), original_major)

    def test_set_major_invalid_with_digits(self):
        """Test set_major with digits."""
        original_major = self.student.get_major()
        self.student.set_major("CS123")
        # Major should not change if invalid
        self.assertEqual(self.student.get_major(), original_major)

    def test_add_course_grade_valid(self):
        """Test add_course_grade with valid grade."""
        self.student.add_course_grade("PHY1010", 92)
        self.assertEqual(self.student.get_grades()["PHY1010"], 92)

    def test_add_course_grade_invalid_negative(self):
        """Test add_course_grade with negative grade."""
        initial_grades = self.student.get_grades().copy()
        self.student.add_course_grade("PHY1010", -5)
        # Grade should not be added if invalid
        self.assertNotIn("PHY1010", self.student.get_grades())
        self.assertEqual(self.student.get_grades(), initial_grades)

    def test_add_course_grade_invalid_too_high(self):
        """Test add_course_grade with grade over 100."""
        initial_grades = self.student.get_grades().copy()
        self.student.add_course_grade("PHY1010", 105)
        # Grade should not be added if invalid
        self.assertNotIn("PHY1010", self.student.get_grades())
        self.assertEqual(self.student.get_grades(), initial_grades)

    def test_update_grade_valid(self):
        """Test update_grade with valid input."""
        self.student.update_grade("COS3040", 98)
        self.assertEqual(self.student.get_grades()["COS3040"], 98)

    def test_update_grade_course_not_found(self):
        """Test update_grade with non-existent course."""
        initial_grades = self.student.get_grades().copy()
        self.student.update_grade("NONEXISTENT", 90)
        # Grades should not change
        self.assertEqual(self.student.get_grades(), initial_grades)

    def test_update_grade_invalid_negative(self):
        """Test update_grade with negative grade."""
        original_grade = self.student.get_grades()["COS3040"]
        self.student.update_grade("COS3040", -10)
        # Grade should not change if invalid
        self.assertEqual(self.student.get_grades()["COS3040"], original_grade)

    def test_calculate_avg_with_grades(self):
        """Test calculate_avg with existing grades."""
        # (95 + 88) / 2 = 91.5
        self.assertEqual(self.student.calculate_avg(), 91.5)

    def test_calculate_avg_no_grades(self):
        """Test calculate_avg with no grades."""
        self.assertEqual(self.student_no_grades.calculate_avg(), 0.00)

    def test_turn_to_gpa_4_0(self):
        """Test turn_to_gpa for 4.0 GPA (avg >= 90)."""
        # Student with avg 91.5 should get 4.0
        self.assertEqual(self.student.turn_to_gpa(), 4.00)

    def test_turn_to_gpa_3_0(self):
        """Test turn_to_gpa for 3.0 GPA (avg >= 80 and < 90)."""
        student = Student("Test", "111111111", "test@gmail.com", "CS", {"COS3040": 85})
        self.assertEqual(student.turn_to_gpa(), 3.00)

    def test_turn_to_gpa_2_0(self):
        """Test turn_to_gpa for 2.0 GPA (avg >= 70 and < 80)."""
        student = Student("Test", "111111111", "test@gmail.com", "CS", {"COS3040": 75})
        self.assertEqual(student.turn_to_gpa(), 2.00)

    def test_turn_to_gpa_1_0(self):
        """Test turn_to_gpa for 1.0 GPA (avg >= 60 and < 70)."""
        student = Student("Test", "111111111", "test@gmail.com", "CS", {"COS3040": 65})
        self.assertEqual(student.turn_to_gpa(), 1.00)

    def test_turn_to_gpa_0_0(self):
        """Test turn_to_gpa for 0.0 GPA (avg < 60)."""
        student = Student("Test", "111111111", "test@gmail.com", "CS", {"COS3040": 50})
        self.assertEqual(student.turn_to_gpa(), 0.00)

    def test_turn_to_gpa_no_grades(self):
        """Test turn_to_gpa with no grades."""
        self.assertEqual(self.student_no_grades.turn_to_gpa(), 0.00)

    def test_lt_operator_by_gpa(self):
        """Test __lt__ operator comparing by GPA."""
        student1 = Student("Alice", "111111111", "alice@gmail.com", "CS", {"COS3040": 95})
        student2 = Student("Bob", "222222222", "bob@gmail.com", "CS", {"COS3040": 85})
        # student1 has higher GPA, so student2 < student1 should be True
        self.assertTrue(student2 < student1)
        self.assertFalse(student1 < student2)

    def test_lt_operator_by_name_when_gpa_equal(self):
        """Test __lt__ operator comparing by name when GPA is equal."""
        student1 = Student("Alice", "111111111", "alice@gmail.com", "CS", {"COS3040": 90})
        student2 = Student("Bob", "222222222", "bob@gmail.com", "CS", {"COS3040": 90})
        # Same GPA, so compare by name: "Alice" < "Bob" should be True
        self.assertTrue(student1 < student2)
        self.assertFalse(student2 < student1)

    def test_display_info(self):
        """Test display_info method."""
        info = self.student.display_info()
        self.assertIn("John", info)
        self.assertIn("123456789", info)
        self.assertIn("john@gmail.com", info)
        self.assertIn("ComputerScience", info)
        self.assertIn("COS3040", info)
        self.assertIn("95", info)
        self.assertIn("GPA", info)

    def test_display_info_no_grades(self):
        """Test display_info with no grades."""
        info = self.student_no_grades.display_info()
        self.assertIn("Jane", info)
        self.assertIn("No courses recorded", info)
        self.assertIn("GPA", info)


class TestGraduateStudent(unittest.TestCase):
    def setUp(self):
     self.grad_student = GraduateStudent("John", "123456789", "john@gmail.com", "ComputerScience","AI programming" ,{"COS3040": 95, "MAT2020": 88})

    def test_get_thesis_title(self):
        """Test get_thesis_title method."""
        self.assertEqual(self.grad_student.get_thesis_title(), "AI programming")

    def test_set_thesis_title_empty(self):
        """Test set_thesis_title method when thesis title is empty."""
        original_title = self.grad_student.get_thesis_title()
        self.grad_student.set_thesis_title("")
        self.assertEqual(self.grad_student.get_thesis_title(), original_title)

    def test_set_thesis_title_digits(self):
        """Test set_thesis_title method when thesis title contains digits."""
        original_title = self.grad_student.get_thesis_title()
        self.grad_student.set_thesis_title("AI programming 1")
        self.assertEqual(self.grad_student.get_thesis_title(), original_title)

    def test_turn_to_gpa_4_0(self):
        """Test turn_to_gpa method for 4.0 GPA."""
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming",{"COS3040": 96})
        self.assertEqual(graduateStudent.turn_to_gpa(), 4.0)

    def test_turn_to_gpa_3_6_7(self):
        """Test turn_to_gpa method for 3.67 GPA."""
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming",{"COS3040": 90})
        self.assertEqual(graduateStudent.turn_to_gpa(), 3.67)

    def test_turn_to_gpa_3_3(self):
        """Test turn_to_gpa method for 3.3 GPA."""
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming",{"COS3040": 86})
        self.assertEqual(graduateStudent.turn_to_gpa(), 3.30)

    def test_turn_to_gpa_3(self):
        """Test turn_to_gpa method for 3.00 GPA."""
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming",{"COS3040": 83})
        self.assertEqual(graduateStudent.turn_to_gpa(), 3.00)

    def test_turn_to_gpa_2_6_7(self):
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming",{"COS3040": 80})
        self.assertEqual(graduateStudent.turn_to_gpa(), 2.67)

    def test_turn_to_gpa_2_3(self):
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming", {"COS3040": 76})
        self.assertEqual(graduateStudent.turn_to_gpa(), 2.30)

    def test_turn_to_gpa_2_0(self):
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming", {"COS3040": 73})
        self.assertEqual(graduateStudent.turn_to_gpa(), 2.00)

    def test_turn_to_gpa_1_6_7(self):
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming", {"COS3040": 70})
        self.assertEqual(graduateStudent.turn_to_gpa(), 1.67)

    def test_turn_to_gpa_1_3_3(self):
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming", {"COS3040": 65})
        self.assertEqual(graduateStudent.turn_to_gpa(), 1.33)

    def test_turn_to_gpa_1_0(self):
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming", {"COS3040": 60})
        self.assertEqual(graduateStudent.turn_to_gpa(), 1.00)

    def test_turn_to_gpa_0_0(self):
        graduateStudent = GraduateStudent("Test", "111111111", "test@gmail.com", "CS", "AI programming", {"COS3040": 40})
        self.assertEqual(graduateStudent.turn_to_gpa(), 0.00)

    def test_display_info(self):
        info = self.grad_student.display_info()
        self.assertIn("John", info)
        self.assertIn("123456789", info)
        self.assertIn("john@gmail.com", info)
        self.assertIn("ComputerScience", info)
        self.assertIn("AI programming", info)
        self.assertIn("COS3040", info)
        self.assertIn("95", info)
        self.assertIn("MAT2020", info)
        self.assertIn("88", info)
        self.assertIn("GPA", info)




if __name__ == "__main__":
    unittest.main()