$(function() {
  // initialize scrollable
  $("#main-slider .scrollable").scrollable({speed: 1000, circular: true}).navigator().autoscroll({ interval: 5000, autoplay: true });
  $("#news-slider .scrollable").scrollable({speed: 1000, circular: true}).navigator().autoscroll({ interval: 5000, autoplay: true });
});

$(document).ready(function() {
//    $("body").click(function() {
//        $('#login-form').hide();
//    })

    $("#login-button").click(function() {
         $('#login-form').toggle();
        return false;
    })
})