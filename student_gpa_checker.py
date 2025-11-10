# Author: Fallon Skeens
# Filename: student_gpa_checker.py
# Description: Repeatedly accepts student last name, first name, and GPA.
#   Stops when last name 'ZZZ' is entered.
#   Prints whether they made the Dean's List or the Honor Roll.


def main():
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name.upper() == "ZZZ":
            print("Program ended.")
            break

        first_name = input("Enter student's first name: ")

        gpa = input("Enter student's GPA: ")
        while True:
            try:
                gpa = float(gpa)
                break
            except ValueError:
                gpa = input("Invalid. Please enter a valid GPA (example; 3.5): ")

        made_any = False
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
            made_any = True
        if gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
            made_any = True
        if not made_any:
            print(f"{first_name} {last_name} has not made the Dean's List or Honor Roll.")
        print("-" * 40)

if __name__ == "__main__":
    main()
