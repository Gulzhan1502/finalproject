import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("air_quality_data.csv")

time_col = 'Timestamp'
if 'Timestamp' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
elif 'Time' in df.columns:
    df['Time'] = pd.to_datetime(df['Time'])
    time_col = 'Time'
else:
    print("No timestamp column found!")

plt.figure(figsize=(15, 10))

plt.subplot(2,2,1)
sns.lineplot(x=df[time_col], y=df['PM2.5 (microg/m3)'])
plt.title("PM2.5 vs Timestamps")
plt.xticks(rotation=45)

plt.subplot(2,2,2)
sns.scatterplot(x=df['PM2.5 (microg/m3)'], y=df['PM10 (microg/m3)'])
plt.title("PM2.5 vs PM10")

plt.subplot(2,2,3)
corr_matrix = df[['PM2.5 (microg/m3)', 'PM10 (microg/m3)', 'CO (ppm)']].corr()
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)
plt.title("Correlation Heatmap")

plt.subplot(2,2,4)
sns.kdeplot(x=df['PM2.5 (microg/m3)'].dropna(), fill=True)
plt.title("PDF of PM2.5")


plt.tight_layout()
plt.show()
