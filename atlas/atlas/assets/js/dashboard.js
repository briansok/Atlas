// Mobile nav
$('#js-nav-trigger').on('click', function() {
    var menu = $(this).next();
    menu.toggleClass('show');
});

function getRootUrl() {
	return window.location.origin ? window.location.origin + '/' : window.location.protocol + '/' + window.location.host + '/';
}

$('#search-bar').on('keyup', function(){
		var q = $(this).val();
		var result_el = $('#search-results')


		if (!q) {
			result_el.hide();	
		} else {
			result_el.show();	
		}

    $.ajax({
        type: "get",
        url: getRootUrl() + 'search?q=' + q,
        success: function(data){
            json = JSON.parse(data);
            if (!json) {
							console.log('no results');
            } else {
							parseResults(json);
            }
        },
        error: function(){
            console.log("Something went wrong");
        }
    });
});

function parseResults(json) {
	var result_el = $('#search-results');
	result_el.empty();

	if (json.sections) {
		for (var i in json.sections) {
			var id = json.sections[i].id;
			var title = json.sections[i].title;
			result_el.append('<li class="result"><a href="/location/sections/' + id + '">' + title + '</a></li>');
		}
	}

	if (json.software) {
		for (var i in json.software) {
			var id = json.software[i].id;
			var title = json.software[i].title;
			result_el.append('<li class="result"><a href="/assets/software/' + id + '">' + title + '</a></li>');
		}
	}

    if (json.hardware) {
        for (var i in json.hardware) {
            var id = json.hardware[i].id;
            var title = json.hardware[i].title;
            result_el.append('<li class="result"><a href="/assets/hardware/' + id + '">' + title + '</a></li>');
        }
    }

    // Currently disabled
	// if (json.person_assets) {
	// 	for (var i in json.person_assets) {
	// 		var id = json.person_assets[i].id;
	// 		var title = json.person_assets[i].title;
	// 		result_el.append('<li class="result"><a href="/assets/' + id + '">' + title + '</a></li>');
	// 	}
	// }
}
