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


# def message(request):
#     messages = Message.user.messages.filter()
#     context = {
#         'page_title': 'Сообщения',
#         'messages': messages,
#     }
#     return render(request, 'mainapp/message.html', context)
