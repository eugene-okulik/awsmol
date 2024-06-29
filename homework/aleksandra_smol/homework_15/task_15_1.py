import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

student_name = 'Voldemort'
student_surname = 'Marvolovich'
query_students = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'

cursor.execute(query_students, (student_name, student_surname))
get_student_id = cursor.lastrowid
db.commit()
print(f'student id is {get_student_id}')

query_books = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
cursor.executemany(query_books, [
    ('History of Magic - level 5', get_student_id),
    ('Dark Arts Defence Basics for Beginners - level 5', get_student_id),
    ('The Standard Book of Spells - level 5', get_student_id),
    ('Intermediate Transfiguration - level 5', get_student_id),
    ('Fantastic Beasts and Where to Find Them - level 5', get_student_id)
])
get_books_id = cursor.lastrowid
db.commit()
print(f'books id is {get_books_id}')

query_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
cursor.execute(query_group, ('Slytherin', 'may 24', 'aug 24'))
get_group_id = cursor.lastrowid
db.commit()
print(f'group id is {get_group_id}')

query_update_group_student = 'UPDATE students SET group_id = %s WHERE id =  %s'
cursor.execute(query_update_group_student, (get_group_id, get_student_id))
db.commit()

query_subjects = 'INSERT INTO subjets (title) VALUES (%s)'
cursor.execute(query_subjects, ('Dark Arts - level 5',))
subject_dark_id = cursor.lastrowid
cursor.execute(query_subjects, ('Potions - level 5',))
subject_potions_id = cursor.lastrowid
cursor.execute(query_subjects, ('Transfiguration - level 5',))
subject_transfig_id = cursor.lastrowid
db.commit()

query_lessons = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
cursor.execute(query_lessons, ('Protective charms', subject_dark_id))
lesson_dark_id = cursor.lastrowid
print(lesson_dark_id)

cursor.execute(query_lessons, ('Potions', subject_potions_id))
lesson_potion_id = cursor.lastrowid
print(lesson_potion_id)

cursor.execute(query_lessons, ('Transfiguration a glass into a mouse', subject_transfig_id))
lesson_transfig_id = cursor.lastrowid
print(lesson_transfig_id)
db.commit()

mark = 'A'
query_marks = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
cursor.executemany(query_marks, [
    (mark, lesson_dark_id, get_student_id),
    (mark, lesson_potion_id, get_student_id),
    (mark, lesson_transfig_id, get_student_id)
])
db.commit()

query_get_marks = 'SELECT * FROM marks WHERE student_id = %s'
cursor.execute(query_get_marks, (get_student_id,))
student_marks = cursor.fetchall()
print(f'Marks of our student: {student_marks}')

query_get_books = 'SELECT * FROM books WHERE taken_by_student_id = %s'
cursor.execute(query_get_books, (get_student_id,))
student_books = cursor.fetchall()
print(f'Books of our student: {student_books}')

query_get_all_student_info = '''
    SELECT *
    FROM students
    JOIN `groups` ON students.group_id = groups.id
    JOIN books ON students.id = books.taken_by_student_id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjets ON lessons.subject_id = subjets.id
    WHERE students.id = '%s'
'''
cursor.execute(query_get_all_student_info, (get_student_id,))
all_about_student = cursor.fetchall()
print(f'All about student: {all_about_student}')

db.close()
