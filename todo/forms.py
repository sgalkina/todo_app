from django.forms import ModelForm, TextInput
from todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={
                'placeholder': 'What else do you need to do?',
                'class': "form-control",
                'style': "width: 70%;",
                'autocomplete': "off",
            }),
        }
        labels = {
            "text": "",
        }
