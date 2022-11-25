from django import forms
from . import models as mdl


class NoteForm(forms.ModelForm):
    # subject =forms.CharField(label='Subject', max_length=100)
    # description = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
    #     ),
    #     max_length=10000,
    # )

    class Meta:
        model = mdl.Note
        fields = ('subject', 'description')
