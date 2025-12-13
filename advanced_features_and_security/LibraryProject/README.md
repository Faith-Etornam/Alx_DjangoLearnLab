# Permissions and Groups Setup

This document outlines the custom permissions and group configurations for the LibraryProject application.

## 1. Custom Permissions
The following permissions are defined in the `Book` model meta options to control access levels.

| Variable Name | Permission Code | Description |
| :--- | :--- | :--- |
| **`can_view`** | `libraryproject.can_view` | Allows a user to read/view book details. |
| **`can_create`** | `libraryproject.can_create` | Allows a user to create new book entries. |
| **`can_edit`** | `libraryproject.can_edit` | Allows a user to modify existing book entries. |
| **`can_delete`** | `libraryproject.can_delete` | Allows a user to remove books from the system. |

## 2. User Groups
We have established three primary groups to manage user roles efficiently.

### **Viewers**
* **Role:** Standard users who can only browse content.
* **Permissions:** `can_view`

### **Editors**
* **Role:** Content creators who manage book listings.
* **Permissions:** `can_view`, `can_create`, `can_edit`

### **Admins**
* **Role:** System administrators with full control.
* **Permissions:** `can_view`, `can_create`, `can_edit`, `can_delete`

## 3. Implementation in Code
To enforce these permissions in views, use the `@permission_required` decorator with the specific permission strings:

```python
from django.contrib.auth.decorators import permission_required

@permission_required('libraryproject.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # View logic here...