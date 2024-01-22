#Exercise 8: Find student with highest average score.
#     students_info = {
# 'student1': {
# 'name': 'John Doe',
# 'age': 20,
# 'subjects': ['Math', 'Physics', 'English'],
# 'scores': [7, 9, 9, 6],
# },
# 'student2': {
# 'name': 'Jane Smith',
# 'age': 19,
# 'subjects': ['Chemistry', 'Biology', 'History'],
# 'scores': [5, 6, 8, 10],
# },
#     }
students_info = {
'student1': {
'name': 'John Doe',
'age': 20,
'subjects': ['Math', 'Physics', 'English'],
'scores': [7, 9, 9, 6],
},
'student2': {
'name': 'Jane Smith',
'age': 19,
'subjects': ['Chemistry', 'Biology', 'History'],
'scores': [5, 6, 8, 10],
},
'student3': {
'name': 'Bob Johnson',
'age': 21,
'subjects': ['Computer Science', 'Statistics', 'Psychology'],
'scores': [8, 8, 9, 9, 9],
},
}
def calculate_average_score(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

highest_average = 0
highest_average_student = None

for student_key, student_info in students_info.items():
    student_scores = student_info['scores']
    avg_score = calculate_average_score(student_scores)

    if avg_score > highest_average:
        highest_average = avg_score
        highest_average_student = student_key

print(f"The student with the highest average score is {students_info[highest_average_student]['name']}")