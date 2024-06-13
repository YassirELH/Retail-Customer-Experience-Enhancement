import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


# Set the seed for reproducibility
np.random.seed(42)

# Parameters
num_days = 7  # one week of data
hours_open = 12  # store is open from 10 AM to 10 PM
entries_per_hour = 50  # average number of customers entering per hour
items_per_customer = 5  # average number of items a customer interacts with
environmental_samples_per_hour = 6  # every 10 minutes

# Generate timestamps for one week
timestamps = pd.date_range(start=datetime.now(), periods=num_days * hours_open * 60, freq='min')

# Simulate customer footfall
footfall = {
    'timestamp': [],
    'event_type': [],
    'customer_id': [],
    'sensor_id': []
}

customer_id = 1
for timestamp in timestamps:
    if 10 <= timestamp.hour < 22:  # between 10 AM and 10 PM
        for _ in range(np.random.poisson(entries_per_hour)):  # simulate number of entries using Poisson distribution
            footfall['timestamp'].append(timestamp)
            footfall['event_type'].append('entry')
            footfall['customer_id'].append(customer_id)
            footfall['sensor_id'].append(np.random.randint(1, 3))  # assuming two entry/exit sensors
            customer_id += 1

# Simulate item interactions
item_interaction = {
    'timestamp': [],
    'event_type': [],
    'customer_id': [],
    'item_id': []
}

for cid in range(1, customer_id):
    entry_time = np.random.choice(footfall['timestamp'])
    for _ in range(np.random.poisson(items_per_customer)):  # number of items interacted with
        item_interaction['timestamp'].append(entry_time + timedelta(minutes=np.random.randint(5, 120)))
        item_interaction['event_type'].append(np.random.choice(['pickup', 'return']))
        item_interaction['customer_id'].append(cid)
        item_interaction['item_id'].append(np.random.randint(1000, 1100))  # assuming 100 different items

# Simulate environmental conditions
environmental = {
    'timestamp': [],
    'temperature': [],
    'humidity': []
}

for timestamp in timestamps:
    if 10 <= timestamp.hour < 22:  # between 10 AM and 10 PM
        if timestamp.minute % 10 == 0:  # every 10 minutes
            environmental['timestamp'].append(timestamp)
            environmental['temperature'].append(np.random.normal(22, 2))  # average 22C, deviation of 2
            environmental['humidity'].append(np.random.normal(50, 10))  # average 50%, deviation of 10%

# Convert dictionaries to DataFrames
df_footfall = pd.DataFrame(footfall)
df_item_interaction = pd.DataFrame(item_interaction)
df_environmental = pd.DataFrame(environmental)

# Save to CSV
df_footfall.to_csv('footfall_data.csv', index=False)
df_item_interaction.to_csv('item_interaction_data.csv', index=False)
df_environmental.to_csv('environmental_data.csv', index=False)
