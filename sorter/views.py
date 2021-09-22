from django.shortcuts import render

# Create your views here.
def top_page(request):
  return render(request, 'sorter/top_page.html', {})