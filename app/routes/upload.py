from flask import Blueprint, request, redirect, url_for, flash
import pandas as pd
from werkzeug.utils import secure_filename
import os

upload_blueprint = Blueprint('upload', __name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_blueprint.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        # Ensure the uploads directory exists
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        # Get the path to the Excel file
        excel_path = filepath
        directory = UPLOAD_FOLDER


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

        return redirect(url_for('main.index'))
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
