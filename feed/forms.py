from django import forms
from .models import Idea


class IdeaForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   'placeholder': 'Enter your idea',
                                   'class': 'form-control'
                               }
                           ),
                           label=''
                           )
    
    class Meta:
        model = Idea
        exclude = ('user',)