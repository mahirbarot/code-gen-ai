from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# HTML form to upload image
@app.route('/')
def upload_file():
    return render_template('upload.html')

# Function to handle image upload
@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    # If user does not select file, browser also submits an empty part without filename
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return f'<h1>Uploaded {filename}</h1><img src="{filepath}" alt="Uploaded Image">'

if __name__ == '__main__':
    app.run(debug=True)
