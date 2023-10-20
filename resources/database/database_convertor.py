import pandas as pd
import os

# Get the path to the Excel file
excel_path = "resources/database/List_of_employees__address.xlsx"
directory = os.path.dirname(excel_path)

# Load the Excel file
xls = pd.ExcelFile(excel_path, engine='openpyxl')

# Loop through each sheet in the Excel file
for sheet_name in xls.sheet_names:
    df = xls.parse(sheet_name)
    
    # Convert the DataFrame to a JSON string
    json_string = df.to_json(orient="records", date_format="iso")

    # Save the JSON string to a file in the same directory, named after the sheet
    json_path = os.path.join(directory, f"{sheet_name}.json")
    with open(json_path, "w") as json_file:
        json_file.write(json_string)
