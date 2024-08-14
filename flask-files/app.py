from flask import Flask, request, render_template_string, redirect, url_for, send_from_directory, abort
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# HTML Templates
upload_page = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload File</title>
</head>
<body>
    <h1>Upload File</h1>
    <form action="{{ url_for('upload_file') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
    <br>
    <a href="{{ url_for('download_file_list') }}">Go to Download Page</a>
</body>
</html>
'''

download_page = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download Files</title>
</head>
<body>
    <h1>Download Files</h1>
    <ul>
    {% for filename in files %}
        <li><a href="{{ url_for('download_file', filename=filename) }}">{{ filename }}</a></li>
    {% else %}
        <li>No files uploaded yet.</li>
    {% endfor %}
    </ul>
    <br>
    <a href="{{ url_for('upload_page') }}">Go to Upload Page</a>
</body>
</html>
'''

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            return redirect(url_for('download_file_list'))
    return render_template_string(upload_page)

@app.route('/download', methods=['GET'])
def download_file_list():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(download_page, files=files)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    if not os.path.exists(os.path.join(UPLOAD_FOLDER, filename)):
        abort(404)
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/')
def upload_page():
    return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(debug=True)
