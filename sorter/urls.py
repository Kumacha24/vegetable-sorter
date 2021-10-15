from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'sorter'

urlpatterns = [
  path('', views.TopView.as_view(), name='top_page'),
  path('image-select/', views.SelectView.as_view(), name='image_select'),
  path('result/<int:pk>/', views.ResultView.as_view(), name='result_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)