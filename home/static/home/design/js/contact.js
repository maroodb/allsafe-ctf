/**
 * Created by maroodb on 7/6/17.
 */


  placeholders = [ "* NAME", "* EMAIL", "* SUBJECT"];
    var i = 0 ;
    $('input[type="text"],input[type="password"],input[type="email"]').each(function () {

        $(this).addClass("form-control s-form-v2__input g-radius--50");
        $(this).attr("placeholder",placeholders[i]);
        //$(this).attr("data-ajax","true");
        i ++ ;
    });


    $('textarea').addClass("form-control s-form-v2__input g-radius--10 g-padding-y-20--xs");
     $('textarea').attr("placeholder",  "* YOUR MESSAGE");
     $('textarea').attr("rows",  "8");


    $('#feedback_form').on('submit', function(event){
    event.preventDefault();
    var form_data = $("#feedback_form").serialize() ;
    post_data(form_data) ;

    });


    function post_data(data) {
         var alert_form = $("#with_error");
         var success_form = $ ("#with_success");
         var spinner = $("#load_spinner");
            alert_form.hide();
            success_form.hide();
            spinner.show();


         ajaxPost('/feedback/',data, function(content){

             var response = JSON.parse(content);
             if ( ! response.robot && response.registered ) {
                 spinner.hide();
                 success_form.show();
             }
             else {
                 spinner.hide();
                 alert_form.show();
             }


            $('#feedback_form').trigger("reset");
             grecaptcha.reset();
        })
    }