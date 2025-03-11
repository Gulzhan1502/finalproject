import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =============================================
# Part I: Data Loading and Initial Processing
# =============================================
#flf;dgf;lgfd;flgdf
# Read data using pandas
file_path = "Sensor_Data.csv"
df = pd.read_csv(file_path)

# Convert columns to appropriate data types
df['Temperature (°C)'] = df['Temperature (°C)'].astype(float)
df['Humidity (%)'] = df['Humidity (%)'].astype(float)
df['Pressure (hPa)'] = df['Pressure (hPa)'].astype(float)

# Task 2: Store Humidity and Pressure for S101 as tuples
s101_data = df[df['Sensor ID'] == 'S101'][['Humidity (%)', 'Pressure (hPa)']]
s101_tuples = list(s101_data.itertuples(index=False, name=None))
print("\n=== Part I Results ===")
print("Humidity and Pressure for S101:", s101_tuples)

# Task 3: Allow user input to retrieve sensor readings
sensor_id_input = input("\nEnter Sensor ID to view its readings (e.g., S101): ")
sensor_readings = df[df['Sensor ID'] == sensor_id_input]
print(f"\nSensor readings for {sensor_id_input}:")
print(sensor_readings.head ())

# Task 4: Identify and print the first 5 high-temperature readings
high_temp_readings = df[df['Temperature (°C)'] > 30].nlargest(5, 'Temperature (°C)')
print("\nFirst 5 high-temperature readings:")
print(high_temp_readings)

# =============================================
# Part II: Temperature Conversion & Anomaly Detection
# =============================================

def convert_temperature(temp):
    if temp > 30:
        return round((temp * 9/5) + 32, 2)  # Fahrenheit
    else:
        return round(temp + 273.15, 2)  # Kelvin

df['Converted Temp'] = df['Temperature (°C)'].apply(convert_temperature)

df['Anomaly'] = (df['Temperature (°C)'] > 30) | (df['Humidity (%)'] > 70)
anomaly_counts = df.groupby('Sensor ID')['Anomaly'].sum()

print("\n=== Part II Results ===")
print("\nAnomaly Counts per Sensor:")
print(anomaly_counts)

# =============================================
# Part III: Functions & User Interactions
# =============================================

def average_temperature(sensor_id):
    return df[df['Sensor ID'] == sensor_id]['Temperature (°C)'].mean().round(2)

def convert_pressure(hpa):
    return round(hpa / 10000, 3)  # Convert hPa to MPa

print("\n=== Part III Results ===")
sensor_id = input("\nEnter Sensor ID for average temperature (e.g., S101): ")
avg_temp = average_temperature(sensor_id)
print(f"Average temperature for {sensor_id}: {avg_temp:.2f}°C")

try:
    index = int(input("\nEnter row index (0-{}): ".format(len(df)-1)))
    pressure = df.loc[index, 'Pressure (hPa)']
    print(f"Pressure in MPa: {convert_pressure(pressure)}")
except (ValueError, IndexError) as e:
    print(f"Invalid input: {e}")

# # =============================================
# # Part IV: Outlier Detection & Cleaning
# # =============================================
sensor_groups = df.groupby('Sensor ID')

def remove_humidity_outliers(df):
    q1 = df['Humidity (%)'].quantile(0.25)
    q3 = df['Humidity (%)'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return df[(df['Humidity (%)'] >= lower_bound) & (df['Humidity (%)'] <= upper_bound)]

clean_df = pd.concat([remove_humidity_outliers(group) for _, group in sensor_groups])

print("\n=== Part IV Results ===")
print(f"Original data count: {len(df)}")
print(f"Cleaned data count: {len(clean_df)}")
print(f"Removed outliers: {len(df) - len(clean_df)}")

# =============================================
# Part V: Data Visualization & Analysis
# =============================================

plt.figure(figsize=(15, 10))

plt.subplot(2,2,1)
sns.lineplot(x='Timestamp', y='Temperature (°C)', data=df)
plt.title('Temperature Trends Over Time')


plt.subplot(2,2,2)
sns.scatterplot(x='Temperature (°C)', y='Humidity (%)', data=df, hue='Sensor ID')
plt.title('Temperature vs Humidity')

plt.subplot(2,2,3)
corr_matrix = df[['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')

plt.subplot(2,2,4)
sns.kdeplot(df['Humidity (%)'], fill=True)
plt.title('Humidity Density Estimation')

plt.tight_layout() 
plt.show()
