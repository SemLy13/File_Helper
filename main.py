from flask import Flask, request, jsonify, redirect, render_template
from flask_httpauth import HTTPBasicAuth
import pandas as pd
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

auth = HTTPBasicAuth()

USER_DATA = {
    "adm": "psw"
}

files_dict = {}  # A dictionary to store files and their columns

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def root():
    return redirect('/login', code=302)

@app.route('/login', methods=['GET'])
@auth.login_required
def login():
    return redirect('/upload')

@app.route('/upload', methods=['GET', 'POST'])
@auth.login_required
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            files_dict[filename] = df.columns.tolist()  # store file columns
        return redirect('/files')  # Перенаправление на страницу файлов после загрузки
    return render_template('upload.html')

@app.route('/files', methods=['GET'])
@auth.login_required
def get_files():
    return render_template('files.html', files_dict=files_dict)

@app.route('/file', methods=['GET'])
@auth.login_required
def get_file_data():
    filename = request.args.get('filename', default=None, type=str)
    filter_cols = request.args.get('filter', default=None, type=str)
    sort_cols = request.args.get('sort', default=None, type=str)

    if filename in files_dict:
        df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if filter_cols:
            filters = filter_cols.split(',')
            df = df[filters]

        if sort_cols:
            sorts = sort_cols.split(',')
            for sort in sorts:
                col, order = sort.split(':')
                df = df.sort_values(col, ascending=(order.lower() == 'asc'))

        return df.to_html()
    else:
        return "File not found"



if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
