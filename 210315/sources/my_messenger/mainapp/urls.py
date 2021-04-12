from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('dialog/<int:dialog_pk>', mainapp.dialog, name='dialog'),
    path('dialogue_creation/', mainapp.dialogue_creation, name='dialogue_creation'),
]
