INSERT INTO students (name, second_name) VALUES ('Hermione', 'Granger');

-- SELECT * FROM students
-- WHERE name = 'Hermione';

INSERT INTO books (title, taken_by_student_id) VALUES ('History of Magic', 1391);
INSERT INTO books (title, taken_by_student_id) VALUES ('Dark Arts Defence Basics for Beginners', 1391);
INSERT INTO books (title, taken_by_student_id) VALUES ('The Standard Book of Spells', 1391);
INSERT INTO books (title, taken_by_student_id) VALUES ('Intermediate Transfiguration', 1391);
INSERT INTO books (title, taken_by_student_id) VALUES ('Fantastic Beasts and Where to Find Them', 1391);

-- SELECT * FROM books
-- WHERE taken_by_student_id = 1391;

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Gryffindor', 'may 2024', 'aug 2024');

-- SELECT * FROM `groups` g 
-- WHERE title LIKE 'Gryff%';

UPDATE students SET group_id = 1391 WHERE id = 1391;

-- SELECT * FROM students
-- WHERE id = 1391;

INSERT INTO subjets (title) VALUES ('Transfiguration');
INSERT INTO subjets (title) VALUES ('Potions');
INSERT INTO subjets (title) VALUES ('Herbology');
INSERT INTO subjets (title) VALUES ('Study of Ancient Runes');
INSERT INTO subjets (title) VALUES ('Defence against the Dark Arts');
INSERT INTO subjets (title) VALUES ('History of Magic');

-- SELECT * FROM subjets
-- ORDER BY id DESC 
-- LIMIT 6;

INSERT INTO lessons (title, subject_id) VALUES ('Transfiguration a glass into a mouse', 1843);
INSERT INTO lessons (title, subject_id) VALUES ('Transfiguration of ears into cacti', 1843);
INSERT INTO lessons (title, subject_id) VALUES ('Felix Felicis', 1844);
INSERT INTO lessons (title, subject_id) VALUES ('Polyjuice Potion', 1844);
INSERT INTO lessons (title, subject_id) VALUES ('Mandrake', 1845);
INSERT INTO lessons (title, subject_id) VALUES ('Bubotuber', 1845);
INSERT INTO lessons (title, subject_id) VALUES ('Fehu', 1846);
INSERT INTO lessons (title, subject_id) VALUES ('Uruz', 1846);
INSERT INTO lessons (title, subject_id) VALUES ('Grindylow', 1847);
INSERT INTO lessons (title, subject_id) VALUES ('Boggart', 1847);
INSERT INTO lessons (title, subject_id) VALUES ('The Goblin War', 1848);
INSERT INTO lessons (title, subject_id) VALUES ('Statute of secrecy', 1848);

-- SELECT * FROM lessons l 
-- WHERE subject_id BETWEEN 1843 and 1849;

INSERT INTO marks (value, lesson_id, student_id) 
VALUES (5, 4208, 1391), (5, 4209, 1391), (5, 4210, 1391),
(5, 4211, 1391), (5, 4212, 1391), (5, 4213, 1391), 
(5, 4214, 1391), (5, 4215, 1391), (5, 4216, 1391),
(5, 4217, 1391), (5, 4218, 1391), (5, 4219, 1391);

SELECT * FROM marks
WHERE student_id = 1391;

SELECT * FROM books
WHERE taken_by_student_id = 1391;

SELECT *
FROM students
JOIN `groups` ON students.group_id = groups.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON marks.student_id = students.id
JOIN lessons ON marks.lesson_id = lessons.id
JOIN subjets ON lessons.subject_id = subjets.id
WHERE students.name = 'Hermione' and students.second_name = 'Granger';
