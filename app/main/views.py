from flask import render_template,request,redirect,url_for
from . import main

#views
@main.route('/')
def index():
    hello="hello world"
    return render_template('index.html', title= 'pitch site', hello=hello)