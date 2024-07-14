from django.contrib import admin
from .models import LibraryTopCategory,LibraryMiddleCategory,LibrarySubCategory,LibraryData

admin.site.register(LibraryTopCategory)
admin.site.register(LibraryMiddleCategory)
admin.site.register(LibrarySubCategory)
admin.site.register(LibraryData)
