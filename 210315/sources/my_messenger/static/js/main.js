let $dialogDOMMessages;

function messageRender(message) {
    let messageDom = $('.message-' + message.pk);
    let textMessage;
    if (!messageDom.length) {
        let messageNew = document.createElement('li');
        messageNew.classList.add('message-' + message.pk);
        textMessage = message.username + " (" + message.created + ") - " + message.text;
        messageNew.innerHTML = textMessage;
        let parent = $dialogDOMMessages.find('.messages-list');
        parent.prepend(messageNew);

    }
}


window.onload = function () {
    console.log('ready');
    $dialogDOMMessages = $('.dialog-messages');
    $dialogDOMMessages.on('click', 'a.dialog-update', function (e) {
        e.preventDefault();
        $.ajax({
            url: e.target.href,
            success: function (response) {
                let messages_new = response.messages_new
                if (messages_new) {
                    messages_new.forEach(function (el, idx) {
                        messageRender(el);
                    })
                }
            }
        })
    })
    setInterval(function(){
        $('.dialog-update').trigger('click');
    }, 5000);
}
