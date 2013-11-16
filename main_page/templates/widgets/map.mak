<div id="map" style="height: 400px;"></div>
<script>
head.js(leaflet, function() {
    var map = L.map('map').setView([${x},${y}], ${z});
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png',
        {attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
    % if value:
        L.marker([${x},${y}]).addTo(map).bindPopup("${value}")
    % endif
});
</script>
