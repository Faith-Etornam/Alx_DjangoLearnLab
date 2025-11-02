
## delete.md

```markdown
# Delete Book Instance

## Command Executed
```python
# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print("Remaining books:")
for book in all_books:
    print(f"- {book.title}")

# Alternative confirmation by trying to retrieve the specific book
try:
    deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
    print("Book still exists!")
except Book.DoesNotExist:
    print("Book successfully deleted - DoesNotExist exception raised")