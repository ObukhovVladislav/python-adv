from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mainapp.models import Message


@login_required
def index(request):
    dialogues = request.user.dialogs.all()
    context = {
        'page_title': 'Диалоги',
        'dialogues': dialogues,

    }
    return render(request, 'mainapp/index.html', context)


def message(request, message_pk):
    message = Message.objects.filter(id=message_pk)
    context = {
        'page_title': 'Сообщения',
        'message': message,
    }
    return render(request, 'mainapp/message.html', context)
