# catalog.py

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        """Добавляет книгу в библиотеку"""
        self.books.append({
            "title": title,
            "author": author,
            "genre": genre
        })

    def remove_book(self, title):
        """Удаляет книгу по названию"""
        self.books = [book for book in self.books if book["title"] != title]

    def search_by_title(self, title):
        """Ищет книги по названию"""
        return [book for book in self.books if book["title"] == title]

    def search_by_author(self, author):
        """Ищет книги по автору"""
        return [book for book in self.books if book["author"] == author]

    def search_by_genre(self, genre):
        """Ищет книги по жанру"""
        return [book for book in self.books if book["genre"] == genre]

    def list_books(self):
        """Возвращает все книги в библиотеке"""
        return self.books
