# Exercise 7: Find youngest student
# Write a function that takes a dictionary with information about students. Return info
# about the youngest student.
# Dictionary example
# students_info = {
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
# 'student3': {
# 'name': 'Bob Johnson',
# 'age': 21,
# 'subjects': ['Computer Science', 'Statistics', 'Psychology'],
# 'scores': [8, 8, 9, 9, 9],
# },
# }
def youngest_student_info(students_info):
    youngest_student = None

    for student in students_info.values():
        age = student['age']
        if youngest_student is None or age < youngest_student['age']:
            youngest_student = student
    return youngest_student
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
youngest_student = youngest_student_info(students_info)
print(youngest_student)