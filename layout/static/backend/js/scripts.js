$(document).ready(function() {
    tinyMCE.init({
        selector: "textarea.editor",
        theme: "modern",
        height : 300,
        plugins: [
            "advlist autolink lists link image charmap print preview hr anchor pagebreak",
            "searchreplace wordcount visualblocks visualchars code fullscreen",
            "insertdatetime media nonbreaking save table contextmenu directionality",
            "emoticons template paste textcolor colorpicker textpattern"
        ],
        toolbar1: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
        toolbar2: "print preview media | forecolor backcolor emoticons| table",
        image_advtab: true
    });

    $(".open-next-div").click(function() {
        var parent = $(this).parent();
        var parent_class = parent.attr('class');

        if(parent_class == "open") {
            parent.removeClass("open");
            $(this).parent().next().hide();
        } else {
            parent.addClass("open");
            $(this).parent().next().show();
        }

    })

    $(".date").datepicker({ dateFormat: 'yy-mm-dd' })
    $(".datetime").datetimepicker({
        dateFormat: "yy-mm-dd",
        timeFormat: "hh:mm:ss",
        timeText: 'Vrijeme',
        hourText: 'Sati',
        minuteText: 'Minute',
        secondText: 'Sekunde',
        currentText: 'Sada',
        closeText: 'Završi',
        dayNames: ['Nedjelja','Ponedjeljak','Utorak','Srijeda','Četvrtak','Petak','Subota'],
        dayNamesShort: ['Ned','Pon','Uto','Sri','Čet','Pet','Sub'],
        dayNamesMin: ['Ned','Pon','Uto','Sri','Čet','Pet','Sub'],
        monthNames: ['Siječanj','Veljača','Ožujak','Travanj','Svibanj','Lipanj','Srpanj','Kolovoz','Rujan','Listopad','Studeni','Prosinac'],
        firstDay: 1
    })

    $(".grid .delete").click(function() {

        var entry_name  = $(this).parent().parent().children("td:nth-child(2)").children().html();

        if(entry_name == null) {
            entry_name  = $(this).parent().parent().children("td:nth-child(2)").html();
        }

        var url = $(this).attr("href");

        $("body").append("<div id='dialog-confirm' title='Potvrda brisanja' class='error'>Jeste li sigurni da \u017eelite obrisati <b>" + entry_name + "</b>?</div>");

        $("#dialog-confirm").dialog({
			resizable: false,
			height:140,
			modal: true,
			buttons: {
				"Da, obri\u0161i zapis": function() {
					window.location = url;
				},
				"Ne, otka\u017ei": function() {
					$(this).dialog("close");
                    $("#dialog-confirm").remove();
				}
			}
		});

        return false;

    })

    $(".autocomplete").each(function() {
        $(this).autocomplete({
            source: $(this).attr("rel"),
            minLength: 2,
            select: function(event,ui) {
                var id_field = $(this).attr("id").replace("_autocomplete", "")
                $("input[id=" + id_field + "]").val(ui.item.id)
            }
        });
    });

    $("input[name=has_title]").change(function() {
        switch_related_field($(this), $("#id_title_order"));
    });

    $("input[name=has_mutations]").change(function() {
        switch_related_field($(this), $("#id_number_of_mutations_order"));
    });

    $("input[name=has_cover]").change(function() {
        switch_related_field($(this), $("#id_turn_on_cover"));
        switch_related_field($(this), $("#id_cover_paper"));
        switch_related_field($(this), $("#id_cover_printer"));
        switch_related_field($(this), $("#id_cover_finish"));
    });

    $("input[name=has_insert]").change(function() {
        switch_related_field($(this), $("#id_insert_paper"));
        switch_related_field($(this), $("#id_insert_press"));
        switch_related_field($(this), $("#id_insert_printer"));
    });

    function switch_related_field(object, parent) {
        var related_select =  parent.parent().parent();
        if(object.is(":checked")) {
            related_select.removeClass("display-none");
        } else {
            related_select.addClass("display-none");
        }
    }

    $("select#id_finish").change(function() {
       var finish_select = $(this);
       var finish_select_value = finish_select.val();
       var finish_type = $("#id_finish_type");
       $("#id_finish_type option:gt(0)").remove();
       var finish_type_initial_option = $("#id_finish_type").html();
       var options = [];

       options.push(finish_type_initial_option);
       $.getJSON("/admin/finish-type/get-type-for-finish", { finish: finish_select_value }, function( data ) {
           $.each( data, function( key, val ) {
               options.push("<option value='" + val["pk"] + "'>" + val["fields"]["name"] + "</option>");
           });
           finish_type.html(options);
       });
    });

    /*
    Cover finish functions
     */

    //$("ul#id_cover_finish").sortable({
    //    stop: function() {
    //        set_finish_order("cover_finish");
    //    }
    //});
    //
    //set_finish_order("cover_finish");
    //
    //$("input[name=cover_finish]").each(function() {
    //    var finish_object = $(this);
    //    get_finish_type_options(finish_object, "cover_finish_type");
    //    is_finish_on(finish_object, "cover_finish");
    //});
    //
    //$("input[name=cover_finish]").change(function() {
    //    var finish_object = $(this);
    //    get_finish_type_options(finish_object, "cover_finish_type");
    //    is_finish_on(finish_object, "cover_finish");
    //});



    /*
    Finish functions
     */

    // finish functions
    $("ul#id_finish").sortable({
        stop: function() {
            set_finish_order("finish");
        }
    });

    $("ul#id_cover_finish").sortable({
        stop: function() {
            set_finish_order("cover_finish");
        }
    });

    function set_finish_order(name) {
        var list_of_values = [];
        $("ul#id_" +  name + " li input[name=" + name + "]").each(function() {
            var value = $(this).attr("value");
            if(value) {
                list_of_values.push(value);
            }
        });
        $("input#id_" + name + "_order").val(list_of_values.join())
    }

    $("input[name=finish]").change(function() {
        var finish_object = $(this);

        if(finish_object.is(":checked")) {
            finish_object.nextAll("label").show();
            finish_object.nextAll("ul").show();
        } else {
            finish_object.nextAll("label").hide();
            finish_object.nextAll("ul").hide();
        }
    });

    $("input[name=cover_finish]").change(function() {
        var finish_object = $(this);

        if(finish_object.is(":checked")) {
            finish_object.nextAll("label").show();
            finish_object.nextAll("ul").show();
        } else {
            finish_object.nextAll("label").hide();
            finish_object.nextAll("ul").hide();
        }
    });
});
