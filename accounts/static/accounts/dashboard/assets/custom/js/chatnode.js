/**
 * Created by maroodb on 8/5/17.
 */
function creatChatElement(data, type_of_msg) {


    var host = window.location.hostname;
    var forme_date = new Date(data.date) + "";
    var time = forme_date.split("GMT")[0];
    var arrow = '<span class="arrow" > </span>';
    var img = $("<img/>");
    var li = $("<li></li>");
    var divmsg = $("<div></div>");
    var spandate = $("<span></span>");
    var spanbody = $("<span></span>");
    var aname = $("<a></a>");

    aname.attr("href", "#");
    aname.attr("class", "name");
    aname.text(data.username);


    spanbody.text(data.text);
    spanbody.attr("class", "body");
    spandate.text(" at " + time);
    spandate.attr("class", "datetime");
    divmsg.attr("class", "message");
    if (host == "127.0.0.1"){
        img.attr("src", "http://" + host + ":8000" + data.avatar);
    }
    else {
        img.attr("src", "http://" +host+ data.avatar);
    }

    img.attr("class", "avatar");


    divmsg.append(arrow, aname, spandate, spanbody);
    li.append(img, divmsg);
    li.attr("class", type_of_msg);

    return li;


}
function appendChatElement(message) {
    if (message.username === username.text()) {

        queue.append(creatChatElement(message, "out"));
    }
    else {
        queue.append(creatChatElement(message, "in"));
    }
    $("#rolette").scrollTop(queue[0].scrollHeight);
}

var username = $("#username");
var avatar = $("#avatar");
var socket = io.connect('http://chatroom.allsafeclub.info');
var box = $('#chatbox');
var queue = $("#chatlist");
var writing = $("#iswriting");
var is_writing = 0;
var timer = null;


var message = {
    "username": username.text(),
    "avatar": avatar.text(),
    "text": "None",
    "date": "None"
};

/* Events handler */
socket.on('message', function (message) {

    writing.hide();
    appendChatElement(message) ;

});


socket.on('update_your_list', function (listOfMessages) {

    Object.keys(listOfMessages).forEach(function (key, v) {
        var msgDate = new Date(parseInt(key));
        var messageFromDataBase = listOfMessages[key] ;
        messageFromDataBase.date = msgDate;

        appendChatElement(messageFromDataBase);

    });
});

socket.on('writing', function (someone) {

    writing.show();
    clearInterval(timer);
    timer = setTimeout(function () {
        writing.hide();
    }, 1500);
});

/* End Events handler */
$('#formulaire_chat').submit(function () {

    is_writing = 0;
    date = new Date();
    message.text = box.val();
    message.date = date.getTime();


    socket.emit('chatroom', message);

    box.val('').focus();

    return false;
});

/* Writing event */


box.keydown(function () {

    is_writing++;
    if (is_writing > 1) {
        socket.emit('is_writing', username.text());
    }


});


