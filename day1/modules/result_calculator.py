# TODO
# Create a function called calculate_percentage()

# It should :
# 1. Accept three marks
# 2. Calculate the total
# 3. Calculate the percentage
# 4. Return the percentage

# TODO
def calculate_percentage(marks_sub1, marks_sub2, marks_sub3):
    total=(marks_sub1+marks_sub2+marks_sub3)
    percentage=(total/300)*100
    return percentage

def calculate_grade(percentage):
    grade=None
    if percentage>=80:
       grade="A"
    elif percentage>=60:
        grade="B"
    elif percentage>=40:
        grade="C"
    else:
        print("D")

    return grade
if __name__=="__main__":
    print("\n -- Result --")
    student_info=input_student()
    print("Student:",student_info["name"])
    percentage=calculate_percentage(
        student_info["python_marks"],
        student_info["math_marks"],
        student_info["comm_marks"])
    print("Percentage", calculate_percentage(
        student_info["python_marks"],
        student_info["math_marks"],
        student_info["comm_marks"]))
    print(f"Grade: {calculate_grade(percentage=percentage)}")