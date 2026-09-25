# Day 1 - Python Fundamentals

def input_student():
    student_name=input("Enter the name:")
    marks_python=float(input("Enter marks for python:")) 
    marks_maths=float(input ("Enter marks for math:"))
    marks_comm=float(input("Enter marks for communication:"))
    dict_student_info={
     "name":student_name,
     "python_marks":marks_python,
     "math_marks":marks_maths,
     "comm_marks":marks_comm
      }
    return dict_student_info
 
def calculate_percentage(marks_python,marks_math,marks_comm):
    total = (marks_python+marks_math+marks_comm)
    percentage=(total/300)*100
    return percentage


if __name__=="__main__":
    print("\n -- Result --")
    student_info=input_student()
    print("Student:",student_info["name"])
    print("Percentage",calculate_percentage(
        student_info["python_marks"],
        student_info["math_marks"],
        student_info["comm_marks"])
        )