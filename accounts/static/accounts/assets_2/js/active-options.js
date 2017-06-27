$(document).ready(function(){
    


var dashboard = $("#dash") ;
var activePosition = $("#l1");

dashboard.click(function(event){

	var clickedId = event.target.id ;
	var clickedElement = $("#"+clickedId);
    var liElement = clickedElement.parent().parent();
    activePosition.removeClass("active");
    liElement.addClass("active");

    activePosition = liElement ;
    

    
    
    
  
}); 


























});