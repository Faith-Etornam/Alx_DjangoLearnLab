from .models import Author, Librarian, Book

books = Book.objects.filter(author_id=1)

Book.objects.all()

Librarian.objects.filter(library_id=1)