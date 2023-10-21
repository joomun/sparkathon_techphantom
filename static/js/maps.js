// script.js

var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 6
    });

    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);
}

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the form from refreshing the page

    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer();

    // Get the origin and destination from the form
    var origin = document.getElementById("origin").value;
    var destination = document.getElementById("destination").value;

    // Create a directions request using the form input
    var request = {
        origin: origin,
        destination: destination,
        travelMode: 'DRIVING'
    };

    directionsService.route(request, function(result, status) {
        if (status == 'OK') {
            // Set the directions on the map
            directionsRenderer.setDirections(result);
        } else {
            alert('Directions request failed due to ' + status);
        }
    });

    directionsRenderer.setMap(map); // Set the map for the directionsRenderer
}

// Add event listener to the form
document.getElementById("routeForm").addEventListener("submit", handleFormSubmit);
