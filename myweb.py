#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：pfl time:2019/1/31

import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)


# @app.errorhandler(404)
# def miss(e):
#     return render_template('login.html'), 404


@app.route('/')
def hello_world():
    ip = request.remote_addr
    print(ip)
    return 'Hello, World! %s' % ip


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return ''
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='80', debug=True)
