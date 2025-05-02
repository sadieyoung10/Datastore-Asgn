# Data Ingestion

### Data Ingestion Process

How It Works:
- For this assignment, the data ingestion process takes data from a CSV file and inserts it into a MongoDB collection. I used Python along with the pandas and pymongo libraries to make this work.

- First, I read the CSV file using pandas.read_csv() to load the data into a DataFrame. Then, I converted the DataFrame into a list of dictionaries using the .to_dict('records') method. This format makes it easy to insert the data directly into MongoDB.

- Next, I connected to my local MongoDB instance using pymongo.MongoClient(), selected the database and collection I wanted to use, and used .insert_many() to add the data.

- This process makes it simple to go from raw CSV to a populated MongoDB collection with just a few lines of code.

### Data Generation and Insertion of Mock Data

- The mock data was generated with predefined categories including "Product A", "Product B", random values, and timestamps.
