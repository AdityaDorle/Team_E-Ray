import psycopg2
import pandas as pd
from tensorflow.keras.models import load_model
import pickle
import numpy as np
from tensorflow.keras.losses import MeanSquaredError
from sklearn.metrics import mean_squared_error, r2_score
 
# Database connection using psycopg2 with explicit encoding handling
def connect_to_postgres():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
        options="-c client_encoding=LATIN1"
    )
    return conn
 
# Fetch data from PostgreSQL with error handling for encoding
def fetch_data():
    conn = connect_to_postgres()
    try:
        query = "SELECT * FROM lake_data"
        df = pd.read_sql(query, conn)
        # Forcefully handle encoding issues by encoding as 'latin1' and decoding to 'utf-8'
        for col in df.columns:
            if df[col].dtype == 'object':  # Only attempt this on string columns
                df[col] = df[col].apply(lambda x: x.encode('latin1', 'ignore').decode('utf-8', 'ignore') if isinstance(x, str) else x)
    except Exception as e:
        print(f"Error fetching data: {e}")
    finally:
        conn.close()  # Ensure the connection is closed
    return df
 
# Function to generate predictions for a missing date
def generate_prediction_for_missing_date():
    # Load the saved model and specify the custom object for 'mse'
    custom_objects = {'mse': MeanSquaredError()}
    model = load_model("lstm_model.h5", custom_objects=custom_objects)
 
    # Load the saved scaler
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
 
    # Fetch the latest data from PostgreSQL to create a new prediction window
    df = fetch_data()
    data = df[['sd', 'chlorophyll', 'tp', 'tno2', 'unix_time']].values
 
    # Scale the data using the saved scaler
    scaled_data = scaler.transform(data)
 
    # Ensure there are enough rows to create a prediction window
    if len(scaled_data) < 5:
        raise ValueError("Not enough data to create a prediction window. Need at least 5 rows of data.")
 
    # Use the last 5 rows to create a prediction window
    last_window = np.array([scaled_data[-5:]])
 
    # Generate predictions
    predicted_scaled = model.predict(last_window)
    predicted_values = scaler.inverse_transform(predicted_scaled)
 
    # Return the predicted values for SD, chlorophyll, TP, TNO2, unix_time
    return predicted_values[0]
 
# Function to calculate model accuracy and error metrics
def calculate_model_performance(true_values, predicted_values):
    # Ensure the arrays are 1D and compatible in shape
    true_values = np.array(true_values).reshape(-1)
    predicted_values = np.array(predicted_values).reshape(-1)
 
    # Calculate the performance metrics
    mse = mean_squared_error(true_values, predicted_values)
    r2 = r2_score(true_values, predicted_values)
    mae = np.mean(np.abs(true_values - predicted_values))
    mape = np.mean(np.abs((true_values - predicted_values) / true_values)) * 100  # in percentage
    accuracy_percentage = 100 - mape  # Accuracy as 100% - MAPE
 
    performance_metrics = {
        'mse': mse,
        'r2_score': r2,
        'accuracy_percentage': accuracy_percentage
    }
 
    return performance_metrics
 
# Function to get model performance metrics (assuming you have test data)
def get_model_performance_metrics():
    # For demonstration purposes, we'll use hardcoded values
    performance_metrics = {
        'mse': 0.1234,
        'r2_score': 0.89,
        'accuracy_percentage': 94.5
    }
    return performance_metrics
 
# Function to save the generated prediction back to PostgreSQL
def save_prediction_to_postgres(name, predicted_data, date_str):
    # Convert numpy.float32 to Python float
    predicted_data = [float(value) for value in predicted_data]  # This ensures psycopg2 can handle it
 
    # Create a connection using psycopg2 for inserting data
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
        options="-c client_encoding=LATIN1"
    )
    cursor = conn.cursor()
 
    # Insert the predicted data into the lake_data table, including 'model_generated' flag
    cursor.execute('''
        INSERT INTO lake_data (name, sd, chlorophyll, tp, tno2, eutrophication_index, unix_time, date, model_generated)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (name, predicted_data[0], predicted_data[1], predicted_data[2], predicted_data[3], None, predicted_data[4], date_str, True))
 
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Predicted data for {name} on {date_str} saved to PostgreSQL.")
 
# Note: Ensure your 'lake_data' table has a 'model_generated' BOOLEAN column.

 
 