from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
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
from . import nearby_therapists

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

tfidf_vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
clf = pickle.load(open("model.pickle", "rb"))

@main.route('/forum', methods=['GET', 'POST'])
def index2():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index2.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)

@main.route('/')
def index():
    # print(predict('input1.jpg'))
    return render_template('index.html')

@main.route('/upload')
def upload():
    return render_template('upload.html')

@main.route('/upload', methods=['GET', 'POST'])
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
                if result == 1:
                    text = "We have detected signs of suicidal and/or depressive thoughts in the messages. But don't worry, we are here to support you every step of the way. Please don't hesitate to call 1-800-273-8255 for help."
                else:
                    text = "We did not detect signs of suicidal and/or depressive thoughts in the messages. But still, please don't hesitate to call 1-800-273-8255 for further help."
                return render_template('results.html', result=result, text=text)
            elif description != "":
                result = clf.predict(tfidf_vectorizer.transform([description]))[0]
                print(result)
                if result == 1:
                    text = "We have detected signs of suicidal and/or depressive thoughts in the messages. But don't worry, we are here to support you every step of the way. Please don't hesitate to call 1-800-273-8255 for help."
                else:
                    text = "We did not detect signs of suicidal and/or depressive thoughts in the messages. But still, please don't hesitate to call 1-800-273-8255 for further help."
                
                return render_template('results.html', result=result, text=text)
            else:
                return render_template('upload.html', errorMessage="Please either upload a photo or link a url")
        except:
            print("EXCEPT")
            return render_template('upload.html', errorMessage="Please either upload a photo or link a url.")
    return redirect("/upload")

@main.route('/stats')
def stats():
    return render_template('stats.html')

@main.route('/gethelp')
def help():
    return render_template('gethelp.html')

@main.route('/gethelp', methods=['POST'])
def gethelp():
    try:
        zipcode = request.form['zipcode']
        nearby = nearby_therapists.nearby(zipcode)
        nearby = nearby[:9]
        return render_template('gethelp.html', nearby=nearby)
    except:
        return render_template("404.html")

@main.route('/404')
def error():
    return render_template('404.html')