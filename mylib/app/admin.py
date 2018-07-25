from django.contrib import admin

# Register your models here.
from app.models import Publisher
from app.models import Book
from app.models import Author

# Register your models here.
class PublishersPostAdmin(admin.ModelAdmin):
    list_display01 = ['id', 'name']

class BooksPostAdmin(admin.ModelAdmin):
    list_display02 = ['id', 'name', 'publisher']

class AuthorsPostAdmin(admin.ModelAdmin):
    list_display03 = ['id', 'name', 'book']


admin.site.register(Publisher, PublishersPostAdmin)

admin.site.register(Book, BooksPostAdmin)

admin.site.register(Author, AuthorsPostAdmin)