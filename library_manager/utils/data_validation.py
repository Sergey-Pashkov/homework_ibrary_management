# utils/data_validation.py

def validate_book_data(data):
    """Проверяет корректность данных книги"""
    required_fields = ["title", "author", "genre"]
    return all(field in data and isinstance(data[field], str) for field in required_fields)
