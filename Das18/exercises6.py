# 6. Tuple Exercise:
# Create a tuple of student names and their corresponding scores. Write a function to find
# the student with the highest score.
def highest_scores_student_name(students):
    student_name=""                                                                                                                                                                                                                                                                                                     
    student_score=0
    for name,score in students:
        if score>student_score:
            student_name=name
            student_score=score
    return student_name
student_scores=(("Arman",20),("Arsen",15),("Aram",25),("Sergey",18))
student_name=highest_scores_student_name(student_scores)
print(f"Student of highest score {student_name}")


