#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb', 27017)
db = client.tododb


@app.route('/')
def todo():
    _items = db.items.find()
    items = [item for item in _items]
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add():
    item_doc = {
        'task': request.form['task'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
