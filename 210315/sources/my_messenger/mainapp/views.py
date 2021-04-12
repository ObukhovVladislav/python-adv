from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.forms import DialogueCreation
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


def dialogue_creation(request):
    if request.method == 'POST':
        form = DialogueCreation(request.POST)
        if form.is_valid():
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = DialogueCreation()
    context = {
        'title': 'Создание диалогов',
        'form': form,
    }
    return render(request, 'mainapp/dialogue_creation.html', context)
