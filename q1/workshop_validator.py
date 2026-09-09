students_name = str(input("Enter your name: ")) 

if not students_name:
    print("ERROR: 404 - name not found. Please restart.")
    quit()


try:
    students_age = int(input("Enter your age: "))

    if students_age < 11 or students_age > 18:
        print("ERROR: 404 - age not found in the system. Please reenter.")
        quit()

except ValueError:
    print("ERROR: 404 - age not found in the system. Please reenter.")
    quit()


try:
    students_grade_level = int(input("Enter your grade level: "))

    if students_grade_level < 7 or students_grade_level > 12:
        print("ERROR: 404 - grade level not found. Please reenter.")
        quit()

except ValueError:
    print("ERROR: 404 - grade level not found. Please reenter.")
    quit()


students_email = input("Enter your corporate email: ")

if "@" not in students_email or "." not in students_email:
    print("ERROR: 404 - email is not valid. Please reenter.")
    quit()


students_regiscode = input("Enter your code: ")

if len(students_regiscode) != 6:
    print("ERROR: 404 - code does not meet standards. Please restart.")
    quit()

print("Registration confirmed.")
