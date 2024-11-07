import os
import re
import json
from datetime import datetime

json_file_path = './countries.json'
output_folder = '../../frontend/db/data/countries'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to create a TypeScript file for a given country
def create_ts_file(country, id_start):
    # Sanitize the country name for file name (lowercase and no punctuation)
    country_name = re.sub(r'[^a-zA-Z0-9]', '', country["name"].lower())

    # Define the TypeScript content using values from the country object
    ts_content = f"""export const Country{country['countryCode']} = {{
    id: {id_start},
    name: "{country['name']}",
    countryCode: "{country['countryCode']}",
    capital: "{country['capital']}",  
    currencyName: "{country['currencyName']}", 
    currencyCode: "{country['currencyCode']}",
    currencySymbol: "{country['currencySymbol']}", 
    timeZone: "{country['timeZone']}",
    website: "{country['website']}",
    createdAt: new Date(),
  }};
  """
    # Create the TypeScript file
    file_path = os.path.join(output_folder, f"{country_name}.ts")
    with open(file_path, "w") as ts_file:
        ts_file.write(ts_content)
    print(f"File created: {file_path}")

# Function to create files from a given country and ID
def create_files_from_country(start_country, start_id, countries):
    # Find the index of the start country
    start_index = next((index for (index, d) in enumerate(countries) if d["name"] == start_country), None)
    
    if start_index is None:
        print(f"Country '{start_country}' not found in the list.")
        return
    
    # Loop through the countries starting from the specified one
    for i, country in enumerate(countries[start_index:], start=start_id):
        create_ts_file(country, i)

# Load countries from a JSON file
def load_countries_from_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

# Main function to execute the script
def main():
    # Load countries from JSON
    countries = load_countries_from_json(json_file_path)

    # Start from Afghanistan (id 1)
    create_files_from_country("Afghanistan", 1, countries)

if __name__ == "__main__":
    main()
