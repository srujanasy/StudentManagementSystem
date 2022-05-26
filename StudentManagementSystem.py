def calculate_highest_in_maths(student_list):
    highest_score_in_Maths = 0
    highest_score_in_Maths_Name = ''
    for student in student_list:
        if(student.get("Maths") > highest_score_in_Maths):
            highest_score_in_Maths = student.get("Maths")
            highest_score_in_Maths_Name = student.get("name")
    print(f"The highest score in Maths is {highest_score_in_Maths} by {highest_score_in_Maths_Name}")


def calculate_highest_in_social(student_list):
    highest_score_in_social = 0
    highest_score_in_Social_Name = ''
    for student in student_list:
        if(student.get("Social") > highest_score_in_social):
            highest_score_in_social = student.get("Social")
            highest_score_in_Social_Name = student.get("name")
    print(f"The highest score in Social is {highest_score_in_social} by {highest_score_in_Social_Name}")


def calculate_highest_in_science(student_list):
    highest_score_in_Science = 0
    highest_score_in_Science_Name = ''
    for student in student_list:
        if(student.get("Science") > highest_score_in_Science):
            highest_score_in_Science = student.get("Science")
            highest_score_in_Science_Name = student.get("name")
    print(f"The highest score in Science is {highest_score_in_Science} by {highest_score_in_Science_Name}")


student_1 = {
    "Maths" : 45,
    "Social" : 75,
    "Science" : 96,
    "name" : "Tanmay"
}

student_2 = {
    "Maths" : 74,
    "Social" : 83,
    "Science" : 100,
    "name" : "Dheeraj"
}

student_3 = {
    "Maths" : 98,
    "Social" : 62,
    "Science" : 23,
    "name" : "Sooraj"
}

student_list = [student_1,student_2,student_3]
calculate_highest_in_maths(student_list)
calculate_highest_in_social(student_list)
calculate_highest_in_science(student_list)