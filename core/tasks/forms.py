from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']
        widgets={'name':forms.TextInput({'style':"width:170px"})}