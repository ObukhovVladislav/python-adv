from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from mainapp.forms import MessageForm
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
    sender = dialog.receive_sender(request.user.pk)

    context = {
        'page_title': 'диалог',
        'dialog': dialog,
        'sender': sender,
    }

    return render(request, 'mainapp/dialog.html', context)


def dialog_create(request):
    dialogues = request.user.dialogs.select_related('dialog').all(). \
        values_list('dialog_id', flat=True)
    collocutors = DialogMembers.objects.filter(dialog__in=dialogues). \
        values_list('member_id', flat=True)
    new_collocutors = User.objects.exclude(pk__in=collocutors)

    context = {
        'page_title': 'новый диалог',
        'new_interlocutors': new_collocutors,
    }
    return render(request, 'mainapp/dialog_create.html', context)


def user_dialog_create(request, user_id):
    collocutor = User.objects.get(pk=user_id)
    dialog = Dialog.objects.create(
        name=collocutor.username
    )
    DialogMembers.objects.create(
        dialog=dialog,
        member=request.user,
        role=DialogMembers.CREATOR
    )
    DialogMembers.objects.create(
        dialog=dialog,
        member=collocutor,
        role=DialogMembers.INTERLOCUTOR
    )

    return HttpResponseRedirect(
        reverse('mainapp:dialog', kwargs={'dialog_pk': dialog.pk})
    )


def delete_dialog(request, pk):
    example = get_object_or_404(Dialog, pk=pk)
    example.delete()
    return HttpResponseRedirect(reverse('mainapp:index'))


class MessageCreate(CreateView):
    model = Message
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        sender_pk = self.request.resolver_match.kwargs['sender_pk']
        form.initial['sender'] = sender_pk

        return context

    def get_success_url(self):
        return reverse(
            'mainapp:dialog',
            kwargs={'dialog_pk': self.object.sender.dialog_id}
        )


def update_new_messages(request, dialog_pk):
    if request.is_ajax():
        dialog = Dialog.objects.filter(pk=dialog_pk).first()
        status = False
        new_messages = None
        if dialog:
            status = True
            new_messages_ = dialog.unread_messages(request.user.pk)
            new_messages = [{'pk': el.pk,
                             'username': el.sender.member.username,
                             'created': el.created.strftime('%Y.%m.%d %H:%M'),
                             'text': el.text}
                            for el in new_messages_]
        return JsonResponse({
            'status': status,
            'new_messages': new_messages,
        })
