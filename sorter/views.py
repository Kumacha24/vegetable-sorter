from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import UserImage
from .forms import UploadImageForm

# Create your views here.
# 関数ベースビューの場合
# def top_page(request):
#   return render(request, 'sorter/top_page.html', {})

# クラスベースビューの場合
class TopView(generic.TemplateView):
  template_name = "sorter/top_page.html"

class SelectView(generic.CreateView):
  model = UserImage
  template_name = 'sorter/image_selection.html'
  form_class = UploadImageForm
  success_url = reverse_lazy('sorter:top_page')