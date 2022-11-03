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

class ForgotPassword(models.Model):
    code = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


##################################################################################################

class Home(models.Model):
    username = models.CharField(max_length = 100)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.first_name



class Stu(models.Model):
    user = models.ForeignKey(Home,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length = 10 )
    last_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.last_name


