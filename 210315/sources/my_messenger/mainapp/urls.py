from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('dialog/<int:dialog_pk>/', mainapp.dialog, name='dialog'),
    path('dialog/create/', mainapp.dialog_create, name='dialog_create'),
    path('user/dialog/create/<int:user_id>/', mainapp.user_dialog_create,
         name='user_dialog_create'),
]
