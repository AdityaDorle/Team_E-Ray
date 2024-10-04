from flask import Flask, jsonify, request, send_from_directory
import psycopg2
from psycopg2.extras import RealDictCursor
from model import generate_prediction_for_missing_date, save_prediction_to_postgres, get_model_performance_metrics
from datetime import datetime
 
app = Flask(__name__, static_url_path='/static', static_folder='static')
 
# Database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        print("Database connection established")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
 
# Fetch lake data by name and date endpoint (GET)
@app.route('/lake_data', methods=['GET'])
def get_lake_data():
    lake_name = request.args.get('name')
    date_str = request.args.get('date')
    print(f"Requested lake data for: {lake_name} on date: {date_str}")
    if not lake_name or not date_str:
        return jsonify({'error': 'Lake name and date are required.'}), 400
 
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500
 
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        # Check if the data for the requested lake and date already exists
        cursor.execute('SELECT * FROM lake_data WHERE "name" = %s AND date = %s', (lake_name, date_str))
        lake_data = cursor.fetchall()
 
        if not lake_data:
            # If no data is found, generate predictions
            predicted_data = generate_prediction_for_missing_date()
 
            # Save the predicted data to PostgreSQL
            save_prediction_to_postgres(lake_name, predicted_data, date_str)
 
            # Convert predicted_data (which may contain numpy.float32) to standard Python float
            predicted_data = [float(value) for value in predicted_data]
 
            # Get model performance metrics
            performance_metrics = get_model_performance_metrics()
 
            # Return the predicted data along with the accuracy metric
            return jsonify({
                'message': 'Predicted data generated and saved to the database.',
                'SD': predicted_data[0],
                'chlorophyll': predicted_data[1],
                'TP': predicted_data[2],
                'TNO2': predicted_data[3],
                'unix_time': predicted_data[4],
                'date': date_str,
                'model_generated': True,  # Flag indicating this is model-generated data
                'performance_metrics': performance_metrics
            })
 
        conn.close()
        # Mark data according to 'model_generated' flag
        for entry in lake_data:
            entry['model_generated'] = entry.get('model_generated', False)
 
        # Get model performance metrics
        performance_metrics = get_model_performance_metrics()
 
        return jsonify({
            'lake_data': lake_data,
            'performance_metrics': performance_metrics
        })
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify({'error': 'Error fetching data'}), 500
 


 
 
 
# Fetch lake data by date endpoint (GET)

@app.route('/lake_data_by_date', methods=['GET'])

def get_lake_data_by_date():

    date_str = request.args.get('date')

    print(f"Requested lake data for date: {date_str}")

    try:

        date = datetime.strptime(date_str, '%Y-%m-%d').date()

    except ValueError:

        print("Invalid date format. Use YYYY-MM-DD.")

        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400
 
    conn = get_db_connection()

    if conn is None:

        return jsonify({'error': 'Failed to connect to the database'}), 500
 
    try:

        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute('SELECT * FROM lake_data WHERE date::date = %s', (date,))

        lake_data = cursor.fetchall()

        conn.close()
 
        if lake_data:

            print(f"Data found for date: {date_str}")

            return jsonify(lake_data)

        else:

            print(f"No data found for date: {date_str}")

            return jsonify({'error': 'No data found for this date'})

    except Exception as e:

        print(f"Error fetching data: {e}")

        return jsonify({'error': 'Error fetching data'}), 500
 
# Serve the homepage

@app.route('/')

def index():

    return send_from_directory(app.static_folder, 'index.html')
 
# Serve the lake list page

@app.route('/lake-list')

def lake_list():

    return send_from_directory(app.static_folder, 'lake_list.html')
 
# Serve the map page

@app.route('/map')

def map_page():

    return send_from_directory(app.static_folder, 'map.html')
 
# Serve the lake details page

@app.route('/lake-details')

def lake_details():

    return send_from_directory(app.static_folder, 'lake_details.html')
 
# Serve the about page

@app.route('/about')

def about():

    return send_from_directory(app.static_folder, 'about.html')
 
# Serve the references page

@app.route('/references')

def references():

    return send_from_directory(app.static_folder, 'references.html')
 
# API to fetch all lakes grouped by state (GET)

@app.route('/api/lakes', methods=['GET'])

def get_all_lakes():

    conn = get_db_connection()

    if conn is None:

        return jsonify({'error': 'Failed to connect to the database'}), 500
 
    try:

        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute('SELECT state, name FROM lake_data GROUP BY state, name ORDER BY state, name')

        lakes = cursor.fetchall()

        conn.close()
 
        lakes_by_state = {}

        for lake in lakes:

            state = lake['state']

            if state not in lakes_by_state:

                lakes_by_state[state] = []

            lakes_by_state[state].append(lake)
 
        return jsonify(lakes_by_state)

    except Exception as e:

        print(f"Error fetching lake list: {e}")

        return jsonify({'error': 'Error fetching lake list'}), 500
 
# Fetch the latest chlorophyll data for a given lake (GET)

@app.route('/latest_chlorophyll', methods=['GET'])

def get_latest_chlorophyll():

    lake_name = request.args.get('name')
 
    if not lake_name:

        return jsonify({'error': 'Lake name is required.'}), 400
 
    conn = get_db_connection()

    if conn is None:

        return jsonify({'error': 'Failed to connect to the database'}), 500
 
    try:

        cursor = conn.cursor(cursor_factory=RealDictCursor)

        current_date = datetime.now().date()
 
        cursor.execute('''

            SELECT chlorophyll, date 

            FROM lake_data 

            WHERE name = %s AND date < %s 

            ORDER BY date DESC 

            LIMIT 1

        ''', (lake_name, current_date))
 
        chlorophyll_data = cursor.fetchone()

        conn.close()
 
        if chlorophyll_data:

            chlorophyll_value = chlorophyll_data['chlorophyll']

            date_str = chlorophyll_data['date'].strftime('%Y-%m-%d')
 
            trophic_state = classify_chlorophyll(chlorophyll_value)
 
            return jsonify({

                'chlorophyll': chlorophyll_value,

                'trophic_state': trophic_state,

                'date': date_str

            })

        else:

            return jsonify({'error': 'No chlorophyll data found for this lake before today.'}), 404
 
    except Exception as e:

        print(f"Error fetching chlorophyll data: {e}")

        return jsonify({'error': 'Error fetching chlorophyll data'}), 500
 
# Function to classify chlorophyll levels based on trophic state

def classify_chlorophyll(chl):

    if chl < 2:

        trophic_state = 'Oligotrophic'

    elif 2 <= chl <= 6:

        trophic_state = 'Mesotrophic'

    elif 6 < chl <= 40:

        trophic_state = 'Eutrophic'

    else:

        trophic_state = 'Hypereutrophic'

    return trophic_state
 
if __name__ == '__main__':

    app.run(debug=True)

 