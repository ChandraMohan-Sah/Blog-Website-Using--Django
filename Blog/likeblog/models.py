from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from phone_field import PhoneField

# Create your models here.
class Address(models.Model):
    address=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.address}'


class Author(models.Model):
    
    aname=models.CharField(max_length=50)
    profile= models.ImageField()
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    contact=PhoneField(blank=True, help_text='Contact phone number')
    email= models.EmailField()

    def __str__(self):
        return f'{self.aname}'

class Category(models.Model):
    blog_name=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.blog_name}'

class Blog(models.Model):
    title = models.CharField(max_length = 50)
    date_posted = models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    author =models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail= models.ImageField(blank=True,null=True)
    slug_title=models.SlugField(null=False,blank=False,editable=False)

    def __str__(self):
        return f'{self.title}-{self.date_posted}'

    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)







