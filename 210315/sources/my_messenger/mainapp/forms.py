from django import forms

from mainapp.models import Dialog, DialogMembers


class DialogueCreation(forms.ModelForm):
    class Meta:
        model = Dialog
        fields = ('name',)
