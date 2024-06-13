import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Parameters
start_date = datetime.now()
num_days = 7  # simulate data for 7 days
num_sensors = 5  # number of sensors
interactions = ['arrival', 'departure', 'item_pickup', 'item_return']

# List to hold all records
data_records = []

# Generate data
for day in range(num_days):
    date = start_date + timedelta(days=day)
    for sensor_id in range(1, num_sensors + 1):
        num_interactions = np.random.randint(5, 20)  # random number of interactions per sensor per day
        for _ in range(num_interactions):
            time = date + timedelta(minutes=random.randint(0, 1440))  # random time during the day
            interaction = random.choice(interactions)
            data_records.append([sensor_id, time, interaction])

# Create a DataFrame
df = pd.DataFrame(data_records, columns=['Sensor_ID', 'Timestamp', 'Interaction'])

df.to_csv('iot_retail_data.csv', index=False)
