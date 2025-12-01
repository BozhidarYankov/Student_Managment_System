# This is the main program it has a load_student_records which loads students from a csv file. After that there are 5
# functions which either sort the students by a given criteria or the student's data is extracted to a JSON file.
# Lastly, there is the menu for the program which includes all of the functions mentioned above and it works until the user decides
# to quit.

import csv
import re
import json
import unittest

from person import Person
from student_1 import Student
from grad_student import GraduateStudent


# Main program


# Load the student.csv file
def load_student_records():
    """Load the student's records from a CSV file."""
    while True:
        file_path = input("Please enter the path to the student data CSV file: ")
        try:
            with open(file_path, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                students = []  # List to store student objects

                for row in reader:
                    # Parse grades dictionary from CSV if it exists
                    grades_dict = {}
                    if "Courses" in row and row["Courses"]:
                        # Allow either ';' or ',' as separators inside the CSV cell
                        course_entries = [entry.strip() for entry in re.split(r"[;,]", row["Courses"]) if entry.strip()]
                        for entry in course_entries:
                            if ":" not in entry:
                                print(f"Invalid course entry '{entry}' for {row['Name']}")
                                continue

                            course, grade = entry.split(":", 1)
                            try:
                                grades_dict[course.strip()] = int(grade.strip())
                            except ValueError:
                                print(f"Invalid grade format for {course} in {row['Name']}")

                    # Determine if graduate student
                    if "ThesisTitle" in row and row["ThesisTitle"]:
                        student = GraduateStudent(
                            row["Name"],
                            row["ID"],
                            row["Email"],
                            row["Major"],
                            row["ThesisTitle"],
                            grades_dict  # Pass the grades dictionary
                        )
                    else:
                        student = Student(
                            row["Name"],
                            row["ID"],
                            row["Email"],
                            row["Major"],
                            grades_dict  # Pass the grades dictionary
                        )

                    students.append(student)  # Add to the list

                print(f"{len(students)} student records loaded successfully.")
                return students, file_path  # Return both students and file_path

        except FileNotFoundError:
            print("Error: File not found. Please enter a valid filename.")
        except Exception as e:
            print(f"Error reading file: {e}. Please try again.")


# Global variable to store original order
original_students_order = None


# 1.option
def list_students(students):
    """Print the student's records."""
    global original_students_order

    print("How would you like to sort the students?")
    print("1. By name")
    print("2. By GPA")
    print("3. By ID")
    print("4. No sorting")

    while True:
        try:
            sort_choice = int(input("Enter a number (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if 1 <= sort_choice <= 4:
            break

        print("Invalid choice. Please enter a number between 1 and 4.")

    if sort_choice == 1:
        students.sort(key=lambda s: s.get_name())
    elif sort_choice == 2:
        students.sort(key=lambda s: s.turn_to_gpa())
    elif sort_choice == 3:
        students.sort(key=lambda s: s.get_id())
    elif sort_choice == 4:
        if original_students_order is not None:
            students[:] = original_students_order

    for student in students:
        print(student.display_info())
        print("-" * 40)


# 2.option
def search_students(students):
    """Search the student's records."""

    while True:
        search_choice = input(
            "Enter a student ID or name (or part of name) to search:").strip()  # If an empty string is entered
        if not search_choice:
            print("No records found. Please enter a student ID or name.")
            continue

        flag = False
        for student in students:
            if search_choice == student.get_id() or search_choice.lower() in student.get_name().lower():  # Searching for the same ID and case-insensitive search for names
                print(student.display_info())
                print("-" * 40)
                flag = True

        if flag:
            break
        else:
            print("No students found matching your search. Please try again.")


# 3.option
def filtering_students(students):
    """Filter the student's records."""
    print("How would you like to filter?")
    print("1. GPA threshold")
    print("2. Major")
    print("3. Courses taken")

    while True:
        try:
            filter_choice = int(input("Enter a number: "))
            if 1 <= filter_choice <= 3:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

    # Filter by GPA
    if filter_choice == 1:
        print("Choose all students with at least ____ GPA")
        while True:
            try:
                gpa_threshold = float(input("Enter a number: "))
                gpa_threshold = round(gpa_threshold, 2)
                if not 0 <= gpa_threshold <= 4:
                    print("Invalid GPA threshold. Please enter a value between 0 and 4.")
                    continue
            except ValueError:
                print("Please enter a numeric GPA.")
                continue

            found = False
            for student in students:
                if student.turn_to_gpa() >= gpa_threshold:
                    print(student.display_info())
                    print("-" * 40)
                    found = True

            if found:
                break
            else:
                print("Sorry, no students found within this GPA treshold.")



    # Filter by major
    elif filter_choice == 2:
        print(" Showing all available majors")

        major_count = 0
        print("Choose a major")
        majors = ["Business", "Computer Science", "Economics", "History", "Journalsim", "Literature", "Mathematics",
                  "Physics", "Philosophy",
                  "Psychology", "Politics"]  # Get all unique majors
        for major in majors:
            major_count += 1
            print(f"{major_count}. {major}")

        while True:  # If no match is found
            major_choice = input("Enter the name of the major: ").strip()

            # Check if empty space is entered
            if not major_choice or major_choice.isdigit():
                print("Invalid input.")
                continue

            found = False
            for student in students:
                if major_choice == student.get_major():
                    print(student.display_info())
                    print("-" * 40)
                    found = True

            if found:
                break
            else:
                print("No students are found with this major")



    # Filtering by Courses taken
    elif filter_choice == 3:
        while True:
            course_name = input("Enter the course name(for ex.:BUS1020): ").strip()
            if not course_name:
                print("Invalid input. Please enter a course name.")
                continue

            found = False

            for student in students:
                if course_name in student.get_grades():
                    print(student.display_info())
                    print("-" * 40)
                    found = True

            if found:
                break

            else:
                print("No students found with that course. Please try again.")


# 4.option
def add_student(students, file_path):
    """Add a student to the list of students."""
    # Enter and validate student name
    student_name = input("Enter student name: ").strip()
    while student_name == "" or student_name.isdigit():
        student_name = input("Please enter a student name: ").strip()

    id_set = set(student.get_id() for student in students)  # Get all unique IDs
    while True:
        student_id = input("Enter student ID: ")

        if not student_id.isdigit() or len(student_id) != 9:
            print("Please enter a valid student ID. ")
            continue
        if student_id in id_set:
            print("Student ID is already in use. Please try again.")
            continue
        break

    # Enter and validate email
    email_set = set(student.get_email() for student in students)
    email_pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|org|edu)"
    while True:
        student_email = input("Enter student email: ")
        if not re.search(email_pattern, student_email):
            print("Invalid email format. Please try again.")
            continue
        if student_email in email_set:
            print("Email already exists. Please enter a different email.")
            continue
        break

    # Enter and validate major
    major_count = 0
    print("Available majors:")
    majors = ["Business", "Computer Science", "Economics", "History", "Journalsim", "Literature", "Mathematics",
              "Physics", "Philosophy",
              "Psychology", "Politics"]  # Get all  majors

    for major in majors:
        major_count += 1
        print(f"{major_count}. {major} ", end='')

    print("\n")
    student_major = input("Enter desired major: ")
    while student_major not in majors:
        student_major = input("Please enter a valid major: ")

    # Determine if the student is graduate
    is_graduate = False
    thesis_title = None
    while True:
        input_thesis_title = input("Is the student graduate? (Y/N): ").strip().lower()
        if input_thesis_title == "y":
            thesis_title = input("Enter thesis title: ")
            is_graduate = True
            break
        elif input_thesis_title == "n":
            break
        else:
            print("Invalid input. Please enter Y or N.")

    # Enter and validate courses and grades
    courses = {}
    course_count = 0
    while True:
        try:
            number_of_courses = int(input("Enter how many courses you want to add: "))
            if number_of_courses > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for course in range(number_of_courses):

        course_count += 1
        print(f"Course {course_count} name ")
        course_name = input("Enter course name: ")
        course_name_pattern = r"[A-Z]{2,3}[0-9]{4}"  # Course name should be at least two uppercase letters coul be be also three. Should be followed by at least 4 digits
        while len(course_name) == 0 or not re.search(course_name_pattern, course_name):
            course_name = input("Please enter a valid course name: ")

        print(f"Course {course_count} grade")
        while True:
            try:
                course_grade = int(input("Enter course grade: "))
                if 0 <= course_grade <= 100:
                    break
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        courses[course_name] = course_grade  # Add course after validation

    print(f"New student {student_name} will be added with {course_count} courses. Confirm? (Y/N).")
    user_choice = input("Enter Y/N: ")

    if user_choice.lower() == "y":  # If user presses Y

        if is_graduate:  # Recognize if student is graduate or not
            new_student = GraduateStudent(student_name, student_id, student_email, student_major, thesis_title,
                                          courses, )
        else:
            new_student = Student(student_name, student_id, student_email, student_major, courses)

        students.append(new_student)

        # Save all students to the CSV file
        with open(file_path, mode="w", newline="") as file:
            fieldnames = ["Name", "ID", "Email", "Major", "ThesisTitle", "Courses"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in students:
                writer.writerow({
                    "Name": student.get_name(),
                    "ID": student.get_id(),
                    "Email": student.get_email(),
                    "Major": student.get_major(),
                    "ThesisTitle": student.get_thesis_title() if isinstance(student, GraduateStudent) else "",
                    "Courses": ";".join(f"{c}:{g}" for c, g in student._grades.items())
                })

        print(f"Student {student_name} added successfully.")
    else:
        print(f"Student {student_name} was discarded.")


# 5.option
def save_students(students):
    """Save the list of students."""
    default_filename = "students.json"
    output_path = input(f"Enter path to save JSON file (default: {default_filename}): ").strip()
    if not output_path:
        output_path = default_filename
    if not output_path.lower().endswith(".json"):
        output_path += ".json"

    try:
        students_information = []
        for student in students:
            student_record = {
                "name": student.get_name(),
                "id": student.get_id(),
                "email": student.get_email(),
                "major": student.get_major(),
                "courses": student.get_grades(),
                "gpa": student.turn_to_gpa()
            }

            if isinstance(student, GraduateStudent):
                student_record["thesis_title"] = student.get_thesis_title()
            else:
                student_record["thesis_title"] = ""

            students_information.append(student_record)

        with open(output_path, "w", encoding="utf-8") as json_file:
            json.dump(students_information, json_file, indent=4)

        print(f"{len(students)} student records saved to {output_path}")
    except IOError as io_err:
        print(f"Failed to write file: {io_err}")
    except Exception as err:
        print(f"Unexpected error while saving: {err}")


# Utility function using tuples
def return_min_max_grade(students):
    """The function returns the minimum and maximum grades."""
    all_grades = []

    # Collect all grades from all students
    for student in students:
        grades = student.get_grades()
        if grades:  # Only add grades if the student has any
            all_grades.extend(grades.values())

    # If no grades found, return None values
    if not all_grades:
        return (None, None)

    # Return tuple of (min_grade, max_grade) - immutable grouping of values
    min_grade = min(all_grades)
    max_grade = max(all_grades)
    return (min_grade, max_grade)


def menu():
    print("Student Record Management - Main Menu")
    print("1. List all students")
    print("2. Search for a student by ID or name")
    print("3. Filter students by criteria")
    print("4. Add a new student record")
    print("5. Save student records to file")
    print("6. Exit")


students, file_path = load_student_records()  # Save student's data and file path
original_students_order = [s for s in students]  # Preserve original order from CSV

user_input = None
while True:
    print()
    menu()
    try:
        user_input = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if not 1 <= user_input <= 6:
        print("Invalid option. Please enter a number between 1 and 6.")
        continue

    if user_input == 1:
        list_students(students)
    elif user_input == 2:
        search_students(students)
    elif user_input == 3:
        filtering_students(students)
    elif user_input == 4:
        add_student(students, file_path)
    elif user_input == 5:
        save_students(students)
    elif user_input == 6:
        confirm = input("Are you sure you want to exit? (Y/N): ")
        if confirm == "Y" or confirm == "y":
            print("Thank you for using this program!")
            break
        else:
            # Don't re-show the menu here — just continue
            continue



