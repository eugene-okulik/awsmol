import os
import csv
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

base_path = os.path.dirname(__file__)
my_homework_path = os.path.dirname(base_path)
homework_path = os.path.dirname((os.path.dirname(base_path)))
eugene_homework_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(eugene_homework_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file, fieldnames=None)
    data = []
    for row in file_data:
        if row:
            data.append(row)

# print(data)

with mysql.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSW'),
        database=os.getenv('DB_NAME')
) as db:
    cursor = db.cursor(dictionary=True)

    for row in data:
        name, second_name, group, book, subject, lesson, mark = row.values()

        # print(f"{name} {second_name}, {group}, {book}, {subject}, {lesson}, {mark}")

        our_query = '''
            SELECT name, second_name, groups.title, books.title, subjets.title, lessons.title, marks.value 
            FROM students
            JOIN `groups` ON students.group_id = groups.id
            JOIN books ON students.id = books.taken_by_student_id
            JOIN marks ON marks.student_id = students.id
            JOIN lessons ON marks.lesson_id = lessons.id
            JOIN subjets ON lessons.subject_id = subjets.id
            WHERE name = %s and second_name = %s and groups.title = %s and books.title = %s 
            and subjets.title = %s and lessons.title = %s and marks.value = %s;
        '''

        cursor.execute(our_query, (name, second_name, group, book, subject, lesson, mark))
        our_names = cursor.fetchall()

        if not our_names:
            print(
                f'В базе данных {os.getenv("DB_NAME")} нет этих данных: '
                f'{name}, {second_name}, {group}, {book}, {subject}, {lesson}, {mark}')
