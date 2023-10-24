import json
import os
import shutil

RAW_DIRECTORY = os.path.join(os.path.abspath(''),"0-RawData")

def scan_and_copy_book_quotes(src_directory, label='Book Quotes',dest_directory="BookQuotes"):
    """
    Scans the source directory for JSON files with a specific structure.
    If the label 'Book Quotes' is found in the file, it is copied to the destination directory.

    Parameters:
    - src_directory (str): The source directory to scan for JSON files.
    - dest_directory (str): The destination directory to copy the matching JSON files to. Defaults to 'Book Quotes'.
    """

    # Ensure destination directory exists, else create it
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    # Loop through each file in the source directory
    for file_name in os.listdir(src_directory):
        if file_name.endswith('.json'):  # Ensure the file is a JSON file
            file_path = os.path.join(src_directory, file_name)

            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)

                    # Check for the required structure and label 
                    if 'labels' in data and any(label.get('name') ==label for label in data['labels']):
                        shutil.copy(file_path, dest_directory)

                except json.JSONDecodeError:
                    # If there's an error in reading the JSON, just skip this file
                    pass

# Directory where raw data is
raw_directory = '1-KeepNotes'

# Directory where only the labeled notes will be copied 
destination_directory = '2-BookQuotes'

scan_and_copy_book_quotes(src_directory=os.path.join(RAW_DIRECTORY,raw_directory),
                          dest_directory=os.path.join(RAW_DIRECTORY,destination_directory))