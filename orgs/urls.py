from django.urls import path

from . import views

app_name = 'orgs'
urlpatterns = [
  # ex: /orgs
  path('', views.index, name='index'),
  # ex: /orgs/5/
  path('<int:org_id>/', views.stream, name='stream'),
  # ex: /orgs/5/detail
  path('<int:org_id>/detail/', views.detail, name='detail'),
]