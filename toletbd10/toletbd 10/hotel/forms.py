from hotel.models import *
from django import forms

class Asked_Questions_Form_Forms(forms.ModelForm):
  class Meta:
    model = Asked_Questions_Form
    fields = "__all__"
    
class NewsletterForm(forms.ModelForm):
  class Meta:
    model = Newsletter
    fields = "__all__"
    
class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = "__all__"
    
class PropertyForm(forms.ModelForm):
  class Meta:
    model = Property
    exclude = ["user",]

