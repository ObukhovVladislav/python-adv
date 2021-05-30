from django.contrib import admin

# Register your models here.
from mainapp.models import Dialog, DialogMembers, Message

admin.site.register(Dialog)
admin.site.register(DialogMembers)
admin.site.register(Message)
