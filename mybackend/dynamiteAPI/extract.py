import os
import json

# Directory path where the Swagger JSON files are located
directory_path = './'
output_directory_path = '/mnt/data/extracted/'

# Ensuring the output directory exists
if not os.path.exists(output_directory_path):
    print("a")
    os.makedirs(output_directory_path)

# Function to extract API information
def extract_api_details(api_data):
    extracted_info = []

    paths = api_data.get("paths", {})
    for path, operations in paths.items():
        for method, operation in operations.items():
            operations_list = operation if isinstance(operation, list) else [operation]

            for details in operations_list:
                if not isinstance(details, dict):
                    continue

                endpoint_info = {
                    "path": path,
                    "method": method.upper(),
                    "summary": details.get("summary", "No summary provided"),
                    "description": details.get("description", "No description provided")
                }

                endpoint_info["parameters"] = []
                if isinstance(details.get("parameters"), list):
                    for param in details["parameters"]:
                        if "$ref" in param:
                            continue
                        endpoint_info["parameters"].append({
                            "name": param.get("name"),
                            "in": param.get("in"),
                            "description": param.get("description", "No description provided"),
                            "required": param.get("required", False),
                            "type": param.get("type", "No type provided")
                        })

                endpoint_info["responses"] = []
                if isinstance(details.get("responses"), dict):
                    for status_code, response_details in details["responses"].items():
                        if "$ref" in response_details:
                            continue
                        endpoint_info["responses"].append({
                            "status_code": status_code,
                            "description": response_details.get("description", "No description provided")
                        })

                extracted_info.append(endpoint_info)
    
    return extracted_info

# Loop through all JSON files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
        file_path = os.path.join(directory_path, filename)
        # Read the JSON file
        with open(file_path, 'r') as file:
            api_data = json.load(file)
        
        # Extract API details
        api_details = extract_api_details(api_data)
        
        # Output the extracted details to a new JSON file
        output_file_path = os.path.join(output_directory_path, f'extracted_{filename}')
        with open(output_file_path, 'w') as out_file:
            json.dump(api_details, out_file, indent=2)

        print(f"Extracted data from {filename} into {output_file_path}")
