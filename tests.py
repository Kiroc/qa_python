from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        #Проверяем, что присвоенное значение равно тому, что присваивали ранее
        assert collector.genre.get('Что делать, если ваш кот хочет вас убить') == 'Детективы'

    def test_get_book_genre_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        # Проверяем с помощью тестируемой функции get_book_genre, что присвоенное значение равно тому, что присваивали ранее
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Детективы'

    def test_get_books_with_specific_genre_one_of_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        # Проверяем с помощью тестируемой функции get_books_with_specific_genre, что присвоенное значение равно тому, что присваивали ранее
        assert collector.get_books_with_specific_genre('Детективы')==['Что делать, если ваш кот хочет вас убить']

    def test_get_books_genre_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        # проверяем, что в списке оба жанра
        assert collector.get_books_genre()==['Детективы','Фантастика']

    def test_get_books_for_children_one_of_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        # проверяем, что в списке находится только одна книга, подходящая для детей
        assert collector.get_books_for_children()==['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что в избранном находится добавленная книга
        assert collector.favorites==['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_add_two_books_and_delete_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        # добавляем две книги в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # удаляем одну книгу из избранного
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что в избранном осталась одна книга
        assert collector.favorites==['Гордость и предубеждение и зомби']

    def test_get_list_of_favorites_book_one_of_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем жанры
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # проверяем, что в избранном одна добавленная книга
        assert collector.get_list_of_favorites_books()==['Что делать, если ваш кот хочет вас убить']