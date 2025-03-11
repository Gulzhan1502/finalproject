import pandas as pd

# 1. Read air quality data
file_path = "air_quality_data.csv"
df = pd.read_csv(file_path)

# 2. Store CO levels for Sensor ID A103 as a list and print
a103_co = df[df['Sensor ID'] == 'A103']['CO (ppm)'].tolist()
print("CO levels for A103 sensor:", a103_co)

# 3. User input for sensor data retrieval
sensor_id = input("\nEnter Sensor ID to view readings (e.g., A101): ")
sensor_readings = df[df['Sensor ID'] == sensor_id]
print(f"\nSensor readings for {sensor_id}:")
print(sensor_readings.head())  # Shows first 5 entries

# 4. Calculate and print mean CO level
mean_co = df['CO (ppm)'].mean()
print(f"\nMean CO level across all sensors: {mean_co:.2f} ppm")