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
        switch_related_field($(this), $("#id_cover_paper"));
        switch_related_field($(this), $("#id_cover_plastic"));
        switch_related_field($(this), $("#id_cover_paper_order"));
        switch_related_field($(this), $("#id_cover_plastic_order"));
    });

    $("input[name=has_insert]").change(function() {
        switch_related_field($(this), $("#id_insert_paper"));
        switch_related_field($(this), $("#id_insert_paper_order"));
    });


    $("input[name=has_cutting]").change(function() {
        switch_related_field($(this), $("#id_cutting_order"));
    });

    $("input[name=has_improper_cutting]").change(function() {
        switch_related_field($(this), $("#id_improper_cutting_order"));
    });

    $("input[name=has_creasing]").change(function() {
        switch_related_field($(this), $("#id_creasing_order"));
    });

    $("input[name=has_hole_drilling]").change(function() {
        switch_related_field($(this), $("#id_hole_drilling_order"));
    });

    $("input[name=has_vacuuming]").change(function() {
        switch_related_field($(this), $("#id_vacuuming_order"));
    });

    $("input[name=has_binding]").change(function() {
        switch_related_field($(this), $("#id_bindings"));
        switch_related_field($(this), $("#id_bindings_order"));
    });

    $("input[name=has_flexion]").change(function() {
        switch_related_field($(this), $("#id_flexion"));
        switch_related_field($(this), $("#id_flexion_order"));
    });

    $("input[name=has_laminating]").change(function() {
        switch_related_field($(this), $("#id_laminating_order"));
    });

    $("input[name=has_plastic]").change(function() {
        switch_related_field($(this), $("#id_plastic"));
        switch_related_field($(this), $("#id_plastic_order"));
    });

    $("input[name=has_rounding]").change(function() {
        switch_related_field($(this), $("#id_rounding_order"));
    });

    function switch_related_field(object, parent) {
        var related_select =  parent.parent().parent();
        if(object.is(":checked")) {
            related_select.removeClass("display-none");
        } else {
            related_select.addClass("display-none");
        }
    }

});
