from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default = False)
    discription = models.TextField(null = True ,blank = True)
    image = models.ImageField(upload_to='article_image',null =True, blank=True )

    def __str__(self):
        return self.headline

