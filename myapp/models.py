from django.db import models

# Create your models here.
class Book(models.Model):
    def __str__(self):
        return self.book

    book = models.CharField(max_length=100)
    author = models.CharField(max_length=300)
    book_image = models.ImageField(default= 'default.jpg' , upload_to = 'book_images/')
    book_upload  = models.FileField( default = 'default.pdf', upload_to='Book_file')