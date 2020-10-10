from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # ex: /orgs/5/
  path('<int:org_id>/', views.detail, name='detail'),
]