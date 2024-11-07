import os
import json
import re

json_file_path = 'countries.json' 
output_folder = '../../frontend/db/data/countries' 
output_file_path = os.path.join(output_folder, 'index.ts')

# Load countries from the JSON file
def load_countries_from_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)
    
def sanitize_country_name(name):
    # Lowercase, replace spaces with nothing, and remove special characters
    return re.sub(r'[^a-zA-Z0-9]', '', name.lower())

# Create index.ts file with imports
def create_index_file(countries):
    imports = []
    
    for country in countries:
        # Sanitize the country name for file import (lowercase and no spaces)
        country_name = sanitize_country_name(country["name"])
        country_code = country["countryCode"]
        # Construct the import statement
        import_statement = f'import {{ Country{country_code} }} from "./{country_name}.ts";'
        imports.append(import_statement)
    
    # Create the array for countryList
    country_list_array = "const countryList = [" + ", ".join([f'Country{country["countryCode"]}' for country in countries]) + "];"

    # Define the content for index.ts
    ts_content = "\n".join(imports) + "\n\n" + country_list_array + "\n\nexport default countryList;"

    # Write to index.ts
    with open(output_file_path, 'w') as ts_file:
        ts_file.write(ts_content)
    print(f"File created: {output_file_path}")

# Main function to execute the script
def main():
    countries = load_countries_from_json(json_file_path)
    create_index_file(countries)

if __name__ == "__main__":
    main()