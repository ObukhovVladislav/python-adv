from django.forms import ModelForm

from mainapp.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('sender', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name_field, field in self.fields.items():
            print(name_field, field)
