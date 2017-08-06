/**
 * Created by maroodb on 7/31/17.
 */


$('input[type="text"], input[type="number"]').each(function(){
        $(this).attr("class", "form-control todo-taskbody-tasktitle");

    });

$('select').attr("class", "form-control todo-taskbody-tags");
