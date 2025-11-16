#-- imports
import os
import django
from relationship_app.models import Author, Book, Library, Librarian

#-- setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

#--Queries:

#-- Query all books by a specific author.
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print("Author not found.")

#-- List all books in a library
def get_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library_name}:")
        for book in library.books.all():
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print("Library not found.")

#-- Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library.name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or librarian not found.")


#-- Running all queries
if __name__ == "__main__":
    get_books_by_author("Chinua Achebe")
    get_all_books_in_library("Accra City Library")
    get_librarian_for_library("Accra City Library")
