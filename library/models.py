from django.db import models

class LibraryTopCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class LibraryMiddleCategory(models.Model):
    top_category = models.ForeignKey(LibraryTopCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.top_category.name} - {self.name}"


class LibrarySubCategory(models.Model):
    middle_category = models.ForeignKey(LibraryMiddleCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.middle_category.name} - {self.name}"


class LibraryData(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    author = models.CharField(max_length=255,blank=True,null=True)
    top_category = models.ForeignKey(LibraryTopCategory,on_delete=models.CASCADE)
    middle_category = models.ForeignKey(LibraryMiddleCategory,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(LibrarySubCategory,on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='library_covers/',blank=True,null=True)
    file = models.FileField(upload_to='library_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title