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
    post_data() ;

    });


    function post_data() {
         ajaxPost('/feedback/', {'foo': 'bar'}, function(content){
            //onSuccess
            alert(content);
        })
    }