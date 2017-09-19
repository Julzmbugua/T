// NAVBAR REVEAL ON SCROLL

$(function() {
  //caches a jQuery object containing the header element
  var header = $('.mediumnavigation-t');
  $(window).scroll(function() {
    var scroll = $(window).scrollTop();

    if (scroll >= 600) {
      header.removeClass('.mediumnavigation-t').addClass('.mediumnavigation').fadeIn();
    }
    else {
      header.removeClass('.mediumnavigation').addClass('.mediumnavigation-t').fadeIn();
    }
  });
});
// AUTO HIDE NAVBAR TOGGLE

$(".navbar-nav li a").click(function(event) {
    if (!$(this).parent().hasClass('dropdown'))
        $(".navbar-collapse").collapse('hide');
});