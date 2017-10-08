/**
 * Created by maroodb on 10/7/17.
 */


var doc_urls = $(".urls");

doc_urls.on("click", function () {

    var href = $(this).attr('href');
    params = href.split("?doc=");
    var doc_id = params[1];

    var desc = document.getElementById("doc_description");
    if (desc === null) {
        setTimeout(function () {
            var descriptor = document.getElementById("doc_description");
            if (descriptor !== null) {
                update_Container(doc_id);
            }
        }, 700);
    }
    else {
        setTimeout(function () {
            var descriptor = document.getElementById("doc_description");
            if (descriptor !== null) {
                update_Container(doc_id);
            }
        }, 50);
    }

});


function update_Container(doc_id) {

    $.get("/accounts/library/documents/" + doc_id, function (data, status) {


        if (!data.success) {
            alert("Oops! something gone wrong. Please contact the webmaster.")
        }

        else {

            $("#description").text(data.description);
            $("#uploader").text(data.uploader);
            $("#title").text(data.title);
            $("#date").text(data.date);
            $("#cover_pic").attr('src', data.cover_pic);
            $("#file_url").attr('href', data.url);
        }
    });

}
