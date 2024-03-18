import xlrd

def read_excel_xls(file_path):
    """
    Read data from an Excel (.xls) file using xlrd.
    
    Args:
    - file_path (str): The path to the Excel (.xls) file to be read.
    
    Returns:
    - excel_list (list): A list containing the data from the Excel (.xls) file.
    """
    excel_list = []
    
    # Open the Excel (.xls) file and create an xlrd workbook object
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)
    
    # Iterate over the rows in the sheet and append each row to the excel_list
    for i in range(sheet.nrows):
        excel_list.append(sheet.row_values(i))
    
    return excel_list

def main():
    # Prompt user to enter the file path
    file_path = input("Enter the path to the Excel (.xls) file: ")
    
    try:
        # Read data from the file
        data = read_excel_xls(file_path)
        print("Data successfully read from the file:")
        print(data)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")

if __name__ == "__main__":
    main()

