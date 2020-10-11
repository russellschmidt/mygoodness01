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

class Detail(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    org_detail_page_title = models.CharField(max_length=40, default="About Us")
    org_detail_hero_image = models.URLField(max_length=200, default='https://source.unsplash.com/random/1080x1080')
    org_detail_page_header = models.CharField(max_length=80, default="Detail about what we do")
    org_detail_description = models.TextField(max_length=10000, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eu diam sed nunc suscipit pulvinar. Curabitur vel lobortis ipsum, ac tincidunt libero. Proin tincidunt suscipit rhoncus. Cras molestie turpis urna, nec bibendum risus egestas at. Curabitur diam massa, tincidunt in nunc id, volutpat euismod massa. Sed ornare et augue eu consequat. Curabitur quis sapien iaculis, sollicitudin nunc tempor, maximus mi. Etiam vulputate viverra neque nec dapibus. Ut vitae feugiat nunc, id feugiat eros. Sed et faucibus metus, et efficitur justo. Sed ac neque nunc. Vestibulum a tellus mi.")
    def __str__(self):
        return self.org_detail_page_title