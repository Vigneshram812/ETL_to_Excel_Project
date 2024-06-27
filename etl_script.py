import os
import pandas as pd

def extract_data(file_path):
    # Check if the file exists and print its path
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Print file size and read the content
    print(f"File {file_path} exists, size: {os.path.getsize(file_path)} bytes")
    with open(file_path, 'r') as file:
        print(file.read())
    
    # Load data using pandas
    data = pd.read_csv(file_path)
    print("Extracted Data:\n", data.head())
    return data

def transform_data(data):
    # Perform some transformation on the data
    data['Total'] = data['Quantity'] * data['Price']
    print("Transformed Data:\n", data.head())
    return data

def load_data(data, output_file_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    
    # Write the data to an Excel file with engine='openpyxl'
    data.to_excel(output_file_path, index=False, engine='openpyxl')
    print(f"Data successfully written to {output_file_path}")

def main():
    input_file = 'data/store_sales.csv'
    output_file = 'output/transformed_sales.xlsx'
    
    # Extract
    data = extract_data(input_file)
    
    # Transform
    transformed_data = transform_data(data)
    
    # Verify data before loading
    print("Data to be loaded:\n", transformed_data.head())
    
    # Load
    load_data(transformed_data, output_file)
    
    print("ETL process completed successfully.")

if __name__ == "__main__":
    main()