from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (ForeignKey)
print("All books by J.K. Rowling:")
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
for book in books:
    print(f"- {book.title}")

print()

# 2. List all books in a library (ManyToMany)
print("All books in Central Public Library:")
library = Library.objects.get(name=library_name)
for book in library.books.all():
    print(f"- {book.title}")

print()

# 3. Retrieve the librarian for a library (OneToOne)
print("Librarian for Central Public Library:")
library = Library.objects.get(name="Central Public Library")
librarian = Librarian.objects.get(library=library)
print(f"- {librarian.name}")