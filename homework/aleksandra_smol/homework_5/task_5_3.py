students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_open = ', '.join(students)
subjects_open = ', '.join(subjects)

text = f"Students {students_open} study these subjects: {subjects_open}"
print(text)
