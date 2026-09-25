# Fundamentals of Cybersecurity and Data Privacy

**Activity:** PSHS Secure Club Registration System  
**Name:** Jireh Loquinerio  
**Section:** Dahlia  
**Quarter:** 1

---

## Activity Overview

In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple PSHS Club Registration System.

The goal is to create a program that collects only necessary information and accepts only correct, expected, and appropriate input.

---

# Part A - Cybersecurity Threat Analysis

## Assigned Case

**Case Number:** Case 1  
**Case Title:** Fake Login Alert

> A message claims that the student's account will be disabled and asks them to click a link and enter their username and password.

---

### 1. What cybersecurity threat is shown?

The threat is **phishing**. 

### 2. What warning signs make the situation suspicious?

The message says the account will be disabled, which can pressure the student to act quickly.

### 3. What may be affected?

- Data
- Account
- Application
- Device
- Network

The student's account and personal information could be compromised if they enter their login details into a fake website. The link could also lead to an unsafe website or download.

### 4. What information could be exposed or misused?

The student's username and password could be stolen. If the attacker gets access to the account, other information connected to it could also be accessed.

### 5. What should the user do to reduce the risk?

The student should not click the link and enter their username or password. They should verify the message with the school or report it as suspicious.

### 6. What mitigation can reduce the risk?

Students can reduce the risk by learning how to recognize phishing messages, checking links carefully, and using multi-factor authentication when available.

# Part B - Data Privacy and Secure Data Capture

A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.

| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | **Collect** | In order to identify the student being registered. |
| Section | **Collect** | In order to know what class the student goes to. |
| Club Choice | **Collect** | In order to know what club the student is being registered to. |
| School Email | **Collect** | In order for easier contact and communication with the student. |
| Attendance Status | **Collect** | In order to record whether the student is present, absent, or late. |
| Password | **Do Not Collect** | A password is not needed for a club registration. |
| OTP | **Do Not Collect** | An OTP is not needed because it does not need account verification. |
| Home Address | **Do Not Collect** | A student's home address is not needed for club registration. |
| Parent Bank Account | **Do Not Collect** | Banking information is unrelated to registering for a school club. |

---

## Privacy Question

### Why is it safer to collect only information that the program actually needs?

It is safer because it collects less personal information which could be used against them. It also protects the students privacy and doesn't give unneccessary information.

# Part C - Security-Focused Validation Rules

Complete the validation rules before writing the program.

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | A student's name | Missing student information | Blank | Must not be blank | ERROR 404: Student name is blank. |
| Section | An allowed section | Incorrect section information | Unknown Section | Must match an allowed section | ERROR 404: Enter a valid section. |
| Club Choice | Arab Adab, ACS, APC, Sports Club, English Club, Dance Troupe, Danza, Chorale, Rondalla, Polaris, Sigma, Earth Savers, Iskolarts, Pisay-MUN, Bahaynayan, Agham Radio Club | Invalid club registration | Danza | Must match one of the allowed clubs | ERROR 404: Enter a valid club. |
| School Email | School email containing `@` and `.` | Incorrect email information | studentpshs.edu.ph | Must contain `@` and `.` | ERROR 404: Enter a valid school email. |
| Attendance Status | Present, Absent, Late | Incorrect attendance record | Maybe | Must match one of the allowed statuses | ERROR 404: Enter a valid attendance status. |

---

## Secure Data Capture Questions

### 1. What should your program accept?

The program should be able to process a complete and valid student information that must adhere to the provided guidelines.

### 2. What should your program reject?

The program should reject blanks, invalid sections, unavailable clubs, invalid email format, and invalid attendance status.

### 3. How do your validation rules help reduce incorrect or unsafe input?

Validation rules can help ensure that the program only accepts appropriate and expected information. They can help prevent the entry of missing, incorrect, and unwanted information.

---
# Part D - Secure Program Implementation
## Program
Create a simple **PSHS Club Registration System**.
The program should collect only:
- Student Name
- Section
- Club Choice
- School Email

- Attendance Status
It should **not request passwords, OTPs, banking information, or unnecessary personal information**.
---
## Source Code File
[`secure_registration.py`](secure_registration.py)
---
## Final Code
```python
name = input("Enter your name: ")

if name == "":
    print("ERROR 404: Student name is blank.")
else:
    section = input("Enter your section: ")

    if section != "Dahlia" and section != "Ilang-Ilang" and section != "Rosal" and section != "Sampaguita":
        print("ERROR 404: Enter a valid section.")
    else:
        club = input("Enter your club: ")

        if club != "Arab Adab" and club != "ACS" and club != "APC" and club != "Sports Club" and club != "English Club" and club != "Polaris" and club != "Dance Troupe" and club != "Danza" and club != "Chorale" and club != "Rondalla" and club != "Sigma" and club != "Earth Savers" and club != "Iskolarts" and club != "Pisay-MUN" and club != "Bahaynayan" and club != "Agham Radio Club":
            print("ERROR 404: Enter a valid club.")
        else:
            email = input("Enter your corporate email: ")

            if "@" not in email or "." not in email:
                print("ERROR 404: Enter a valid school email.")
            else:
                attendance = input("Enter attendance status:  ")

                if attendance != "Present" and attendance != "Absent" and attendance != "Late":
                    print("ERROR 404: Enter a valid attendance status.")
                else:
                    print("--------------------------------")
                    print("REGISTRATION COMPLETE")
                    print("--------------------------------")
                    print("Student:", name)
                    print("Section:", section)
                    print("Club:", club)
                    print("Email:", email)
                    print("Attendance:", attendance)
```
---
## Security Practices Applied
### Required Input
> The code was designed to detect if the value was blank to determine if it was an invalid or valid input.
### Allowed Values
> The section, club and attendance.
### Format Check
> The code checked if the input had an "@" or "." to determine if the output approved or not.
### Error Messages
> To determine if the input was validated ot invalidated
### Data Minimization
> The program only collects information needed for club registration. It does not ask for passwords, OTPs, home addresses, or banking information because these are unnecessary for the activity.


