from django import forms
from .models import newPerson

class newPersonForm(forms.ModelForm):
	class Meta:
		model = newPerson