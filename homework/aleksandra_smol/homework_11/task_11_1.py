class Book:
    material = "Бумага"
    text = True

    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.flag = False

    def reserved_book(self):
        self.flag = True

    def about_book(self):
        if self.flag:
            print(
                f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}, '
                f'зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}')


class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, subject, level):
        super().__init__(title, author, pages, isbn)
        self.subject = subject
        self.level = level
        self.exercises = False

    def reserved_school_book(self):
        self.exercises = True

    def about_school_book(self):
        if self.exercises:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, '
                  f'класс: {self.level}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
                  f'предмет: {self.subject}, класс: {self.level}')


book_1 = Book('Дон Кихот', 'Сервантес Сааведра Мигель де', 192, '978-5-389-11309-1')
book_2 = Book('Гарри Поттер', 'Роулинг Джоан Кэтлин', 432, '978-5-389-07435-4')
book_3 = Book('12 стульев', 'Ильф Илья, Петров Евгений', 448, '978-5-17-092624-4')
book_4 = Book('Алиса в Стране чудес', 'Кэрролл Льюис', 224, '978-5-17-163391-2')
book_5 = Book('Пиноккио', 'Коллоди Карло', 216, '978-5-370-05316-0')

book_2.reserved_book()

book_1.about_book()
book_2.about_book()
book_3.about_book()
book_4.about_book()
book_5.about_book()

school_book_1 = SchoolBook('Алгебра', 'Виленкин Наум', 176,
                           '978-5-09-102531-6', 'Математика', '5')
school_book_2 = SchoolBook('Русский язык', 'Иванов', 211,
                           '978-5-11-102871-1', 'Русский', '10')
school_book_3 = SchoolBook('История России', 'Петров', 430,
                           '978-5-09-102576-5', 'История', '6')

school_book_2.reserved_school_book()

school_book_1.about_school_book()
school_book_2.about_school_book()
school_book_3.about_school_book()
