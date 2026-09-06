# Get the student's score
student_score = int(input("Enter the student's score (0-100): "))

# Make sure the score is within the valid range
if not 0 <= student_score <= 100:
    print("Invalid Score.")

# Classify the student's performance
elif student_score >= 90:
    print("Outstanding")
elif student_score >= 80:
    print("Very Satisfactory")
elif student_score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")
