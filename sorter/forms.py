from django import forms
from PIL import Image
from .models import UserImage

class UploadImageForm(forms.ModelForm):
  class Meta:
    model = UserImage
    fields = ('image',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'