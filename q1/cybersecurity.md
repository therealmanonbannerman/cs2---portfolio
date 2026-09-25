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
