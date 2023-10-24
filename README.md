# Google Keep Notes to Goodreads Statistics Matcher

This repository contains a script that automates the processing and analysis of book quotes saved in Google Keep notes, and matches them against read books statistics from Goodreads. It organizes, matches, and visualizes the data in a comprehensive manner to make it easily understandable.

## Features

- **Google Keep Notes Processing**: Filters and saves notes with specific labels such as 'book quotes' in a separate directory.
- **Goodreads Data Import**: Imports and processes the exported Goodreads data file.
- **Quote Matching**: Matches the processed book quotes against the Goodreads statistics of read books using Fuzzywuzzy.
- **Text Analysis**: Processes the quotes using NLTK and Gensim for themes or topics.
- **Visualization**: Utilizes pyLDAvis to display visualizations of the discovered themes or topics in the data.

## Prerequisites

Ensure you have the following installed:
- Python 3.9
- Necessary Python libraries: fuzzywuzzy, nltk, gensim, pyLDAvis, pandas

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/rsiller/google-keep-to-goodreads.git
    cd google-keep-to-goodreads
    ```
   
2. Place your exported Google Keep JSON files into the `0-RawData/1-KeepNotes` directory and the Goodreads data file into the `0-RawData/` directory as `goodreads_library_export.csv`

3. Run the main script:
    ```bash
    python google_keep_label_filter.py
    ```
   
4. View the generated visualization and results in the `0-RawData/2-BookQuotes` directory.
5. The Jupyter notebook `book_analysis.ipynb` contains the imports, matching and visualization tools. 

## Visualization Sample with pyLDAvis

![Visualization Sample](/1-Images/sample_image.png)

## Contributing

Feel free to fork the repository and submit pull requests for any enhancements, bug fixes, or other contributions. Open issues if you encounter any problems or have suggestions for improvements.


## Acknowledgments

- The Fuzzywuzzy library is used for string matching.
- NLTK and Gensim are used for text processing and analysis.
- pyLDAvis is used for data visualization.

