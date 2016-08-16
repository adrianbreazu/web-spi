console.log(time)

// AJAX logic for manual release of sprinkler
$(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('[id$="_button"]').change(function () {
        var dataObject = new Object();
        var sprinklerObject = new Object();
        sprinklerObject.id = $(this).attr('sprinkler_id');
        sprinklerObject.status = $(this).prop('checked');
        dataObject.sprinkler = sprinklerObject;

        request = $.ajax({
            url: $(this).attr('sprinkler_id'),
            method: "POST",
            data: JSON.stringify(dataObject),
            datatype: "json"
        });

        request.done(function(response) {
            //window.alert('done: status: '+ response.sprinkler.status + ' and id: ' + response.sprinkler.id);
            console.log('done: ' + JSON.stringify(response));
        });

        request.fail(function(error) {
            window.alert('failed: '+ JSON.stringify(error));
        });
    });

    $('#submit').click(function () {
        console.log("submit pressed");

        var submit_dataObject = new Object();
        var submit_sprinklerObject = new Object();
        var sprinklers = [];

        submit_dataObject.name =  $("#scheduler_name").val();
        submit_dataObject.start_time = $("#scheduler_start_time").val();
        submit_dataObject.skip = $("#scheduler_skip").val();
        submit_dataObject.days = $("#scheduler_days").val();
        $("#panel_group").children("[id^='sprinkler_main_div_']").each(function() {
            submit_sprinklerObject.id = $(this).children("[id$='_id']").val();
            submit_sprinklerObject.name = $(this).children("[id$='_name']").val();
            submit_sprinklerObject.duration = $(this).children("[id$='_duration']").val();
            submit_sprinklerObject.notes = $(this).children("[id$='_notes']").val();
            sprinklers.push(submit_sprinklerObject);
            submit_sprinklerObject = {};
        });
        submit_dataObject.sprinkler = sprinklers;

        //request = $.post("#", JSON.stringify(submit_dataObject), "json");
        request = $.post("submit", JSON.stringify(submit_dataObject), "json");

        request.fail(function(error) {
            //window.alert('failed on submit: ' + JSON.stringify(error));
            console.log('failed on submit: ' + JSON.stringify(error));
        });
    });
});

// form post request
$(function () {

});