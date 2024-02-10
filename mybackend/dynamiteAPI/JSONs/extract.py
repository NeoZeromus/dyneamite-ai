import os
import json

# Directory path where the Swagger JSON files are located
directory_path = '/mnt/data/'  # Update this path to your actual file location



output_directory_path = '/mnt/data/extracted/'

# Ensuring the output directory exists
if not os.path.exists(output_directory_path):
    os.makedirs(output_directory_path)

# Function to extract API information
def extract_api_details(api_data):
    extracted_info = []

    paths = api_data.get("paths", {})
    for path, operations in paths.items():
        # Extract common parameters if they exist at the path level
        common_params = operations.get('parameters', [])
        for method, operation in operations.items():
            if method == 'parameters':  # Skip the common parameters object itself
                continue
            
            # Initialize endpoint info structure
            endpoint_info = {
                "path": path,
                "method": method.upper(),
                "summary": operation.get("summary", "No summary provided"),
                "description": operation.get("description", "No description provided"),
                "parameters": common_params.copy(),  # Start with common parameters
                "responses": {}
            }

            # Add method-specific parameters if they exist
            if isinstance(operation.get("parameters"), list):
                for param in operation["parameters"]:
                    if "$ref" in param:  # Reference object, handle separately
                        continue  # For now, we'll skip it, but you could implement reference resolution here
                    endpoint_info["parameters"].append({
                        "name": param.get("name"),
                        "in": param.get("in"),
                        "description": param.get("description", "No description provided"),
                        "required": param.get("required", False),
                        "type": param.get("type", "No type provided")
                    })

            # Extract responses
            if isinstance(operation.get("responses"), dict):
                for status_code, response_details in operation["responses"].items():
                    if "$ref" in response_details:  # Reference object, handle separately
                        continue  # For now, we'll skip it, but you could implement reference resolution here
                    endpoint_info["responses"][status_code] = response_details.get("description", "No description provided")

            extracted_info.append(endpoint_info)

    return extracted_info


# Loop through all JSON files in the directory
print(directory_path)
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
