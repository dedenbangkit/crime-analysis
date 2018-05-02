function initMap() {
    var locations = [];
    var contents = [];
    $.get("/api/data", function(data) {
        $(data).each(function(i, dt) {
            locations.push({
                lat: dt.lat,
                lng: dt.lng,
            });
            contents.push(dt);
        });
        mapstyle = [{
                "featureType": "administrative",
                "elementType": "labels.text.fill",
                "stylers": [{
                    "color": "#444444"
                }]
            },
            {
                "featureType": "landscape",
                "elementType": "all",
                "stylers": [{
                    "color": "#f2f2f2"
                }]
            },
            {
                "featureType": "poi",
                "elementType": "all",
                "stylers": [{
                    "visibility": "off"
                }]
            },
            {
                "featureType": "road",
                "elementType": "all",
                "stylers": [{
                        "saturation": -100
                    },
                    {
                        "lightness": 45
                    }
                ]
            },
            {
                "featureType": "road.highway",
                "elementType": "all",
                "stylers": [{
                    "visibility": "simplified"
                }]
            },
            {
                "featureType": "road.arterial",
                "elementType": "labels.icon",
                "stylers": [{
                    "visibility": "off"
                }]
            },
            {
                "featureType": "transit",
                "elementType": "all",
                "stylers": [{
                    "visibility": "off"
                }]
            },
            {
                "featureType": "water",
                "elementType": "all",
                "stylers": [{
                        "color": "#ffffff"
                    },
                    {
                        "visibility": "on"
                    }
                ]
            }
        ]
        var map = new google.maps.Map(document.getElementById("map"), {
            zoom: 11,
            center: {
                lat: 34.1088566,
                lng: -118.4375098,
            },
            styles: mapstyle
        });
        map.addListener("click", function() {
            $("#detail-info").slideUp("fast");
        });

        /* var color = 'green';
        sets = {fillColor:color, strokeColor:color, strokeWeight:1
        map.data.loadGeoJson('/static/scripts/la.json')
        map.data.setStyle(function(feature){return (sets) */

        var markers = locations.map(function(location, i) {
            var mark = new google.maps.Marker({
                position: location,
                content: contents[i],
            });
            mark.addListener("click", function() {
                var dt = this.content;
                console.log(dt);
                $("#detail-info").slideDown("fast", function() {
                    $this = $(this);
                    $this.find("h1").text(dt.crime_desc);
                    if (dt.victim_sex !== null) {
                        var sex;
                        if (dt.victim_sex === "F") {
                            sex = "Female";
                        } else {
                            sex = "Male";
                        }
                        new google.maps.StreetViewPanorama(document.getElementById('pano'), {
                            position: location,
                            addressControl: false,
                            fullscreenControl: false,
                            linksControl: false,
                            panControl: false,
                            enableCloseButton: false
                        });
                        $this.find(".lead .victim").text(sex + ", " + dt.victim_age);
                    }
                    $this.find(".lead .address").text(dt.address + ", " + dt.area);
                    $this.find(".lead .reported").text(convertDate(dt.date_reported));
                    $this.find(".lead .occured").text(convertDate(dt.date_occured));
                    $this.find("a").attr("href", "https://google.com/search?&q=" + dt.crime_desc + " " + dt.address + " " + dt.date_reported);
                });
            });
            return mark;
        });
        var markerCluster = new MarkerClusterer(map, markers, {
            imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
            maxZoom: 15,
        });
    });
}

function convertDate(date) {
    return moment(new Date(date)).format("dddd, Do MMM YYYY");
}
