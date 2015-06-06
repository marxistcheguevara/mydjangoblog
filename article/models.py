from django.db import models
from time import time

class Author(models.Model):
	
	name = models.CharField(max_length=20)

class Category(models.Model):
	
	name = models.CharField(max_length=20)
	

def get_upload_file_name(instance,  filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'),  filename)

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(Author, default=lambda: Author.objects.get(id=1))
    thumbnail = models.FileField(upload_to = get_upload_file_name)
    category = models.ForeignKey(Category, default=lambda: Category.objects.get(id=1))
		
    def __unicode__(self):
        return self.title
        
class Comment(models.Model):
                          
    name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    article = models.ForeignKey(Article)

        
#class Category(models.Model):
	
#	name = models.CharField(max_length=20)
#	article = models.ForeignKey(Article)
	
	
	
