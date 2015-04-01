$(function() {
  // initialize scrollable
  $("#main-slider .scrollable").scrollable({speed: 1000, circular: true}).navigator().autoscroll({ interval: 5000, autoplay: true });
  $("#news-slider .scrollable").scrollable({speed: 1000, circular: true}).navigator().autoscroll({ interval: 5000, autoplay: true });
});

$(document).ready(function() {
    $("body").click(function() {
        $('div.drop-down-menu').hide();
    })

    $("#login-button").click(function() {
         $('#login-form').toggle();
        return false;
    })


    $("a.drop-down-menu").click(function() {
        $('div.drop-down-menu').toggle();
        return false;
    });


    $("#product-cart-form input").keyup(function() {
        calculate_price();
    });


    $("#product-cart-form input[type=checkbox]").change(function() {
        calculate_price();
    });

    $("#product-cart-form select").change(function() {
        calculate_price();
    });

    function calculate_price() {
        var form_data = $("#product-cart-form").serialize();
        $.post("/product/calculate-price", form_data).done(function(data) {
            $("#product-price").html(data.product_price);
        });
    }
})