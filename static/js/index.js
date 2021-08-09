var map;
map = new google.maps.Map(document.getElementById('map'), {
	center: {lat: 36.2048, lng: 138.2529},
	zoom: 5
});

var server_url;
$.ajaxSetup({async: false});
$.getJSON("static/config/config.json", function(data){
	server_url = data.server_url;
});
$.ajaxSetup({async: true});


function execSmoothZoom(){
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: 36.2048, lng: 138.2529},
		zoom: 5
	});
	const url = new URL(server_url + "/api/get_random_city");
    fetch(url)
	    .then(response => response.json())
	    .then(data => {
			console.log(data)
			document.getElementById("destination").innerHTML = data.name;
			document.getElementById("pos_lat").innerHTML = data.lat;
			document.getElementById("pos_lng").innerHTML = data.lng;
    		map.panTo(new google.maps.LatLng(data.lat, data.lng));
    		smoothZoom(map, 16, map.getZoom());
		})
}


// the smooth zoom function
function smoothZoom (map, max, cnt) {
	if (cnt >= max) {
		return;
	}
	else {
		z = google.maps.event.addListener(map, 'zoom_changed', function(event){
			google.maps.event.removeListener(z);
			smoothZoom(map, max, cnt + 1);
		});
		setTimeout(function(){map.setZoom(cnt)}, 250);
	}
}
