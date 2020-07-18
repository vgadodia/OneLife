from flask import Flask, jsonify, request, send_file, render_template, redirect, url_for, make_response
from flask_socketio import SocketIO, send
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import pathlib
import hashlib
import pickle
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

tfidf_vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
clf = pickle.load(open("model.pickle", "rb"))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    # print(predict('input1.jpg'))
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def getupload():
    if request.method == "POST":
        try:
            memory = request.files['memory']
            description = request.form['description']
            if memory.filename != "" and description != "":
                return render_template('upload.html', errorMessage="Please either upload a photo or link a url")
            elif memory.filename != "":
                memory.save(memory.filename)
                text = pytesseract.image_to_string(Image.open(memory.filename))
                result = clf.predict(tfidf_vectorizer.transform([text]))[0]
                print(result)
            elif description != "":
                result = clf.predict(tfidf_vectorizer.transform([description]))[0]
                print(result)
            else:
                return render_template('upload.html', errorMessage="Please either upload a photo or link a url")
        except:
            print("EXCEPT")
            return render_template('upload.html', errorMessage="Please either upload a photo or link a url.")
    return redirect("/")

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/gethelp')
def gethelp():
    return render_template('gethelp.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message' + msg)
    send(msg, broadcast=True)

@app.route('/forum')
def forums():
    return render_template('forum.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=8080, debug=True)

if __name__ == '__main__':
    socketio.run(app)