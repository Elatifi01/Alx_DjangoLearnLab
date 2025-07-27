```python
from bookshelf.models import Book
book.delete()

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>
