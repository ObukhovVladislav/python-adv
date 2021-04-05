from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('message/<int:message_pk>', mainapp.message, name='message'),
    path('dialog/<int:dialog_pk>', mainapp.dialog, name='dialog'),
]
