console.log("main.js loaded"); // REMEMBER TO REMOVE THIS LINE

// When the user scrolls down 100px from the top of the document, show the button
$( window ).on( "scroll", function() {scrollFunction()});
$("#topButton").click(function() {
    topFunction();
});

function scrollFunction() {
  if (document.body.scrollTop > 250 || document.documentElement.scrollTop > 250) {
    topButton.style.display = "block";
  } else {
    topButton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}