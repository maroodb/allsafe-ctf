/**
 * Created by maroodb on 7/3/17.
 */


  placeholders = [ "FIRST NAME", "LAST NAME", "EMAIL", "USERNAME", "PASSWORD", "RETYPE PASSWORD"]
    var i = 0 ;
    $('input[type="text"],input[type="password"],input[type="email"]').each(function () {

        $(this).addClass("form-control s-form-v3__input");
        $(this).attr("placeholder",placeholders[i]);
        i ++ ;
    });
