from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
# 関数ベースビューの場合
# def top_page(request):
#   return render(request, 'sorter/top_page.html', {})

# クラスベースビューの場合
class TopView(generic.TemplateView):
  template_name = "sorter/top_page.html"