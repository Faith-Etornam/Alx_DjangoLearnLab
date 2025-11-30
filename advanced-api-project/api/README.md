# Book API - View Configuration

## Endpoints:
    -GET /books/: List all books instances. This task can be done by anyone.
    -GET /books/<id>/: Retrieve a book by ID. This task can be done by anyone.
    -POST /books/create/: Create a new book. This task can be done by only authenticated users.
    -PUT /books/<id>/update: Update a book. This task can be carried out by only authenticated users.
    -DELETE /books/<id>/delete: Delete a book. This operation can be done by only authenticated users.


## Customizations:
    -perform_create(): Attaches the logged-in user as the maker or creator.
    -perform_create(): Tracks who last modified the book.


## Permissions/Authorizations:
    -AllowAny: Used for viewing books instances and for getting the details of a book instance
    -IsAuthenticated: For the creation, update and deletion of books instances.