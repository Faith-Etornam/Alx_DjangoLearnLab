from .models import Author, Librarian, Book, Library

Library.objects.get(name=library_name).books.all()

Author.objects.filter(author=author)

books = Book.objects.filter(author_id=1)

Book.objects.all()

Librarian.objects.filter(library_id=1)