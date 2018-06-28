var $el = $('.plan-image rect');
var $popup = $('#plan-popup');

$el.on('click', function(event){
    var $x = $(this).attr('x');
    var $y = $(this).attr('y');

    $.ajax({
        type: "get",
        url: getRootUrl() + 'location/plan/?plan_x=' + $x + "&plan_y=" + $y,
        success: function(data){
            json = JSON.parse(data);
            openSection(event, json, $x, $y);
        },
        error: function(){
            console.log("Something went wrong");
        }
    });
});

function getRootUrl() {
	return window.location.origin ? window.location.origin + '/' : window.location.protocol + '/' + window.location.host + '/';
}

function redirectSection(json) {
    if (json[0]['pk'] !== undefined) {
        var $id = json[0]['pk'];
        window.location.href = getRootUrl() + 'location/sections/' + $id;
    }
}

function openSection(event, json, $x, $y) {
    console.log('open');
    $popup.css('left',event.pageX);
    $popup.css('top',event.pageY);
    $popup.css('display','inline');
    $popup.css("position", "absolute");

    $.ajax({
        type:"GET",
        url: getRootUrl() + 'location/plan/get/',
        data: {'x': $x, 'y': $y},
        success: function(data) {
            console.log(data);
            if (data.x == 'none') {
                addSection(event, $x, $y);
            } else {
                json = JSON.parse(data);
                if (json[0].fields.plan_x > 0 && json[0].fields.plan_y > 0) {
                    editSection(event, json, json[0].fields.plan_x, json[0].fields.plan_y);
                }
            }
        }
    });
    return false;
}

function editSection(event, $x, $y) {
    var $redirect = $('#plan-redirect');
    $('#plan-edit-form').show();
    $('#plan-add-form').hide();

    $('#plan-delete').on('click', function(){
        $.ajax({
            type:"POST",
            url: getRootUrl() + 'location/plan/delete/',
            data: {'x': $x, 'y': $y},
            success: function() {
                console.log('luckt');
            }
        });
        return false;
    });
    $redirect.on('click', function(){
        redirectSection(json)
    });
}

function addSection(event, $x, $y) {
    $('#plan-add-form').show();
    $('#plan-edit-form').hide();

    $('input[name="plan_x"]').val($x);
    $('input[name="plan_y"]').val($y);

    $form.submit(function(){
        $.ajax({
            type:"POST",
            url: getRootUrl() + 'location/plan/set/',
            data: $form.serialize(),
            success: function() {
                $popup.css('display', 'none');
                $('.messages').append('<li class="info">Success</li>');
            }
        });
        return false;
    });
}

$el.mouseenter(function(){
    $(this).css('fill', '#05d669');
    $(this).css('cursor', 'pointer');
});

$el.mouseleave(function(){
    $(this).css('fill', '');
    $(this).css('cursor', '');
});

$('.popup-close').on('click', function(){
    $popup.css('display', 'none');
});
