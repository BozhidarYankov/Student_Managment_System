#This is the person class it has attributess name, id, email with provided getters and setters. Setters include validation of
#all of the attributes and finally there is a display_info function which displays the information about the person
class Person:
    """Represents a person with basic information."""

    def __init__(self, name, id, email):
        self._name = name
        self._id = id
        self._email = email

    def get_name(self):
        """Return the name of the person."""
        return self._name

    def get_id(self):
        """Return the id of the person."""
        return self._id

    def get_email(self):
        """Return the email of the person."""
        return self._email

    def set_name(self, name):
        """Set the name of the person."""
        if len(name) == 0:  # If name is empty
            print("You must enter a name")
        elif not name.isalpha():  # If name does not consists only of alphabetic characters
            print("Name must contain only letters")
        elif not name[0].isupper():  # If the first character is not uppercase
            print("Name must start with an uppercase letter")
        else:
            self._name = name

    def set_id(self, person_id):  # person_id because id is a built-in function
        """Set the id of the person."""
        if not person_id.isdigit() or len( person_id) != 9:  # If the string does not contain only digits and is not exactly nine characters
            print("You must enter a valid ID")
        else:
            self._id = person_id

    def set_email(self, email):
        """Set the email of the person."""
        if not email.endswith("@gmail.com") or len(email)==0:  # Check if email endswith @gmail.com and is in lowercase
            print("You must enter a valid email")
        else:
            self._email = email

    def display_info(self):
        """Display the information of the person."""
        return f"Name: {self.get_name()}, ID: {self.get_id()}, Email: {self.get_email()}"