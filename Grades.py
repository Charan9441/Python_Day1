
english_marks = input("Enter English marks: ")
math_marks = input("Enter Math marks: ")
science_marks = input("Enter Science marks: ")
social_marks = input("Enter Social marks: ")
second_language = input("Enter Second Language marks: ")
total_marks =   int(english_marks) + int(math_marks) + int(science_marks) + int(social_marks) + int(second_language)
percentage = total_marks / 5
print("Total marks: ", total_marks)
print("Percentage: ", percentage)

if total_marks >450:
    print("Distinction")
elif total_marks >400:
    print("A")
elif total_marks >350:
    print("B")
elif total_marks >270:
    print("C")
else:
    print("Fail")