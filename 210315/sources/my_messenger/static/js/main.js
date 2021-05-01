window.onload = function () {
    console.log('ready');
    $('.dialog-messages').on('click', 'dialog-update', function (e) {
        e.preventDefault();
        $.ajax( {
            url: e.target.href,
            success: function (response){
                console.log(response);
            }
        })
    })
}