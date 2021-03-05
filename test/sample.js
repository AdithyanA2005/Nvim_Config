console.log("welcome adi")

function updateMap() {
    console.log("Updating map with realtime data")
    fetch("assets/json/data.json")
        .then(response => response.json())
        .then(rsp => {
            console.log(rsp.data)
            rsp.data.forEach(element => {

                // Variables from the data.json 
                latitude = element.latitude;
                longitude = element.longitude;
                cases = element.infected;
                dead = element.dead;
                recovered = element.recovered;

                // Color scheme of the map
                if (recovered <= dead) {
                    // color = `rgb(${cases}, 0, 0)`;
                    color = "rgb(255, 0, 0)";
                }
                else if (dead < recovered) {
                    // color = `rgb(0, ${recovered}, 0)`;
                    color = "rgb(0, 255, 0)";

                }
                else {
                    color = `rgb(0, ${recovered}, 0)`;
                }

                // Poineter on the map
                new mapboxgl.Marker({
                    draggable: false,
                    color: color
                }).setLngLat([longitude, latitude])
                    .addTo(map);
            });
        })
} updateMap()

// When the data is collected from a API in forn of json file then this will reload the function in every 20-seconds
let interval = 20000;
setInterval(updateMap, interval);
