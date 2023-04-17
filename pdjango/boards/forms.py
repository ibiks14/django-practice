from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control','cols':40, 'rows': 5, 'placeholder': 'What is on your mind?'}  
        ), 
        max_length=4000,
        help_text='The max length of the text is 4000.', required=True
        )
    subject = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Topic
        fields = ['subject', 'message']


