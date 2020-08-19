from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Task...'}))

	class Meta:
		model = Task
		fields = '__all__'
		widgets = {
			'completed' : forms.CheckboxInput(attrs={'style':'width:15px;height:15px;vertical-align:-2px'}),
		}