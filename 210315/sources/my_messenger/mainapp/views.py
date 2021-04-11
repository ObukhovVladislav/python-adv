from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from mainapp.models import Message, DialogMembers, Dialog


@login_required
def index(request):
    dialogues = request.user.dialogs.select_related('dialog').all()
    context = {
        'page_title': 'Диалоги',
        'dialogues': dialogues,

    }
    return render(request, 'mainapp/index.html', context)


def dialog(request, dialog_pk):
    dialog = get_object_or_404(Dialog, pk=dialog_pk)
    _dialog_members = DialogMembers.objects.filter(dialog=dialog)
    dialog_members = _dialog_members.exclude(member=request.user). \
        select_related('member')
    messages = Message.objects.filter(sender__in=dialog_members). \
        select_related('sender__member')

    context = {
        'dialog': dialog,
        'dialog_members': dialog_members,
        'messages': messages,
    }
    return render(request, 'mainapp/dialog.html', context)
