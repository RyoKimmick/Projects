"""
This program is a simple gradebook for a course. It will provide a menu system that allows the user to interact with the gradebook. This includes: 
-Adding a student to the course 
-Adding a grade item to the course 
-Adding students grade to a specified grade item 
-Printing out students grades for each grade item 
-Printing out the class roster 
-Printing out the grades for all students in the class.

Author: Ryo Kimmick
"""
# This class stores the student's first name, last name, and student id
class Student:
    # This method initializes the attributes
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    # This method returns the first name
    def get_first_name(self):
        return self.first_name
    
    # This method returns the last name
    def get_last_name(self):
        return self.last_name

    # This method returns the student id
    def get_student_id(self):
        return self.student_id


# This class will contain the name of the assignment, the total number of points for the assignment, and a dictionary of grades
class GradeItem:
    # This method initializes all the attributes
    def __init__(self, assignment_name, assignment_points):
        self.assignment_name = assignment_name
        self.assignment_points = assignment_points
        self.grades = {}

    # This method returns the assignment's name
    def get_name(self):
        return self.assignment_name
    
    # This method returns the number of points earned on the assignment
    def get_total_points(self):
        return self.assignment_points

    # This method puts the student id (key) and number of points awarded to the assignment (value) into the dictionary
    def add_student_grade(self, student_id, assignment_points):
        self.grades[student_id] = assignment_points
    
    # This method returns the dictionary with the student id's and points
    def get_student_grade(self, student_id):
        return self.grades.get(student_id)


# This class will keep track of and provide access to the information stored in the gradebook
class Course:
    # This method will initialize all the attributes
    def __init__(self):
        self.roster = []
        self.grade_items = []

    # This method adds a student object to the roster list
    def add_student(self, student):
        self.roster.append(student)

    # This method adds a grade item object to the list
    def add_grade_item(self, grade_item):
        self.grade_items.append(grade_item)

    # This method checks to see if the student exists in the roster, then searches for the corresponding GradeItem object to add the student’s grade to the grade item’s dictionary.
    def add_student_grade(self, grade_item_name, student_id, grade):
        # This checks to see if there are objects in the roster. If not, it will raise the custom Empty Roster Error
        if not self.roster:
            raise EmptyRosterError()

        # This creates student variable and assigns it to none, meaning there is no value associated with student
        student = None
        # This searches the roster for a student with the specified student id
        for s in self.roster:
            # If there is a match, the current student object is assigned to student and the loop breaks
            if s.get_student_id() == student_id:
                student = s
                break
        # If the student variable still is none, this will raise the custom Student Not Found Error
        if not student:
            raise StudentNotFoundError(student_id)

        # This creates grade_item variable and assigns it to none, meaning there is no value associated with grade_item
        grade_item = None
        # This searches the grade items roster for an item with the specified name
        for item in self.grade_items:
            # If there is a match, the current grade item object to the grade item variable and the loop breaks
            if item.get_name() == grade_item_name:
                grade_item = item
                break
        # If the grade_item variable is still none, this will raise the custom Grade Item Not Found Error
        if not grade_item:
            raise GradeItemNotFoundError(grade_item_name)

        # This uses the add student grade method from the other class to store the student's grades
        grade_item.add_student_grade(student_id, grade)

    # This method checks to see if the student exists in the roster and then prints out that student’s grades for each grade item in the gradebook. 
    def print_student_grades(self, student_id):
        # If the roster is empty, this will raise the custom Empty Roster Error will
        if not self.roster:
            raise EmptyRosterError()

        # This creates student variable and assigns it to none, meaning there is no value associated with student
        student = None
        # This searches the roster for a student with the specified student id
        for s in self.roster:
            # If there is a match is found, the current student object is assigned to student and the loop breaks
            if s.get_student_id() == student_id:
                student = s
                break
        # If the student variable still is none, this will raise the custom Student Not Found Error
        if not student:
            raise StudentNotFoundError(student_id)

        # This is an empty list for the output of the grades
        grades_output = []
        # This iterates through the grade items list
        for grade_item in self.grade_items:
            # This calls the get_student_grade method, producing either a None variable or an integer
            grade = grade_item.get_student_grade(student_id)
            # If the variable was an integer, this formats the grade name, grade, and total potential points and adds it to the empty string
            if grade is not None:
                grades_output.append(f"{grade_item.get_name()}: {grade} ({grade_item.get_total_points()}) | ")
            # If the variable was None, this formats the grade name, grade, and total potential points and adds it to the empty string. However, it will put N/A for the grade because it does not exist
            else:
                grades_output.append(f"{grade_item.get_name()}: N/A ({grade_item.get_total_points()}) | ")
        # This formats and prints the users last name, first name, student id, grade assignment, grade, and total points
        print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()}) | ", *grades_output)

    # This method prints the roster of students
    def print_roster(self):
        # If the roster is empty, this will raise the custom Empty Roster Error
        if not self.roster:
            raise EmptyRosterError()

        # This prints all the student's last names, first names, and student ids
        print("Course Roster:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()})")

    # This prints the grades for the entire class
    def print_class_grades(self):
        # If the roster is empty, this will raise the custom Empty Roster Error
        if not self.roster:
            raise EmptyRosterError()

    # This will iterate through all students in the roster
        for student in self.roster:
            # This is an empty list for the output of the grades
            grades_output = []
            # This iterates through the grade items list
            for grade_item in self.grade_items:
                # This calls the get_student_grade method, producing either a None variable or an integer
                grade = grade_item.get_student_grade(student.get_student_id())
                # If the variable was an integer, this formats the grade name, grade, and total potential points and adds it to the empty string
                if grade is not None:
                    grades_output.append(f"{grade_item.get_name()}: {grade} ({grade_item.get_total_points()}) | ")
                # If the variable was None, this formats the grade name, grade, and total potential points and adds it to the empty string. However, it will put N/A for the grade because it does not exist
                else:
                    grades_output.append(f"{grade_item.get_name()}: N/A ({grade_item.get_total_points()}) | ")
        # This formats and prints the users last name, first name, student id, grade assignment, grade, and total points
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()}) | ", *grades_output)

# This class is for the customn Empty Roster Error. This will be raised if the roster is empty
class EmptyRosterError(Exception):
    # This method will initialize the attribute
    def __init__(self):
        Exception.__init__("Error: Course Roster is Empty!")

# This class is for the custom Student Not Found Error. This will be raised if the student is not found in the roster
class StudentNotFoundError(Exception):
    # This method will initialize the attribute
    def __init__(self, student_id):
        Exception.__init__(f"Exception: Student ({student_id}) not found.")

# This class is for the custom Grade Item Not Found Error. This will be raised if the grade item is not found
class GradeItemNotFoundError(Exception):
    # This method will initialize the attribute
    def __init__(self, grade_item_name):
        Exception.__init__(f"Exception: Grade Item ({grade_item_name}) not found.")

# This method is what prints to the user
def main():
    course = Course()

    print("Welcome to CSC/DSCI 1301: Principles of CS/DS 1")
    while True:
        print("")
        print("Please choose one of the following options (Enter 'quit' or 'q' to exit):")
        print("1) Add a student.")
        print("2) Add a Grade Item.")
        print("3) Add a student's Grade.")
        print("4) Print a Student's Grades.")
        print("5) Print Course Roster.")
        print("6) Print Class Grades.")
        print("")

        # This gets what the user wishes to do
        choice = input(":> ")
        # If the user enters "quit" or "q", the program will stop
        if choice in ["quit", "q"]:
            break
        
        try:
            # This will run if the user chooses to add a student
            if choice == "1":
                # These will get the first name, last name, and student ID from the user
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                student_id = input("Enter Student ID: ")
                # If the user does not enter digits for the id, the value error will be raised
                if not student_id.isdigit():
                    raise ValueError("Error: Enter a Integer Student ID")
                # This adds the students
                course.add_student(Student(first_name, last_name, int(student_id)))

            # This will run if the user chooses to add a grade item
            elif choice == "2":
                # this gets the grade item and the total points for that item from the user
                name = input("Enter grade item name: ")
                points = input("Enter the total points for the grade item: ")
                # if the user does not enter digits for the points, the value error will be raised
                if not points.isdigit():
                    raise ValueError("Error: Enter numeric Total Points")
                # This adds the grade items
                course.add_grade_item(GradeItem(name, int(points)))

            # This will run if the user chooses to add a student's grade
            elif choice == "3":
                # This gets the grade item, student id, and student grade from the user
                grade_item_name = input("Enter grade item name: ")
                student_id = input("Enter Student ID: ")
                print("")
                grade = input("Enter Student Grade: ")
                # If the user does not enter digits for the student id or grades, the value error will be raised
                if not student_id.isdigit() or not grade.isdigit():
                    raise ValueError("Error: Enter integer values for Student ID and Grade")
                # This adds the student's grades
                course.add_student_grade(grade_item_name, int(student_id), int(grade))

            # This will run if the user chooses to print a student's grades
            elif choice == "4":
                # this gets the student id from the user
                student_id = input("Enter Student ID: ")
                # If the user does not enter digits for the id, the value error will be raised
                if not student_id.isdigit():
                    raise ValueError("Error: Enter a numeric Student ID")
                # this calls the print student grades method and executes it
                course.print_student_grades(int(student_id))

            # this will run if the user wishes to print the course roster
            elif choice == "5":
                # this calls the print roster method and executes it
                course.print_roster()

            # this will run if the user wishes to print the class grades
            elif choice == "6":
                # this calls the print class grades method and executes it
                course.print_class_grades()

        # These will print if any of these errors are raised
        except ValueError as value_error:
            print(value_error)
        except EmptyRosterError as empty_roster_error:
            print(empty_roster_error)
        except StudentNotFoundError as student_not_found_error:
            print(student_not_found_error)
        except GradeItemNotFoundError as grade_item_not_found_error:
            print(grade_item_not_found_error)

if __name__ == "__main__":
    main()