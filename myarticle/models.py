from django.db import models

# Create your models here.
class Signup(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    password = models.CharField(max_length=100,unique=True)
    article_preference = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name

class Article(models.Model):

    user = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True, blank=True)
    article_name = models.CharField(max_length=100)
    article_desc = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.article_name

