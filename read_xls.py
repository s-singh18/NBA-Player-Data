import pandas as pd
import json
from pymongo import MongoClient

# Read in file as pandas dataframe
file = "stephcurry2020-2021.xlsx"
df = pd.read_excel(file)

# Convert dataframe to dictionary
js = df.to_json()
di = json.loads(js)

# Open MongoDB connection
client = MongoClient(host="localhost", port=27017)
print(client.server_info())
# Get database
db = client.players
col = db.sc30

# Insert data
col.insert_one(di)
