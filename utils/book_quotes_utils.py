import json
import os

def extract_book_quotes_from_json(directory):
    """
    Extracts the title and quotes from JSON files in the specified directory.

    Parameters:
    - directory (str): The directory containing the JSON files.

    Returns:
    - List[Dict[str, str]]: A list of dictionaries containing the title and quotes from each JSON file.
    """
    extracted_data = []

    # Loop through each file in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith('.json'):
            file_path = os.path.join(directory, file_name)
            
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    title = data.get("title", "")
                    
                    # Extract quotes from textContent, excluding chapter names
                    quotes = []
                    for line in data.get("textContent", "").split("\n"):
                        if line.startswith("▪"):
                            quotes.append(line[2:].strip())  # Remove the '▪' and whitespace
                    
                    extracted_data.append({"title": title, "quotes": quotes})

                except json.JSONDecodeError:
                    # If there's an error in reading the JSON, just skip this file
                    pass

    return extracted_data