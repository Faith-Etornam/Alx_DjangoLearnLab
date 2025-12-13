from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display= ('title', 'author', 'publication_year')
    list_filter = ('title','publication_year')
    search_fields = ('title',)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', )


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

