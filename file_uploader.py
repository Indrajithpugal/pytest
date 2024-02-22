from flask import Flask, render_template, url_for, request
from werkzeug import security

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('file_uploader.html')

@app.route('/uploader', methods =['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        file=request.files['file']