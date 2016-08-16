// logic for populating days of the week
var days_of_the_week = $('#scheduler_days').val();
if (days_of_the_week[0] === "M")
    $('#checkbox_Monday').prop('checked', true);
else
    $('#checkbox_Monday').prop('checked', false);

if (days_of_the_week[1] === "T")
    $('#checkbox_Tuesday').prop('checked', true);
else
    $('#checkbox_Tuesday').prop('checked', false);

if (days_of_the_week[2] === "W")
    $('#checkbox_Wednesday').prop('checked', true);
else
    $('#checkbox_Wednesday').prop('checked', false);

if (days_of_the_week[3] === "T")
    $('#checkbox_Thursday').prop('checked', true);
else
    $('#checkbox_Thursday').prop('checked', false);

if (days_of_the_week[4] === "F")
    $('#checkbox_Friday').prop('checked', true);
else
    $('#checkbox_Friday').prop('checked', false);

if (days_of_the_week[5] === "S")
    $('#checkbox_Saturday').prop('checked', true);
else
    $('#checkbox_Saturday').prop('checked', false);

if (days_of_the_week[6] === "S")
    $('#checkbox_Sunday').prop('checked', true);
else
    $('#checkbox_Sunday').prop('checked', false);

if ($('#checkbox_Monday').prop('checked') && $('#checkbox_Tuesday').prop('checked') && $('#checkbox_Wednesday').prop('checked') && $('#checkbox_Thursday').prop('checked') && $('#checkbox_Friday').prop('checked') && $('#checkbox_Saturday').prop('checked') && $('#checkbox_Sunday').prop('checked'))
    $('#checkbox_all').prop('checked', true);
else
    $('#checkbox_all').prop('checked', false);

// logic for all days of the week
$('#checkbox_all').change(function () {
    if ($('#checkbox_all').prop('checked')) {
        $('#checkbox_Monday').prop('checked', true);
        $('#checkbox_Tuesday').prop('checked', true);
        $('#checkbox_Wednesday').prop('checked', true);
        $('#checkbox_Thursday').prop('checked', true);
        $('#checkbox_Friday').prop('checked', true);
        $('#checkbox_Saturday').prop('checked', true);
        $('#checkbox_Sunday').prop('checked', true);
        $('#scheduler_days').val('MTWTFSS');
        console.log("111" + days_of_the_week);
    } else {
        $('#checkbox_Monday').prop('checked', false);
        $('#checkbox_Tuesday').prop('checked', false);
        $('#checkbox_Wednesday').prop('checked', false);
        $('#checkbox_Thursday').prop('checked', false);
        $('#checkbox_Friday').prop('checked', false);
        $('#checkbox_Saturday').prop('checked', false);
        $('#checkbox_Sunday').prop('checked', false);
        $('#scheduler_days').val('-------');
        console.log("2222" + days_of_the_week);
    }


$('[id$="day"]').change(function () {
    console.log("begin" + days_of_the_week);
    if ($('#checkbox_Monday').prop('checked') && $('#checkbox_Tuesday').prop('checked') && $('#checkbox_Wednesday').prop('checked') && $('#checkbox_Thursday').prop('checked') && $('#checkbox_Friday').prop('checked') && $('#checkbox_Saturday').prop('checked') && $('#checkbox_Sunday').prop('checked'))
        $('#checkbox_all').prop('checked', true);
    else
        $('#checkbox_all').prop('checked', false);

    switch ($(this).attr('id')) {
        case "checkbox_Monday":
            if ($('#checkbox_Monday').prop('checked')) {
                days_of_the_week = 'M' + days_of_the_week.substr(1);
            } else {
                days_of_the_week = '-' + days_of_the_week.substr(1);
            }
        case "checkbox_Tuesday":
           if ($('#checkbox_Tuesday').prop('checked')) {
                days_of_the_week = days_of_the_week.substr(0,1) + 'T' + days_of_the_week.substr(2);
            } else {
                days_of_the_week =  days_of_the_week.substr(0,1) + '-' + days_of_the_week.substr(2);
            }
        case "checkbox_Wednesday":
           if ($('#checkbox_Wednesday').prop('checked')) {
                days_of_the_week =  days_of_the_week.substr(0,2) + 'W' + days_of_the_week.substr(3);
            } else {
                days_of_the_week =  days_of_the_week.substr(0,2) + '-' + days_of_the_week.substr(3);
            }
        case "checkbox_Thursday":
           if ($('#checkbox_Thursday').prop('checked')) {
                days_of_the_week =  days_of_the_week.substr(0,3) + 'T' + days_of_the_week.substr(4);
            } else {
                days_of_the_week =  days_of_the_week.substr(0,3) + '-' + days_of_the_week.substr(4);
            }
        case "checkbox_Friday":
           if ($('#checkbox_Friday').prop('checked')) {
                days_of_the_week =  days_of_the_week.substr(0,4) + 'F' + days_of_the_week.substr(5);
            } else {
                days_of_the_week =  days_of_the_week.substr(0,4) + '-' + days_of_the_week.substr(5);
            }
        case "checkbox_Saturday":
           if ($('#checkbox_Saturday').prop('checked')) {
                days_of_the_week =  days_of_the_week.substr(0,5) + 'S' + days_of_the_week.substr(6);
            } else {
                days_of_the_week =  days_of_the_week.substr(0,5) + '-' + days_of_the_week.substr(6);
            }
        case "checkbox_Sunday":
           if ($('#checkbox_Sunday').prop('checked')) {
                days_of_the_week =  days_of_the_week.substr(0,6) + 'S';
            } else {
                days_of_the_week =  days_of_the_week.substr(0,6) + '-';
            }
    }
    $('#scheduler_days').val(days_of_the_week);
    console.log("end" + days_of_the_week);
});
});