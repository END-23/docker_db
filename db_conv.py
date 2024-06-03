import time
import xml.etree.ElementTree as ET
from pymongo import MongoClient
from bs4 import BeautifulSoup

# Attendere che MongoDB sia pronto
time.sleep(10)

# Parse XML file
tree = ET.parse('/app/Db_example.xml')
root = tree.getroot()

# MongoDB connection
client = MongoClient('mongo', 27017)
db = client['mydatabase']

# Set the collection name to "database"
collection_name = "database"
collection = db[collection_name]

# Create collections and insert sample data
for diagram in root.findall('.//diagram'):
    # Populate collection with sample data
    sample_data = {}
    for cell in diagram.findall('.//mxCell'):
        if 'value' in cell.attrib:
            value = cell.get('value')
            # Remove HTML tags
            text = BeautifulSoup(value, 'html.parser').get_text().strip()
            
            # Exclude PK and FK values
            if text and not any(keyword in text for keyword in ["PK", "FK"]):
                sample_data[text] = {}

    # Insert sample data into MongoDB collection
    if sample_data:  # Check if sample_data is not empty before inserting
        collection.insert_one(sample_data)

# Close MongoDB connection
client.close()





















