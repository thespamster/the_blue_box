console.log("main.js loaded"); // REMEMBER TO REMOVE THIS LINE

// When the user scrolls down 250px from the top of the document, show the button
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

// Change style of account login page and Google login option
$("#id_password_helptext a").text("Reset")
$('label[for="id_login"]').css("display", "none")
$('label[for="id_password"]').css("display", "none")