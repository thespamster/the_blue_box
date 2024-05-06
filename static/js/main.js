console.log("main.js loaded"); // REMEMBER TO REMOVE THIS LINE

// When the user scrolls down 250px from the top of the document, show the 'back to the top' button
$( window ).on( "scroll", function() {scrollFunction()});
$("#topButton").click(function() {
    topFunction();
});

function scrollFunction() {
  if (document.body.scrollTop > 250 || document.documentElement.scrollTop > 250) {
      $("#topButton").css("display", "block");
      
  } else {
    topButton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// JS to style the allauth templates

$('input').css('border', 'none')
$('input').css('width', '15rem') 
$(":submit").css("padding", "5px") 
$(":submit").addClass("btn-keep-shopping")

// Change style of account login page
$('#id_password_helptext a').text("Reset")
$('label[for="id_login"]').css("display", "none")
$('label[for="id_password"]').css("display", "none")

// Change style of account signup page
$('label[for="id_email"]').css("display", "none")
$('label[for="id_email2"]').css("display", "none")
$('label[for="id_username"]').css("display", "none")
$('label[for="id_password1"]').css("display", "none")
$('label[for="id_password2"]').css("display", "none")