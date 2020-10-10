from django.db import models

# Create your models here.

class Org(models.Model):
  category_text = models.CharField(max_length=40)
  title_text = models.CharField(max_length=40)
  subtitle_text = models.CharField(max_length=200, null=True)
  button_label = models.CharField(max_length=20, default="Learn More")
  background_image = models.URLField(max_length=200, default='https://source.unsplash.com/random/480x853')
  pub_date = models.DateTimeField('date published')