```python
Book.objects.all()
# Output: <QuerySet [<Book: 1984>]>

book = Book.objects.get(id=1)
book.title
# Output: '1984'
