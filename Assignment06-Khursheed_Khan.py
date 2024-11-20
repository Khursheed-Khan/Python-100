# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Khursheed Khan, Foundations of Programming - Python, Nov 18 2024
#   RRoot,1/1/2030,Created Script
#   First run, Nov 15 2024 at 2pm PST, final run Nov 19 @ 4pm PST.
# ------------------------------------------------------------------------------------------ #

"""
Course Registration Program

This script allows users to register students for courses, view current registrations,
save them to a JSON file, and load data on startup. The program uses exception handling
to manage file operations and input validation to ensure data integrity.

Features:
    - Register students for courses.
    - View all registered students and their courses.
    - Save and load data from a JSON file.

ChangeLog:
    Khursheed Khan, Nov 18 2024, First run
    RRoot, Jan 1 2030, Updated script structure
"""


import json
from json import JSONDecodeError


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments1000.json"
students: list[dict[str,str]] = [] # Set to empty
menu_choice: str = str() # Hold the choice made by the user.

# Define the Data Variables and constants // Taken inside classes and functions
    #student_first_name: str = str()  # Holds the first name of a student entered by the user.
    #student_last_name: str = str()  # Holds the last name of a student entered by the user.
    #course_name: str = str()  # Holds the name of a course entered by the user. // Difference between  str = "" and this?
    #file_obj = None  # Holds a reference to an opened file. Not file but with obj.
    #menu_choice: str = str() # Hold the choice made by the user.
    #student_data: dict[str,str] = {} # Set to empty dictionary # Use it to store one record at a time
    #students: list[dict[str,str]] = [] # Set to empty

# Initiate error handling in case the file is not available, create one

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    Methods:
        read_data_from_file(file_name, student_data):
            Reads student data from a specified JSON file and returns it as a list of dictionaries.
        write_data_to_file(file_name, student_data):
            Writes a list of student dictionaries to a specified JSON file.

    ChangeLog:
        Khursheed Khan, Nov 18 2024, first update
        RRoot, Jan 1 2030, Created Class
    """
    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file

    @staticmethod
    #def read_data_from_file(file_name: str, student_data: list ) -> list[dict]:
    def read_data_from_file(file_name: str, student_data: list[dict[str,str]]):
        """
               Reads student data from a JSON file. If the file doesn't exist or contains invalid JSON, handles errors.

               Args:
                   file_name (str): Name of the file to read from.
                   student_data (list[dict[str, str]]): An initial list of student data.

               Returns:
                   list[dict[str, str]]: Updated list of student data read from the file.
               """

        try:
            with open(FILE_NAME, "r") as file_obj:
                student_data = json.load(file_obj)
                return student_data

        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
            return []
            #except FileNotFoundError:
            #print("File not found, creating it")
        except JSONDecodeError as e:
            IO.output_error_messages("JSON decoding error, resetting file", e)
            return []
        #except JSONDecodeError:
            #print("JSON decoding error, resetting file")
        except Exception as e:
            IO.output_error_messages("There was a non specific error while reading the file", e)
            print("There was an error opening the file")
            print('----Technical Error Message ---')
            print(e,e.__doc__,type(e), sep="\n")
            return []

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list[dict[str,str]]):
        """
        Writes student data to a JSON file.

        Args:
            file_name (str): Name of the file to write to.
            student_data (list[dict[str, str]]): List of student dictionaries to write.

        Returns:
            None
        """

        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file, indent=4)
        except TypeError as e:
                IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
                IO.output_error_messages("There was a non-specific error!", e)

class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    Methods:
        output_error_messages(message, error):
            Displays a custom error message and optionally a technical error message.
        output_menu(menu):
            Displays a formatted menu to the user.
        input_menu_choice():
            Prompts the user to select a menu option and validates the choice.
        input_student_data(student_data):
            Collects student details from the user and adds them to the student data list.
        output_student_courses(student_data):
            Displays the list of registered students and their courses.

    ChangeLog:
        Khursheed Khan, Nov 18 2024, first update
        RRoot, Jan 1 2030, Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays a custom error message to the user.

        Args:
            message (str): A descriptive error message.
            error (Exception, optional): The technical error, if available.

        Returns:
            None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays a menu of choices to the user.

        Args:
            menu (str): The formatted menu string to display.

        Returns:
            None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        Prompts the user to select a menu option.

        Returns:
            str: The user's validated menu choice.
        """
        choice = "0" #Why needed?
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ["1", "2", "3", "4"]:  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message # clarify?
        return choice

    @staticmethod
    def input_student_data(student_data: list[dict[str,str]] = None) -> list[dict[str,str]]:
        """
        Collects student data (first name, last name, course) from the user.

        Args:
            student_data (list[dict[str, str]], optional): Existing student data to update.

        Returns:
            list[dict[str, str]]: Updated list of student data.
        """
        # Ensure student_data is a list
        if student_data is None:
            student_data = []
    # Input data from user
        try:
            # Need to figure out how to use while not sutdent_first_name for this loop....
            # raise ValueError ("Name alphabetic") etc... then in the except below you have to continue somehowe the loop

            while True:  # Keep processing running in this loop
                student_first_name = input("Enter your first name: ").strip()
                if not student_first_name.isalpha():
                #print("First name must be alphabetic, please try again: ")
                    raise ValueError("Alphabetic name required!")
                elif not student_first_name:
                    print("First name is required, it cannot be blank, pls try again: ")
                else:
                    break

            while True:
                student_last_name = input("Enter your last name: ").strip()
                if not student_last_name.isalpha():
                    raise ValueError("Last name must be alphabetic") # This exits the while/ loop ... :(
                #print("Last name must be alphabetic, pls try again: ")
                elif not student_last_name:
                #print("Last name is required, it cannot be blank, pls try again: ")
                    raise ValueError("Alphabetic name rquired!")
                else:
                    break

            while True:
                course_name = input("Please enter the name of the course: ").strip()
                if not course_name:
                    print("Course name is required, it cannot be blank, pls try again: ")
                else:
                    break

        # Create dictionary to store student data
            student = {
                'first_name': student_first_name,
                'last_name': student_last_name,
                'course': course_name
                }

        # Append student data to the students list
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        #except ValueError as error:
        #print(f"Input Error: {error}")
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list[dict[str, str]]):
        """
                Displays the list of registered students and their courses.

                Args:
                    student_data (list[dict[str, str]]): List of student dictionaries to display.

                Returns:
                    None
                """
        if student_data:
            print("Registered Students")
            for student in student_data:
                print(f"{student['first_name']} {student['last_name']} {student['course']}")
        else:
            print("You have not registered yet")

#  End of function definitions

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)

    elif menu_choice == "2": # Display current data
        IO.output_student_courses(student_data=students)

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)

    elif menu_choice == "4":  # End the program
        print("Program ended, thanks")
        break  # out of the while loop

