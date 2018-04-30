function initMap() {
    var locations = [];
    var labels = [];
    $.get('/data', function(data){
        $(data).each(function(i, dt){
            locations.push({lat:dt.lat, lng:dt.lng});
            labels.push(data.crime_code);
        });
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 11,
            center: {
                lat: 34.1088566,
                lng: -118.4375098
            }
        });
        var markers = locations.map(function(location, i) {
            return new google.maps.Marker({
                position: location,
                label: labels[i]
            });
        });
        var markerCluster = new MarkerClusterer(map, markers, {
            imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
        });
    });
}

