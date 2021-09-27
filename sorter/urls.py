from django.urls import path
from . import views

app_name = 'sorter'

urlpatterns = [
  path('', views.TopView.as_view(), name='top_page'),
]