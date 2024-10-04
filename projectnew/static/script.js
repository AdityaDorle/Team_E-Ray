// Initialize the map and set its view to Germany
var map = L.map('map').setView([51.1657, 10.4515], 6);

// Add a tile layer (map layer)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Array of lakes with coordinates and names
var lakes = [
    { name: "Lake Constance", coords: [47.654, 9.204] },
    { name: "Lake Chiemsee", coords: [47.866, 12.400] },
    { name: "Lake Müritz", coords: [53.377, 12.718] },
    { name: "Lake Starnberg", coords: [47.900, 11.304] },
    { name: "Lake Ammer", coords: [47.966, 11.114] },
    { name: "Lake Tegernsee", coords: [47.710, 11.758] },
    { name: "Lake Wannsee", coords: [52.439, 13.163] },
    { name: "Lake Schwerin", coords: [53.636, 11.418] },
    { name: "Lake Steinhude", coords: [52.475, 9.357] },
    { name: "Lake Edersee", coords: [51.180, 9.035] }
];

// Selected lake name variable
let selectedLake = '';
let lakeMarkers = [];

// Function to add markers and update the dropdown with chlorophyll index
function addMarkersAndDropdown() {
    lakeMarkers.forEach(marker => map.removeLayer(marker));
    lakeMarkers = [];
    const dropdown = document.getElementById('lake-dropdown');
    dropdown.innerHTML = '<option value="">Select a lake</option>';

    lakes.forEach(function(lake) {
        const marker = L.marker(lake.coords).addTo(map);
        lakeMarkers.push(marker);

        // Fetch the latest chlorophyll data for the lake
        fetch(`/latest_chlorophyll?name=${encodeURIComponent(lake.name)}`)
            .then(response => response.json())
            .then(data => {
                let tooltipContent = lake.name;

                if (data.error) {
                    tooltipContent += ' (No chlorophyll data available)';
                } else {
                    const chlorophyll = data.chlorophyll.toFixed(2);
                    const trophicState = data.trophic_state;
                    const date = data.date;

                    if (chlorophyll < 2 || chlorophyll > 40) {
                        tooltipContent += ` - Chlorophyll: <span style="color:red;">${chlorophyll}</span> (Warning: Out of normal range)`;
                    } else {
                        tooltipContent += ` - Chlorophyll: ${chlorophyll} (${trophicState})`;
                    }
                    tooltipContent += ` (Latest on ${date})`;
                }

                marker.bindTooltip(tooltipContent, { permanent: false, className: "lake-tooltip" });
            })
            .catch(error => {
                console.error(`Error fetching chlorophyll data for ${lake.name}:`, error);
                marker.bindTooltip(lake.name + ' (Error fetching chlorophyll data)', { permanent: false, className: "lake-tooltip" });
            });

        marker.on('mouseover', function() {
            dropdown.value = lake.name;
        });

        marker.on('click', function() {
            dropdown.value = lake.name;
            selectedLake = lake.name;
        });

        // Add lakes to dropdown initially
        const bounds = map.getBounds();
        if (bounds.contains(lake.coords)) {
            const option = document.createElement('option');
            option.value = lake.name;
            option.text = lake.name;
            dropdown.add(option);
        }
    });
}

// Update dropdown when map is moved or zoomed
map.on('moveend', addMarkersAndDropdown);

// Initial population of markers and dropdown
addMarkersAndDropdown();

// Handle dropdown change event
document.getElementById('lake-dropdown').addEventListener('change', function() {
    selectedLake = this.value;
});

// Handle fetch data button click
document.getElementById('fetch-data-button').addEventListener('click', () => {
    const lakeName = document.getElementById('lake-dropdown').value;
    const selectedDate = document.getElementById('date-input').value;
    if (!lakeName) {
        alert("Please select a lake.");
        return;
    }
    if (!selectedDate) {
        alert("Please select a date.");
        return;
    }
    const queryString = `name=${encodeURIComponent(lakeName)}&date=${encodeURIComponent(selectedDate)}`;
    window.location.href = `/lake-details?${queryString}`;
});
