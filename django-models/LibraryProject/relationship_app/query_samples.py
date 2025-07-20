from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
orwell = Author.objects.get(name="George Orwell")
books_by_orwell = Book.objects.filter(author=orwell)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
library_books = library.books.all()

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
