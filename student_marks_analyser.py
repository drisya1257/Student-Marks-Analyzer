print("============================")
print("Student Marks Analyser")
print("============================")
name = input("Enter student name:")
print("\n===== STUDENT RESULT =====")
print("Student:",name)

subject = ["Maths","Python","Java","Aiml","English"]
marks = []
count = 1
while count <= 5:
    mark = int(input("Enter marks: "))
    if mark >= 0 and mark <= 100:
        marks.append(mark)
        count = count + 1
    else:
        print("Invalid marks. Enter again.")
print("Student:", name)
print("\n--- Marks ---")
print("Maths:", marks[0])
print("Python:", marks[1])
print("Java:", marks[2])
print("AIML:", marks[3])
print("English:", marks[4])
print("Maths:", marks[0], "-", "PASS" if marks[0] >= 40 else "FAIL")
print("Python:", marks[1], "-", "PASS" if marks[1] >= 40 else "FAIL")
print("Java:", marks[2], "-", "PASS" if marks[2] >= 40 else "FAIL")
print("AIML:", marks[3], "-", "PASS" if marks[3] >= 40 else "FAIL")
print("English:", marks[4], "-", "PASS" if marks[4] >= 40 else "FAIL")
total = sum(marks)
print("Total",total)
print("\n--- Result ---")
highest = max(marks)
print("Highest mark:", highest)
lowest = min(marks)
print("Lowest mark :",lowest)
average = total / 5
print("Average:",average)
percentage = (total / 500)*100
print("percentage:",percentage,"%")
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)
if percentage >= 90:
    remark = "Excellent"
elif percentage >= 80:
    remark = "Very Good"
elif percentage >= 70:
    remark = "Good"
elif percentage >= 40:
    remark = "Needs Improvement"
else:
    remark = "Poor"

print("Remark:", remark)

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("Result:", result)
file = open("student_result.txt", "w")

file.write("Student: " + name + "\n")
file.write("Total: " + str(total) + "\n")
file.write("Average: " + str(average) + "\n")
file.write("Percentage: " + str(percentage) + "%\n")
file.write("Grade: " + grade + "\n")
file.write("Result: " + result + "\n")

file.close()

print("Result saved successfully!")
print("\n----- RESULT SUMMARY -----")
print("Student:", name)
print("Total:", total, "/ 500")
print("Average:", average)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)
again = input("Do you want to run again? (yes/no): ")

if again == "yes":
    print("Restart the program.")
else:
    print("Thank you for using Student Marks Analyzer!")



