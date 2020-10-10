import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Org(models.Model):
  organization_text = models.CharField(max_length=80, null=True)
  category_text = models.CharField(max_length=40)
  title_text = models.CharField(max_length=40)
  subtitle_text = models.CharField(max_length=200, null=True)
  button_label = models.CharField(max_length=20, default="Learn More")
  background_image = models.URLField(max_length=200, default='https://source.unsplash.com/random/480x853')
  pub_date = models.DateTimeField('date published')
  def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  def __str__(self):
        return self.title_text
