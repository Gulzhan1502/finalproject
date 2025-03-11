#part 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#1 read air quality data
file_path="air_quality_data.csv"
df=pd.read_csv(file_path)
#2 store CO levels for sensor ID A103 as lists
#3Allow user input to retrieve sensor readings for a given sensor
sensor_id=input("Enter Sensor ID:")

#4Identify and print the mean value for CO level readings



