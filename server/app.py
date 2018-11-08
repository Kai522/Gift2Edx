from flask import Flask, render_template, request, url_for, redirect, session

from functools import wraps
app = Flask(__name__)

@app.route('/')
def index(data=None):
    return render_template('items/index.html', data=data)

if __name__ == "__main__":
    app.run()