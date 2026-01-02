import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\nsg94\OneDrive\Desktop\Movies_dataset.csv")
print(df)
print("✅ Dataset loaded successfully!")
print(f"Total Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\nColumns List:\n", list(df.columns))

# CONVERT DATE COLUMN TO DATETIME
df['Date.Full'] = pd.to_datetime(df['Date.Full'], errors='coerce')

# BASIC SUMMARY
print("\n📊 BASIC DATA SUMMARY:")
print(df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# ADD NEW COLUMNS
df['Temp Range'] = df['Data.Temperature.Max Temp'] - df['Data.Temperature.Min Temp']
df['Month Name'] = df['Date.Full'].dt.month_name()

# AVERAGE TEMPERATURE TREND OVER TIME
daily_avg = df.groupby('Date.Full')['Data.Temperature.Avg Temp'].mean()
plt.figure(figsize=(10,4))
plt.plot(daily_avg, color='orange')
plt.title("Daily Average Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Average Temperature (°F)")
plt.grid(True)
plt.show()

#TOP 10 HOTTEST STATES
top_states = (
    df.groupby('Station.State')['Data.Temperature.Avg Temp']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
plt.figure(figsize=(10,4))
sns.barplot(x=top_states.index, y=top_states.values, palette='flare')
plt.title("Top 10 Hottest States by Average Temperature")
plt.ylabel("Average Temperature (°F)")
plt.xticks(rotation=45)
plt.show()

# CITY-WISE TEMPERATURE VARIATION
top_cities = df['Station.City'].value_counts().head(5).index
city_data = df[df['Station.City'].isin(top_cities)]
plt.figure(figsize=(10,5))
sns.boxplot(x='Station.City', y='Data.Temperature.Avg Temp', data=city_data, palette='viridis')
plt.title("Temperature Distribution for Top 5 Cities")
plt.xlabel("City")
plt.ylabel("Average Temperature (°F)")
plt.show()

# ⿩ MONTHLY TEMPERATURE TREND
monthly_temp = df.groupby('Date.Month')['Data.Temperature.Avg Temp'].mean()
plt.figure(figsize=(8,4))
monthly_temp.plot(marker='o', color='green')
plt.title("Average Temperature by Month")
plt.xlabel("Month Number")
plt.ylabel("Average Temperature (°F)")
plt.grid(True)
plt.show()

# WIND SPEED ANALYSIS
plt.figure(figsize=(6,4))
sns.histplot(df['Data.Wind.Speed'], bins=30, kde=True, color='purple')
plt.title("Distribution of Wind Speeds")
plt.xlabel("Wind Speed (mph)")
plt.ylabel("Frequency")
plt.show()

# CORRELATION HEATMAP
plt.figure(figsize=(8,6))
corr = df[['Data.Precipitation','Data.Temperature.Avg Temp',
           'Data.Temperature.Max Temp','Data.Temperature.Min Temp',
           'Data.Wind.Speed','Temp Range']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Weather Variables")
plt.show()

# PRECIPITATION VS TEMPERATURE
plt.figure(figsize=(6,4))
plt.scatter(df['Data.Temperature.Avg Temp'], df['Data.Precipitation'], alpha=0.5, color='teal')
plt.title("Precipitation vs Temperature")
plt.xlabel("Average Temperature (°F)")
plt.ylabel("Precipitation (inches)")
plt.grid(True)
plt.show()

#  AVERAGE TEMPERATURE BY STATE AND MONTH
pivot_table = df.pivot_table(values='Data.Temperature.Avg Temp',
                             index='Station.State', columns='Date.Month', aggfunc='mean')
plt.figure(figsize=(12,6))
sns.heatmap(pivot_table, cmap='YlOrRd')
plt.title("Average Temperature by State and Month")
plt.xlabel("Month")
plt.ylabel("State")
plt.show()

#  TEMPERATURE RANGE ANALYSIS
plt.figure(figsize=(8,4))
sns.histplot(df['Temp Range'], bins=30, kde=True, color='coral')
plt.title("Distribution of Daily Temperature Ranges")
plt.xlabel("Temperature Range (°F)")
plt.ylabel("Frequency")
plt.show()

print("\n🌡 WEATHER DATA INSIGHTS 🌡")
print(f"Highest Recorded Avg Temperature: {df['Data.Temperature.Avg Temp'].max()} °F")
print(f"Lowest Recorded Avg Temperature: {df['Data.Temperature.Avg Temp'].min()} °F")
print(f"Mean Precipitation: {df['Data.Precipitation'].mean():.2f} inches")
print(f"Mean Wind Speed: {df['Data.Wind.Speed'].mean():.2f} mph")
print(f"Average Temperature Range: {df['Temp Range'].mean():.2f} °F")

# Identify hottest and coldest states
hottest_state = df.groupby('Station.State')['Data.Temperature.Avg Temp'].mean().idxmax()
coldest_state = df.groupby('Station.State')['Data.Temperature.Avg Temp'].mean().idxmin()
print(f"Hottest State: {hottest_state}")
print(f"Coldest State: {coldest_state}")










