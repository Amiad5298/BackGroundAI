from flask import Flask, render_template, request, redirect, url_for
import os
from ExcelManager import ExcelManager

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Set your OpenAI API key here
OPENAI_API_KEY = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Use ExcelManager to process the file and generate backgrounds
        excel_manager = ExcelManager(file_path, OPENAI_API_KEY)
        data = excel_manager.process_excel()

        if data is not None:
            return render_template('data.html', data=data)
        else:
            return "There was an error processing the Excel file.", 500

if __name__ == '__main__':
    app.run(debug=True)
