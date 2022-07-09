from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language, AuthorAdmin

#admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)
# Register your models here.