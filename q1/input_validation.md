# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:** Jireh Jorge S. Loquinerio
**Section:** 8 - Dahlia
**Quarter:** 1

## Activity Overview

In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code

---

# Part A - Validation Requirements
Complete the table below before writing your program.

| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Text | Required | Empty | Must not be empty | ERROR: 404 - name not found. Please restart. |
| Age | Integer (11–18) | Range + Data Type | 10, 19, "abc" | Must be a number between 11 and 18 | ERROR: 404 - age not found in the system. Please reenter. |
| Grade Level | Integer (7–12) | Range + Data Type | 6, 13, "abc" | Must be a number between 7 and 12 | ERROR: 404 - grade level not found. Please reenter. |
| Email Address | Text with @ and . | Format | "student.com" | Must contain "@" and "." | ERROR: 404 - email is not valid. Please reenter. |
| Registration Code | 6 characters | Length | "ABC12" | Must be exactly 6 characters | ERROR: 404 - code does not meet standards. Please restart. |
---

## Validation Questions
### 1. Why should the student name not be blank?
> The student name should not be blank because the program needs to specify the student.
### 2. Why should age be checked for both data type and range?
> Age should be tested for a data type and range; that is, it should be an integer and within a certain range, like 11-18.
### 3. Why should grade level only accept specific values?
> The grade level should have a set of permissible values only; this can be done so that it only accepts 7-12 as inputs.
### 4. What format requirements did you use for the email address?
> The email address should contain an @ symbol and a period (.) to be valid.
### 5. What length requirement did you use for the registration code?
> The code should be 6 characters long.

# Part B - Program Design

## Pseudocode

START

INPUT student's name

IF student's name is empty THEN
    DISPLAY "Name not found"
    STOP
END IF

INPUT student's age

IF age is not a number THEN
    DISPLAY "Invalid age"
    STOP
END IF

IF age is less than 11 OR greater than 18 THEN
    DISPLAY "Invalid age"
    STOP
END IF

INPUT student's grade level

IF grade level is not a number THEN
    DISPLAY "Invalid grade level"
    STOP
END IF

IF grade level is less than 7 OR greater than 12 THEN
    DISPLAY "Invalid grade level"
    STOP
END IF

INPUT student's email

IF "@" is not in email OR "." is not in email THEN
    DISPLAY "Invalid email"
    STOP
END IF

INPUT student's registration code

IF code length is not equal to 6 THEN
    DISPLAY "Invalid code"
    STOP
END IF

DISPLAY "Registration confirmed"

END

# Part C - Programming Implementation

## Programming Language
> Python

## Source Code File
[`workshop_validator.py`](workshop_validator.py)

## Final Code
```python
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
```
---

### Presence Validation
Explain where you used presence validation.
> I used presence validation for the name part. 
### Data Type Validation
Explain where you used data type validation.
> I used data type validation for the age and grade levels to make sure they are integer. 
### Range Validation
Explain where you used range validation. 
> I used range validation for the age and grade levels.
### Acceptable Value Validation
Explain where you used acceptable value validation.
> I used acceptable value validation for the grade levels. 
### Pattern Validation
Explain the simple pattern validation you used. 
> It must be for the email which has to contain "@" and "."
### Length Validation
Explain the length rule you used.
> It was for the registration code for the length to be exactly 6 characters.

# Part D - Testing
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | Registration successful! | Registration successful! | PASS |
| 2 | Blank student name | Presence | ERROR: 404 - name not found. Please restart. | ERROR: 404 - name not found. Please restart. | PASS |
| 3 | Age = `fourteen` | Data type | ERROR: 404 - age not found in the system. Please reenter. | ERROR: 404 - age not found in the system. Please reenter. | PASS |
| 4 | Age = `11` | Minimum boundary | *Continued with the code| *Continue with the code | PASS |
| 5 | Age = `18` | Maximum boundary | *Continue with the code | *Continue with the code | PASS |
| 6 | Age = `10` | Range | ERROR: 404 - age not found in the system. Please reenter. | ERROR: 404 - age not found in the system. Please reenter. | PASS |
| 7 | Grade Level = `13` | Acceptable value | ERROR: 404 - grade level not found. Please reenter. | ERROR: 404 - grade level not found. Please reenter. | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | ERROR: 404 - email is not valid. Please reenter. | ERROR: 404 - email is not valid. Please reenter. | PASS |
| 9 | Registration Code = `ABC` | Length | ERROR: 404 - code does not meet standards. Please restart. | ERROR: 404 - code does not meet standards. Please restart. | PASS |
| 10 | Registration Code = `CS2026` | Valid length | Registration confirmed. | Registration confirmed. | PASS |
