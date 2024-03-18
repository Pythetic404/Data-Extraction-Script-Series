import openpyxl

def read_excel_xlsx(file_path):
    """
    Read data from an Excel (.xlsx) file using openpyxl.
    
    Args:
    - file_path (str): The path to the Excel (.xlsx) file to be read.
    
    Returns:
    - excel_list (list): A list containing the data from the Excel (.xlsx) file.
    """
    excel_list = []
    
    # Open the Excel (.xlsx) file and create an openpyxl workbook object
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    
    # Iterate over the rows in the sheet and append each row to the excel_list
    for row in sheet.iter_rows(values_only=True):
        excel_list.append(row)
    
    return excel_list

def main():
    # Prompt user to enter the file path
    file_path = input("Enter the path to the Excel (.xlsx) file: ")
    
    try:
        # Read data from the file
        data = read_excel_xlsx(file_path)
        print("Data successfully read from the file:")
        print(data)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")

if __name__ == "__main__":
    main()
