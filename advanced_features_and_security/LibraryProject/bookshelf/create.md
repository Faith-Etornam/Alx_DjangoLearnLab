# Create Book Instance

## Command Executed
```python
# Create a Book instance with specified attributes
new_book = Book.objects.create(
    title="1984",
    author="George Orwell", 
    published_year=1949
)