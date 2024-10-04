
# Interactive Water Quality Dashboard for Lakes in Germany

This project provides an interactive dashboard to visualize and analyze water quality data for various lakes in Germany. Users can explore the data through a dynamic map or a list of lakes categorized by state.

## Features

- Interactive map with clickable markers for lakes
- List of lakes by state with clickable items
- Detailed water quality data for each lake
- Date selection for historical data
- Visualizations of key water quality parameters
- Trophic State Index (TSI) calculations and visualizations
- Automatic data generation using a machine learning model if data for a selected date does not exist

## Setup

1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up the database and populate it with lake data.
4. Run the Flask server:
   ```sh
   python serve.py
   ```
5. Open your browser and navigate to `http://localhost:5000/`.

## Usage

- Visit the homepage and choose between the map view and the list view.
- Click on a lake to view detailed water quality data.
- Select a date to fetch historical data.
- If data for the selected date does not exist, it will be generated using a machine learning model.

## References

- [Leaflet.js](https://leafletjs.com/)
- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [OpenStreetMap](https://www.openstreetmap.org/)

## About

This interactive dashboard provides comprehensive information about the water quality of various lakes in Germany. Users can explore lake data through a dynamic map or browse a list of lakes categorized by state. The dashboard visualizes key water quality parameters, calculates the Trophic State Index (TSI), and provides forecasts using machine learning models. This information helps users determine the suitability of lakes for activities like fishing, swimming, and drinking.
