from flask import Flask, render_template, request, redirect, url_for
from pdf_processing.extractor import extract_content
from pdf_processing.mdformatter import md_formatter
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MARKDOWN_FOLDER'] = 'markdown_files/'  # Add new config for markdown files

# Create markdown directory if it doesn't exist
os.makedirs(app.config['MARKDOWN_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.pdf'):
            # Save PDF file
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Generate markdown content
            content = extract_content(filepath)
            markdown_output = md_formatter(content)

            # Save markdown content
            md_filename = os.path.splitext(file.filename)[0] + '.md'
            md_filepath = os.path.join(app.config['MARKDOWN_FOLDER'], md_filename)
            with open(md_filepath, 'w', encoding='utf-8') as md_file:
                md_file.write(markdown_output)

            return render_template('result.html', markdown_output=markdown_output)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)