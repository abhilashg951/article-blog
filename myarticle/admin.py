from django.contrib import admin

# Register your models here.
from myarticle.models import *

class SignupAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name','phone_no','email','dob','password','article_preference']
admin.site.register(Signup,SignupAdmin)

class ArticleAdmin(admin.ModelAdmin):
	list_display=['user', 'article_name', 'article_desc', 'category', 'tag',]
admin.site.register(Article,ArticleAdmin)