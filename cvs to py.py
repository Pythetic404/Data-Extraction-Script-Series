import csv

# Specify the file path to the CSV file
file_path = r'C:\Users\Pythetic\Downloads\watch_test.csv'

# Initialize an empty list to store the extracted data
excel_list = []

# Open the CSV file
with open(file_path, newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Iterate over the rows in the CSV file
    for row in reader:
        # Append each row to the excel_list
        excel_list.append(row)

# Optional: Print the extracted data to verify data extraction
print(excel_list)

# Markdown Notes Section:
"""
## Notes

- Ensure that the `file_path` variable points to the correct location of your CSV file.
- The `csv.reader()` object iterates over the rows in the CSV file, treating each row as a list of strings.
- The extracted data is stored in the `excel_list` variable for further processing or analysis.
"""

# If we wanted to get the data vertically from the spreadsheet, we can use the following approach:
"""
with open(file_path, newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Transpose rows and columns by iterating over the columns
    for col in zip(*reader):
        # Append each column data to the excel_list
        excel_list.append(list(col))
"""

