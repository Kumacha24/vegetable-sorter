from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import UserImage
from .forms import UploadImageForm
from static.python.machinelearning_model import predict_image

class TopView(generic.TemplateView):
  template_name = "sorter/top_page.html"

class SelectView(generic.CreateView):
  model = UserImage
  template_name = 'sorter/image_selection.html'
  form_class = UploadImageForm

  def get_success_url(self):
    return reverse('sorter:result_page', kwargs={'pk': self.object.id}) 


class ResultView(generic.DetailView):
  model = UserImage
  template_name = 'sorter/vegetable_description_page.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      uploaded_image = self.object.image
      label = predict_image(uploaded_image)
      context['label'] = label
      return context