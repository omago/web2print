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
    })


//    $(".autocomplete").click(function() {
//        alert($(this).attr("rel"))
//    })


//    $("#add_new_key").click(function() {
//
//        $("#dialog-form").remove();
//        $("body").append("<div id='dialog-form' title='Dodavanje ključa'>" +
//            "<div class='dialog_form'>" +
//                "Molimo upišite naziv ključa<br /><br />" +
//                "<label>Naziv</label>" +
//                "<input type='text' id='key_name' name='key_name'>" +
//            "</div></div>");
//
//        $("#dialog-form").dialog({
//			resizable: false,
//			height: 182,
//			modal: true,
//			buttons: {
//                "Dodaj ključ": function() {
//
//                    var dialog = $(this);
//
//                    var value = $("input#key_name").val()
//                    var valid = validate(value, 'a-zA-Z1234567890_-');
//
//                    $("#dialog-form div.error").remove();
//
//                    if(valid) {
//                        $.ajax({
//                            url: "/system-configuration/add_key/",
//                            dataType: "json",
//                            data: {
//                                key: value
//                            },
//                            success: function( data ) {
//                                if(data.success){
//                                    $(".no-keys-defined").remove();
//                                    $("#form").append("<div>" +
//                                        "<label for='id_" + value + "'>" + value + "</label>" +
//                                        "<div>" +
//                                            "<input id='id_" + value + "' name='" + value + "' type='text' value=''></div>" +
//                                            "<a class='delete-key' data-key='" + value + "' title='Obriši ključ'></a>" +
//                                        "</div>");
//                                    dialog.dialog("close");
//                                } else {
//                                    $("input#key_name").after("<div class='error'>" + data.error + "</div>")
//                                }
//                            }
//                        });
//                    } else {
//                        $("input#key_name").after("<div class='error'>Dozvoljeni su samo alfanumerički znakovi</div>")
//                    }
//
//				},
//                "Odustani": function() {
//					$(this).dialog("close");
//                    $("#dialog-form").remove();
//				}
//			}
//		})
//    })

//    function validate(value, allowed_chars){
//        var reg = new RegExp('^[' + allowed_chars + ']+$');
//        var valid = reg.test(value);
//        return valid;
//    }

//    $(document).on("click", ".delete-key", function() {
//        var clicked_key = $(this);
//        var value = clicked_key.data("key");
//
//        $.ajax({
//            url: "/system-configuration/remove_key/",
//            dataType: "json",
//            data: {
//                key: value
//            },
//            success: function( data ) {
//                if(data.success) {
//                    $.when(clicked_key.parent().remove()).then(add_no_key_div());
//                }
//            }
//        });
//    })
//
//    function add_no_key_div() {
//        if($("#form div").length == 0) {
//            $("#form").append("<div class='no-keys-defined margin-10'>Nema definiranih ključeva</div>")
//        }
//
//    }

});
