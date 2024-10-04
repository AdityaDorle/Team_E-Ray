# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the uploaded Excel file
# file_path = 'C:/Users/SPEED FORCE/Downloads/Map_prototype1/static/Updated_Dataset_with_Converted_Date_Format 1.xlsx'
# excel_data = pd.ExcelFile(file_path)

# # Check sheet names to understand the structure of the file
# excel_data.sheet_names
# # Load the data from the first sheet
# data = pd.read_excel(file_path, sheet_name='Sheet1')

# # Display the first few rows of the data to understand its structure
# data.head()
# # Analyze the columns and their data types for better understanding
# data.info()


# # Create a list of the numerical columns to plot
# numerical_columns = ['SD', 'chlorophyll', 'TP', 'TNO2', 'eutrophication_index']

# # Plot each numerical column to visualize the data
# for column in numerical_columns:
#     plt.figure(figsize=(8, 6))
#     plt.plot(data['date'], data[column], marker='o', linestyle='-', markersize=3)
#     plt.title(f'Time Series of {column}')
#     plt.xlabel('Date')
#     plt.ylabel(column)
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()

# # Convert the 'date' column to datetime format for easier manipulation
# data['date'] = pd.to_datetime(data['date'])

# # Extract month and year for aggregation purposes
# data['year'] = data['date'].dt.year
# data['month'] = data['date'].dt.month


# # Bar plots: Seasonal aggregates for each parameter (SD, Chlorophyll, TP)


# # Winter: December to February, Spring: March to May, Summer: June to August, Fall: September to November
# season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter', 
#               3: 'Spring', 4: 'Spring', 5: 'Spring', 
#               6: 'Summer', 7: 'Summer', 8: 'Summer', 
#               9: 'Fall', 10: 'Fall', 11: 'Fall'}

# # Map months to seasons
# data['season'] = data['month'].map(season_map)

# # Aggregate by year and season
# seasonal_aggregates = data.groupby(['year', 'season']).mean(numeric_only=True)

# # Bar plot for seasonal aggregates
# fig, ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# seasonal_aggregates['SD'].unstack().plot(kind='bar', ax=ax[0], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Secchi Disk Depth')
# ax[0].set_ylabel('Secchi Disk Depth')

# seasonal_aggregates['chlorophyll'].unstack().plot(kind='bar', ax=ax[1], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Chlorophyll')
# ax[1].set_ylabel('Chlorophyll')

# seasonal_aggregates['TP'].unstack().plot(kind='bar', ax=ax[2], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Total Phosphorus')
# ax[2].set_ylabel('Total Phosphorus')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()




# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the uploaded Excel file
# file_path = 'C:/Users/SPEED FORCE/Downloads/Map_prototype1/static/Updated_Dataset_with_Converted_Date_Format 1.xlsx'
# excel_data = pd.ExcelFile(file_path)

# # Load the data from the first sheet
# data = pd.read_excel(file_path, sheet_name='Sheet1')

# # Convert the 'date' column to datetime format for easier manipulation
# data['date'] = pd.to_datetime(data['date'])

# # Extract month and year for aggregation purposes
# data['year'] = data['date'].dt.year
# data['month'] = data['date'].dt.month

# # Winter: December to February, Spring: March to May, Summer: June to August, Fall: September to November
# season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter', 
#               3: 'Spring', 4: 'Spring', 5: 'Spring', 
#               6: 'Summer', 7: 'Summer', 8: 'Summer', 
#               9: 'Fall', 10: 'Fall', 11: 'Fall'}

# # Map months to seasons
# data['season'] = data['month'].map(season_map)

# # Aggregate by year and season
# seasonal_aggregates = data.groupby(['year', 'season']).mean(numeric_only=True)

# # Bar plot for seasonal aggregates
# fig, ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# seasonal_aggregates['SD'].unstack().plot(kind='bar', ax=ax[0], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Secchi Disk Depth')
# ax[0].set_ylabel('Secchi Disk Depth')

# seasonal_aggregates['chlorophyll'].unstack().plot(kind='bar', ax=ax[1], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Chlorophyll')
# ax[1].set_ylabel('Chlorophyll')

# seasonal_aggregates['TP'].unstack().plot(kind='bar', ax=ax[2], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Total Phosphorus')
# ax[2].set_ylabel('Total Phosphorus')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Line plot for seasonal aggregates
# fig, ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# seasonal_aggregates['SD'].unstack().plot(kind='line', ax=ax[0], marker='o', title='Seasonal Average of Secchi Disk Depth (Line Graph)')
# ax[0].set_ylabel('Secchi Disk Depth')

# seasonal_aggregates['chlorophyll'].unstack().plot(kind='line', ax=ax[1], marker='o', title='Seasonal Average of Chlorophyll (Line Graph)')
# ax[1].set_ylabel('Chlorophyll')

# seasonal_aggregates['TP'].unstack().plot(kind='line', ax=ax[2], marker='o', title='Seasonal Average of Total Phosphorus (Line Graph)')
# ax[2].set_ylabel('Total Phosphorus')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the uploaded Excel file
# file_path = 'C:/Users/SPEED FORCE/Downloads/Map_prototype1/static/Updated_Dataset_with_Converted_Date_Format 1.xlsx'
# excel_data = pd.ExcelFile(file_path)

# # Load the data from the first sheet
# data = pd.read_excel(file_path, sheet_name='Sheet1')

# # Convert the 'date' column to datetime format for easier manipulation
# data['date'] = pd.to_datetime(data['date'])

# # Extract month and year for aggregation purposes
# data['year'] = data['date'].dt.year
# data['month'] = data['date'].dt.month

# # Winter: December to February, Spring: March to May, Summer: June to August, Fall: September to November
# season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter', 
#               3: 'Spring', 4: 'Spring', 5: 'Spring', 
#               6: 'Summer', 7: 'Summer', 8: 'Summer', 
#               9: 'Fall', 10: 'Fall', 11: 'Fall'}

# # Map months to seasons
# data['season'] = data['month'].map(season_map)

# # Aggregate by year and season
# seasonal_aggregates = data.groupby(['year', 'season']).mean(numeric_only=True)

# # Bar plot for seasonal aggregates
# fig, ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# seasonal_aggregates['SD'].unstack().plot(kind='bar', ax=ax[0], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Secchi Disk Depth', legend=False)
# ax[0].set_ylabel('Secchi Disk Depth')

# seasonal_aggregates['chlorophyll'].unstack().plot(kind='bar', ax=ax[1], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Chlorophyll', legend=False)
# ax[1].set_ylabel('Chlorophyll')

# seasonal_aggregates['TP'].unstack().plot(kind='bar', ax=ax[2], color=['skyblue', 'lightgreen', 'salmon', 'orange'], title='Seasonal Average of Total Phosphorus', legend=False)
# ax[2].set_ylabel('Total Phosphorus')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Line plot for seasonal aggregates
# fig, ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# seasonal_aggregates['SD'].unstack().plot(kind='line', ax=ax[0], marker='o', title='Seasonal Average of Secchi Disk Depth (Line Graph)', legend=False)
# ax[0].set_ylabel('Secchi Disk Depth')

# seasonal_aggregates['chlorophyll'].unstack().plot(kind='line', ax=ax[1], marker='o', title='Seasonal Average of Chlorophyll (Line Graph)', legend=False)
# ax[1].set_ylabel('Chlorophyll')

# seasonal_aggregates['TP'].unstack().plot(kind='line', ax=ax[2], marker='o', title='Seasonal Average of Total Phosphorus (Line Graph)', legend=False)
# ax[2].set_ylabel('Total Phosphorus')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()










# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the uploaded Excel file
# file_path = 'C:/Users/SPEED FORCE/Downloads/Map_prototype1/static/Updated_Dataset_with_Converted_Date_Format 1.xlsx'
# excel_data = pd.ExcelFile(file_path)

# # Load the data from the first sheet
# data = pd.read_excel(file_path, sheet_name='Sheet1')

# # Convert the 'date' column to datetime format for easier manipulation
# data['date'] = pd.to_datetime(data['date'])

# # Extract month and year for aggregation purposes
# data['year'] = data['date'].dt.year
# data['month'] = data['date'].dt.month

# # Winter: December to February, Spring: March to May, Summer: June to August, Fall: September to November
# season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter', 
#               3: 'Spring', 4: 'Spring', 5: 'Spring', 
#               6: 'Summer', 7: 'Summer', 8: 'Summer', 
#               9: 'Fall', 10: 'Fall', 11: 'Fall'}

# # Map months to seasons
# data['season'] = data['month'].map(season_map)

# # Aggregate by year and season
# seasonal_aggregates = data.groupby(['year', 'season']).mean(numeric_only=True)

# # Line plot for seasonal aggregates
# fig, ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# seasonal_aggregates['SD'].unstack().plot(kind='line', ax=ax[0], marker='o', title='Seasonal Average of Secchi Disk Depth (Line Graph)', legend=False)
# ax[0].set_ylabel('Secchi Disk Depth')

# seasonal_aggregates['chlorophyll'].unstack().plot(kind='line', ax=ax[1], marker='o', title='Seasonal Average of Chlorophyll (Line Graph)', legend=False)
# ax[1].set_ylabel('Chlorophyll')

# seasonal_aggregates['TP'].unstack().plot(kind='line', ax=ax[2], marker='o', title='Seasonal Average of Total Phosphorus (Line Graph)', legend=False)
# ax[2].set_ylabel('Total Phosphorus')

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()






import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded Excel file
file_path = 'C:/Users/SPEED FORCE/Downloads/Map_prototype1/static/Updated_Dataset_with_Converted_Date_Format 1.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from the first sheet
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Convert the 'date' column to datetime format for easier manipulation
data['date'] = pd.to_datetime(data['date'])

# Extract month and year for aggregation purposes
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

# Winter: December to February, Spring: March to May, Summer: June to August, Fall: September to November
season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter', 
              3: 'Spring', 4: 'Spring', 5: 'Spring', 
              6: 'Summer', 7: 'Summer', 8: 'Summer', 
              9: 'Fall', 10: 'Fall', 11: 'Fall'}

# Map months to seasons
data['season'] = data['month'].map(season_map)

# Aggregate by year and season
seasonal_aggregates = data.groupby(['year', 'season']).mean(numeric_only=True)

# Line plot for seasonal aggregates
fig, ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# Secchi Disk Depth Plot with Legend on the right
sd_plot = seasonal_aggregates['SD'].unstack().plot(kind='line', ax=ax[0], marker='o', title='Seasonal Average of Secchi Disk Depth (Line Graph)', legend=True)
ax[0].set_ylabel('Secchi Disk Depth')
ax[0].legend(title="Season", bbox_to_anchor=(1.05, 1), loc='upper left')  # Legend moved to the right

# Chlorophyll Plot without a legend
seasonal_aggregates['chlorophyll'].unstack().plot(kind='line', ax=ax[1], marker='o', title='Seasonal Average of Chlorophyll (Line Graph)', legend=False)
ax[1].set_ylabel('Chlorophyll')

# Total Phosphorus Plot without a legend
seasonal_aggregates['TP'].unstack().plot(kind='line', ax=ax[2], marker='o', title='Seasonal Average of Total Phosphorus (Line Graph)', legend=False)
ax[2].set_ylabel('Total Phosphorus')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
