// Mobile nav
$('#js-nav-trigger').on('click', function() {
    var menu = $(this).next();
    menu.toggleClass('show');
});

