var socket = null

function append_chat_content(msg){
    var d = new Date()
    t = d.toLocaleTimeString();
    $('#chat_area').prepend('<p><span>' + t + ":" + msg + '</span></p>');
}

function connect(){
    append_chat_content("正在连接..");
    var socket = io.connect('http://' + document.domain + ':' + location.port, {"timeout": 2000});
    socket.on('connect', function(msg) {
        append_chat_content("服务器已连接");
        socket.emit('connect_cb');
    });
    socket.on('chat_recieve', function(msg) {
        append_chat_content(msg.content);
    });
    $('form#chat').submit(function(event) {
        socket.emit('chat_push', {data: $('#chat_data').val()});
        return false;
    });
};


angular.module('meican_helper', [])
  .controller('MeicanLoginController', function($scope, $http) {
    var helper = this;
    var login_data = null
    helper.is_login = function(){
        return login_data != null
    }
    helper.login = function() {
        console.log(helper.login_psw)
        var data = JSON.stringify({acc: helper.login_acc, pwd: helper.login_psw})
        $http({
            url: "/login_meican",
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            data: data})
        .success(function(data) {
            console.log(data)
            for (day in data){
                for (sub_type in data[day]){
                    $("#food_list_already").append("<p>"+sub_type+'</p>')
                    for (item in data[day][sub_type]){
                        var it = data[day][sub_type][item]
                        $("#food_list_already").append("<p>"+it+'</p>')
                    }
                }
            }
        });
    };
  });
