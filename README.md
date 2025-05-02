# Datastore-Asgn
datastore, ingestion, and visualization of data

# Data Storage and Visualization Project

For this project I set up a MongoDB database, inserted mock data into it, and then created plots to visualize that data using Python and Matplotlib.

## What This Project Does

1. **Sets up a MongoDB database**  
   I used pymongo to connect to a local MongoDB instance and set up a basic database and collection.

2. **Ingests mock data**  
   A script generates and inserts random data into MongoDB. Each entry has a category, value, and timestamp.

3. **Visualizes the data**  
   I used matplotlib to create a simple bar chart showing the average value for each category and another time series plot to show the trends overtime. The chart is saved as dashboard.png and time_series_dashboard.png.

## Files Included

- `datastore_setup.py`: Sets up the MongoDB database and collection.
- `data_ingest.py`: Creates and inserts mock data into the database.
- `visualization.py`: Pulls data from MongoDB and creates a plot.
- `dashboard.png`: Screenshot of the generated chart.
- `datastore-setup.md`: Explanation of the datastore choice.
- `data-ingestion.md`: How the data ingestion process works.
- `visualization.md`: How to view and understand the visualization.

## Requirements

- Python
- MongoDB installed and running
- pymongo, pandas, matplotlib libraries

To install the required Python packages, run:
    -pip install pymongo
    -pip install pandas
    -pip install matplotlib
