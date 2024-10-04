import psycopg2
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
import pickle

# Connect to PostgreSQL
def connect_to_postgres():
    conn = psycopg2.connect(
        dbname="postgres",  # replace with your DB name
        user="postgres",  # replace with your DB user
        password="postgres",  # replace with your DB password
        host="localhost",
        port="5432"
    )
    return conn

# Fetch data from PostgreSQL
def fetch_data():
    conn = connect_to_postgres()
    query = "SELECT * FROM lake_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Train and save the LSTM model
def train_lstm_model():
    # Fetch the data
    df = fetch_data()

    # Select relevant columns for training
    data = df[['sd', 'chlorophyll', 'tp', 'tno2', 'unix_time']].values

    # Scale the data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    # Save the scaler for future use
    with open("scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    # Create rolling windows
    window_size = 5
    X, y = [], []
    for i in range(len(scaled_data) - window_size):
        X.append(scaled_data[i:i + window_size])
        y.append(scaled_data[i + window_size])

    X = np.array(X)
    y = np.array(y)

    # Define LSTM model
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(X.shape[1], X.shape[2])))
    model.add(Dense(5))  # 5 outputs for the 5 features
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

    # Train the model
    model.fit(X, y, epochs=50, batch_size=32, verbose=1)

    # Save the trained model
    model.save("lstm_model.h5")
    print("Model trained and saved to lstm_model.h5")

# Run the training process
train_lstm_model()
