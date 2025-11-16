# Retrieve Book Instance

## Command Executed
```python
# Retrieve the book by title and display all attributes
book = Book.objects.get(title="1984")

# Display all attributes
print(f"ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Published Year: {book.published_year}")
print(f"ISBN: {book.isbn}")
print(f"Genre: {book.genre}")