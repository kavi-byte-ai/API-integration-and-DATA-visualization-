import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import time

# Configuration
API_KEY = '9216ff9c97e1e61239be9a234a8c4fbc'  # Replace with your OpenWeatherMap API key
CITY = 'Mumbai'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data
response = requests.get(URL)
data = response.json()

# Parse data
dates = []
temperatures = []
humidities = []

for entry in data['list']:
    dt_txt = entry['dt_txt']
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']
    
    dates.append(datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S'))
    temperatures.append(temp)
    humidities.append(humidity)

# Visualization using Seaborn
sns.set(style="darkgrid")

# Temperature Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, color='red')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperature_plot.png')
plt.show()

# Humidity Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=humidities, color='blue')
plt.title(f'Humidity Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('humidity_plot.png')
plt.show()
