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

    $("#id_format_choices").change(function() {
        var _this = $(this);
        if(_this.val() == "custom") {
            var dialog_html =
            '<div id="dialog-form" title="Dodaj novi format">' +
                '<form>' +
                    '<fieldset>' +
                        '<div><label for="user_format_width">Širina (mm)</label><input type="text" name="user_format_width" id="user_format_width" /><div class="error"></div></div>' +
                        '<div><label for="user_format_height">Visina (mm)</label><input type="text" name="user_format_height" id="user_format_height" /><div class="error"></div></div>' +
                        '<div><label for="user_format_add_to_my_formats">Dodaj u moje formate</label><input type="checkbox" name="user_format_add_to_my_formats" id="user_format_add_to_my_formats" /></div>' +
                        '<input type="submit" tabindex="-1" style="position:absolute; top:-1000px">' +
                    '</fieldset>' +
                '</form>' +
            '</div>';

            $("body").append(dialog_html);
            var dialog = $("#dialog-form").dialog({
                height: 270,
                width: 350,
                modal: false,
                resizable: false,
                buttons: {
                    "Dodaj format": addUserFormat,
                    "Odustani": function() {
                        dialog.dialog( "close" );
                    }
                },
                close: function() {
                    form[ 0 ].reset();
                    allFields.removeClass( "ui-state-error" );
                }
            });
        }
    });

    function addUserFormat() {
        var user_format_width = $("#user_format_width");
        var user_format_height = $("#user_format_height");
        var user_format_add_to_my_formats = $("#user_format_add_to_my_formats");
        var product_id = $("#id_product");
        var error = false;

        var user_format_width_value = user_format_width.val();
        var user_format_height_value = user_format_height.val();
        var product_id_value = product_id.val();

        user_format_width.next().html("");
        user_format_height.next().html("");

        if(!isInt(user_format_width_value)) {
            user_format_width.next().html("Molimo upišite broj veći od nule");
            error = true;
        }

        if(!isInt(user_format_height_value)) {
            user_format_height.next().html("Molimo upišite broj veći od nule");
            error = true;
        }

        if(error == false) {
            var option_list = [];
            $("#id_format_choices option").each(function() {
                if($(this).attr("value") != "") {
                    option_list.push($(this).attr("value"))
                }
            });

            var user_format_add_to_my_formats_value = 0;
            if(user_format_add_to_my_formats.is(":checked"))
                user_format_add_to_my_formats_value = 1;

            $.get("/format/add-format", {
                product_id: product_id_value,
                user_format_width: user_format_width_value,
                user_format_height: user_format_height_value,
                user_format_add_to_my_formats: user_format_add_to_my_formats_value
            }).done(function(data) {
                if(data.format_type == "new" && option_list.indexOf(data.id.toString()) == -1) {
                    $('<option value="' + data.id + '">' + data.label + '</option>').insertBefore($("#id_format_choices option[value=custom]"));
                }
                $("#id_format_choices").val(data.id);
                $("#dialog-form").remove();
            });
        }
    }

    function isInt(value) {
        var x = parseFloat(value);
        return !isNaN(value) && (x | 0) === x && x > 0;
    }

    $("input[name=has_cover]").change(function() {
        switch_related_field($(this), $("#id_cover_paper"));
        switch_related_field($(this), $("#id_cover_plastic"));
    });

    $("input[name=has_insert]").change(function() {
        switch_related_field($(this), $("#id_number_of_inserts"));
        switch_related_field($(this), $("#id_has_insert_print"));

        if($(this).is(":checked")) {
            switch_related_field($("input[name=has_insert_print]"), $("#id_insert_paper"));
            switch_related_field($("input[name=has_insert_print]"), $("#id_insert_press"));
            switch_related_field($("input[name=has_insert_print]"), $("#id_insert_volume"));
        } else {
            switch_related_field($(this), $("#id_insert_paper"));
            switch_related_field($(this), $("#id_insert_press"));
            switch_related_field($(this), $("#id_insert_volume"));
        }


    });

    $("input[name=has_insert_print]").change(function() {
        switch_related_field($(this), $("#id_insert_paper"));
        switch_related_field($(this), $("#id_insert_press"));
        switch_related_field($(this), $("#id_insert_volume"));
    });

    function switch_related_field(object, parent) {
        var related_select =  parent.parent().parent();
        if(object.is(":checked")) {
            related_select.removeClass("display-none");
        } else {
            related_select.addClass("display-none");
        }
    }

    $(".checkbox-select input").change(function() {
        var object = $(this);
        if(object.is(":checked")) {
            object.next("select").show();
        } else {
            object.next("select").hide();
        }
    })
});