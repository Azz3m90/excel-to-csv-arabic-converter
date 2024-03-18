import pandas as pd

def convert_excel_to_csv(excel_file, csv_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Write to CSV, make sure to encode it in UTF-8 to support Arabic characters
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    # Replace 'input.xlsx' with the path to your Excel file containing Arabic characters
    # Replace 'output.csv' with the desired name/path of the output CSV file
    convert_excel_to_csv('winners.xlsx', 'winners.csv')