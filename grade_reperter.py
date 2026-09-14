# Part A: Grade Reporter
scores = [72, 45, 88, 93, 61, 77, 49, 80, 55]

total = 0
passed = 0

for score in scores:
    total = total + score
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Score: {score} -> Grade: {grade}")
    
    if score >= 50:
        passed = passed + 1

average = total / len(scores)
print(f"\nTotal scores: {len(scores)}")
print(f"Passed: {passed}")
print(f"Average: {average:.2f}")
