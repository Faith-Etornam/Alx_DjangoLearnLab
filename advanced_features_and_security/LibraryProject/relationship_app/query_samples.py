from relationship_app.models import Author, Book, Library, Librarian

def specificAuthor(author_name):
    print("All books by J.K. Rowling:")
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(f"- {book.title}")

print()


def allBooks(library_name):
    print("All books in Central Public Library:")
    library = Library.objects.get(name=library_name)
    for book in library.books.all():
        print(f"- {book.title}")

print()

print("Librarian for Central Public Library:")
library = Library.objects.get(name="Central Public Library")
librarian = Librarian.objects.get(library=library)
print(f"- {librarian.name}")