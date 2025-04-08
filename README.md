# Проект 4 спринта "Юнит-тестирование"
## Файлы:
main.py - главный файл, содеращий класс BooksCollector
tests.py - тесты для класса BooksCollector в классе TestBooksCollector
## Набор тестовых методов класса TestBooksCollector:
- test_add_new_book_add_two_books: Проверка добавления двух книг в словарь
- test_set_book_genre_one_book: Проверка установления жанра
- test_get_book_genre_one_book: Проверка извлечения жанра
- test_get_books_with_specific_genre_one_of_two_books: Проверка, что по запросу жанра выводится одна подходящая книга из двух
- test_get_books_genre_two_books: Проверка вывода жанров двух книг
- test_get_books_for_children_one_of_two_books: Проверка, что по запросу жанра выводится одна подходящая для детей книга из двух
- test_add_book_in_favorites_one_book: Проверка добавления в избранное одной книги
- test_delete_book_from_favorites_add_two_books_and_delete_one_book: Проверка удаления книги из списка с двумя книгами
- test_get_list_of_favorites_book_one_of_two_books: Проверка получения списка избранных