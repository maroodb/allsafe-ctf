/**
 * Created by maroodb on 8/8/17.
 */


    var placeholders = ["Your Name", "Your Email"];
    var i = 0;

    $('input[type="text"],input[type="email"]').each(function () {

        $(this).addClass("form-control s-form-v4__input");
        $(this).attr("placeholder", placeholders[i]);

        i++;
    });


    $('#newslettre_form').on('submit', function (event) {
        event.preventDefault();
        var form_data = $("#newslettre_form").serialize();
        post_data(form_data);

    });

    function post_data(form_data) {
         var alert_form = $("#with_error");
         var success_form = $ ("#with_success");
         var spinner = $("#load_spinner");
            alert_form.hide();
            success_form.hide();
            spinner.show();

        $.post("/magazine/newslettre/",form_data,
        function(data, status){
            spinner.hide();
             if (data.success) {
                 success_form.show();

             }
             else if (data.is_registered) {

                 alert_form.removeClass("alert-danger");
                 alert_form.addClass("alert-warning");
                 alert_form.text(data.error);
                 alert_form.show();
             }
             $('#newslettre_form').trigger("reset");
        });
    }



