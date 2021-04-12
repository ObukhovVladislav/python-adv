from django import forms

from mainapp.models import Dialog


class DialogueCreation(forms.ModelForm):
    class Meta:
        model = Dialog
        fields = ('name',)
