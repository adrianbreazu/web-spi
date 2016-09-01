// AJAX logic for getting a new read on temperature and humidity
$(function () {
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

    $('#get-temperature-and-humidity').click(function () {
        console.log("click")
        var dataObject = new Object();
        dataObject.sessionid = 1;

        request = $.ajax({
            url: "temp",
            method: "POST",
            data: JSON.stringify(dataObject),
            datatype: "json"
        });

        request.done(function(response) {
            //window.alert('done: status: '+ response.sprinkler.status + ' and id: ' + response.sprinkler.id);
            temperature = String(response.temperature);
            humidity = String(response.humidity);
            $('#temperature').val(temperature + " *C");
            $('#humidity').val(humidity + " %");
        });

        request.fail(function(error) {
            window.alert('failed: '+ JSON.stringify(error));
        });
    });
});