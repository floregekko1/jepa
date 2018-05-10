from django.db import models
from django.contrib import admin
from django.utils import timezone
#from embed_video.fields import EmbedVideoField

# Create your models here.
class Article(models.Model):
	titre = models.CharField(max_length=100)
	auteur = models.CharField(max_length = 42)
	contenu = models.TextField(null=True)
	date = models.DateTimeField(default=timezone.now) 
	


