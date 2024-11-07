# utils/formatting.py

def format_book_data(data):
    """Форматирует данные книги для вывода в отчет"""
    return f"Title: {data['title']}, Author: {data['author']}, Genre: {data['genre']}"
