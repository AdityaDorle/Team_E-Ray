import itertools
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA

# Load the CSV file
file_path = r"C:\Users\patna\Downloads\TSI_Calculations_and_Trophic_State 2 1.csv"
df = pd.read_csv(file_path)

# Function to parse the date and convert to Unix timestamp
def parse_date(date_str):
    for fmt in ("%m-%d-%Y %H:%M", "%m/%d/%Y %H:%M"):
        try:
            return int(datetime.strptime(date_str, fmt).timestamp())
        except ValueError:
            continue
    raise ValueError(f"date {date_str} is not in recognized format")

df['Unix_Time'] = df['date'].apply(parse_date)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])
df = df.sort_values(by='date')
df.set_index('date', inplace=True)
ts_data = df['Average_TSI']

# Hypertune ARIMA model parameters
p = d = q = range(0, 3)
pdq = list(itertools.product(p, d, q))

results_table = []

best_aic = float("inf")
best_bic = float("inf")
best_order = None
best_model = None

for param in pdq:
    try:
        model = ARIMA(ts_data, order=param)
        results = model.fit()
        results_table.append((param, results.aic, results.bic))
        if results.aic < best_aic:
            best_aic = results.aic
            best_order = param
        if results.bic < best_bic:
            best_bic = results.bic
            best_model = model
    except:
        continue

# Convert results_table to DataFrame
results_df = pd.DataFrame(results_table, columns=['Order', 'AIC', 'BIC'])

# Fit the best ARIMA model
arima_result = best_model.fit()

# Plot observed vs predicted TSI values
observed_data = ts_data
predicted_data = arima_result.predict(start=observed_data.index[0], end=observed_data.index[-1])

plt.figure(figsize=(10, 6))
plt.plot(observed_data, label='Observed')
plt.plot(predicted_data, label='Predicted', color='red')
plt.xlabel('Date')
plt.ylabel('Average TSI')
plt.title('Observed vs Predicted TSI')
plt.legend()
plt.savefig(r'C:\Users\patna\Desktop\Case Study\project\data\observed_vs_predicted_tsi.png')
plt.show()

# Plot the AIC and BIC values for different (p, d, q) combinations
plt.figure(figsize=(10, 6))
plt.plot([str(order) for order in results_df['Order']], results_df['AIC'], label='AIC', marker='o')
plt.plot([str(order) for order in results_df['Order']], results_df['BIC'], label='BIC', marker='x')
plt.xlabel('(p, d, q)')
plt.ylabel('Value')
plt.title('AIC and BIC values for different ARIMA parameter combinations')
plt.legend()
plt.xticks(rotation=90)
plt.savefig(r'C:\Users\patna\Desktop\Case Study\project\data\aic_bic_values.png')
plt.show()

# Trophic state classification
trophic_classification = {
    "Oligotrophic (low productivity)": (0, 40),
    "Mesotrophic (moderate productivity)": (40, 50),
    "Eutrophic (high productivity)": (50, 70),
    "Hypereutrophic (very high productivity)": (70, float("inf"))
}

# Plot trophic state classification
plt.figure(figsize=(10, 6))
for i, (label, (low, high)) in enumerate(trophic_classification.items()):
    plt.barh(label, high-low, left=low, color=f'C{i}')
plt.xlabel('TSI Value')
plt.title('Trophic State Classification')
plt.savefig(r'C:\Users\patna\Desktop\Case Study\project\data\trophic_state_classification.png')
plt.show()

# Save the results DataFrame
results_df.to_csv(r'C:\Users\patna\Desktop\Case Study\project\data\ARIMA_results.csv', index=False)
