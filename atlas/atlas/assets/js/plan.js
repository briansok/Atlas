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
            if (json[0]) {
                redirectSection(json);
            } else {
               addSection(event, $x, $y)
            }
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

function addSection(event, $x, $y) {
    var $form = $('#plan-form');

    $popup.css('left',event.pageX);
    $popup.css('top',event.pageY);
    $popup.css('display','inline');
    $popup.css("position", "absolute");

    $('input[name="plan_x"]').val($x);
    $('input[name="plan_y"]').val($y);

    $form.submit(function(){
        $.ajax({
            type:"POST",
            url: getRootUrl() + 'location/plan/set/',
            data: $form.serialize(),
            success: function() {
                console.log('section added');
                $popup.css('display', 'none');
            }
        });
        return false;
    });
}

$el.mouseenter(function(){
    $(this).css('fill', 'red');
    $(this).css('cursor', 'pointer');
});

$el.mouseleave(function(){
    $(this).css('fill', '');
    $(this).css('cursor', '');
});

$('.popup-close').on('click', function(){
    $popup.css('display', 'none');
});
