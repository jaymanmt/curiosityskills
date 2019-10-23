from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.template.html")


if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)