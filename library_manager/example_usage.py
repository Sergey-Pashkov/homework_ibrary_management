# example_usage.py

from catalog import Library
from report import generate_report
from utils.data_validation import validate_book_data
from utils.formatting import format_book_data

# Создаем экземпляр библиотеки
library = Library()

# Данные книг для добавления
book1 = {"title": "1984", "author": "George Orwell", "genre": "Dystopian"}
book2 = {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Science Fiction"}

# Валидация и добавление книг
if validate_book_data(book1):
    library.add_book(**book1)
if validate_book_data(book2):
    library.add_book(**book2)

# Генерация отчета и вывод
print(generate_report(library))
