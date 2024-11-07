# report.py

def generate_report(library):
    """Генерирует отчет о книгах в библиотеке"""
    report_lines = ["Library Report:"]
    for book in library.list_books():
        line = f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}"
        report_lines.append(line)
    return "\n".join(report_lines)
