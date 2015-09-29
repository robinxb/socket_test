function append_chat_content(msg){
    $('#chat_area').append('<p><span>' + msg + '</span></p>');
}

$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port, {"timeout": 2000});
    socket.on('connect', function(msg) {
        append_chat_content("你已进入聊天");
    });
    socket.on('chat_recieve', function(msg) {
        console.log(msg);
        append_chat_content(msg.content);
    });
    $('form#chat').submit(function(event) {
        socket.emit('chat_push', {data: $('#chat_data').val()});
        return false;
    });
});
