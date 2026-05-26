

var fill = document.getElementById('progressFill');

if (fill) {
  fill.style.width = fill.dataset.progress + '%';
}


/* Read values from HTML instead of raw Jinja in JS */

const startLat=
parseFloat(
"0"
);

const startLon=
parseFloat(
"0"
);

const endLat=
parseFloat(
"0"
);

const endLon=
parseFloat(
"0"
);



var map=L.map(
'map'
).setView(

[startLat,startLon],

13

);


L.tileLayer(

'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',

{
attribution:
'OpenStreetMap'
}

).addTo(map);



L.marker(
[startLat,startLon]
)

.addTo(map)

.bindPopup(
"Start"
);



L.marker(
[endLat,endLon]
)

.addTo(map)

.bindPopup(
"Destination"
);



var route=L.polyline(

[

[startLat,startLon],

[endLat,endLon]

],

{

color:'#00ff90',

weight:6

}

)

.addTo(map);


map.fitBounds(
route.getBounds()
);


setTimeout(

()=>{

map.invalidateSize()

},

100

)

