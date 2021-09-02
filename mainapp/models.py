from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    image = models.ImageField(upload_to='articles/',blank = True,null = True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='author_images/',blank = True,null = True)
    text = models.TextField()
    date = models.DateField()
    duration = models.PositiveIntegerField()
    main = models.BooleanField()
    key = models.ForeignKey("Category",on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    image = models.ImageField(upload_to = 'categories/',blank = True,null = True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    