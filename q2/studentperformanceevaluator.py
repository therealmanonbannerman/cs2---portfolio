def calculate_average(score1, score2, score3):
  return (score1 + score2 + score3) / 3

def get_performance(average):
  if average >= 85:
    return ("Mastery")
  elif average >= 70:
    return ("Developing")
  else:
    return ("Needs Review")

def is_eligible(average, tasks):
  return average >= 85 and tasks >= 3

score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: ")) 
score3 = float(input("Enter the final score: "))
tasks = int(input("Enter the number of completed tasks: "))

average = calculate_average(score1, score2, score3)
performance = get_performance(average)
eligibility = is_eligible(average, tasks)

print("The average of the student: ", round(average, 2))
print("The performance of the student: ", performance)
print("The eligibility of the student: ", eligibility)

# Documentation Questions
# 1. The calculate_average is the one that returns a number, get_performance is the one that returns a string, and is_eligible is the one that returns a Boolean.
# 2. The variable average starts in calculate_average in which it uses the variable average to store the defined function. It is then passed to the get_performance as a parameter to determine the status of the student. 
# 3. The eligibility will show "False" because the Boolean requires both the average to be equal or higher than 85 and the tasks completed equal or higher than 3. Both conditions must be met for the Boolean to show "True".
# 4. The "return" is more appropriate because print only displays the final value of the program while return can be used to for storing the given info in a variable and it allows for the functions given information to be used in a much later part of the code, exactly what we did in this code. 
