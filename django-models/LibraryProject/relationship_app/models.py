from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)   

class UserProfile(models.Model):
    ADMIN_ROLE = 'Admin'
    LIBRARIAN_ROLE = 'Librarian'
    MEMBER_ROLE = 'Member'

    ROLE_CHOICES = {
        ADMIN_ROLE: 'Admin',
        LIBRARIAN_ROLE: 'Librarian',
        MEMBER_ROLE: 'Member'
    }
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES)
