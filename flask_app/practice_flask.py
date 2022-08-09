#!/usr/bin/env python3

import sqlite3
import os
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response
import sys

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if not os.path.exists('sqlite3_db'):
        db_dir = os.mkdir('sqlite3_db')
    db_name = 'flask_employee.db'
    sqlite3_db = os.path.join('sqlite3_db', db_name)
    if db is None:
        db = g._database = sqlite3.connect(sqlite3_db)
    return db

@app.teardown_appcontext
def create_table():
    with app.app_context():
        db = get_db()
        db.execute('CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, user_name TEXT)')
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/employee', methods=['PUT', 'POST', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    name = request.args.get('name', name)
    if request.method == 'GET':
        curs.execute('SELECT * FROM employee WHERE user_name = ?', (name,))
        if not employee:
            return Response(status=404)
        id, user_name = employee
        return f"{id}: {user_name}", 200
    elif request.method == 'PUT':
        curs.execute('INSERT INTO employee (user_name) VALUES (?)', (name,))
        db.commit()
        return Response(f"{name} created!", status=201)
    elif request.method == 'POST':
        new_name = request.values['new_name']
        curs.execute('UPDATE employee SET user_name = ? WHERE user_name = ?', (new_name, name))
        db.commit()
        return Response(f"{name} updated to {new_name}!", status=200)
    elif request.method == 'DELETE':
        curs.execute('DELETE FROM employee WHERE user_name = ?', (name,))
        db.commit()
        return Response(f"{name} deleted!", status=200)
    else:
        return Response('Method not allowed', status=405)


@app.route('/')
def hello_world():
    return 'top'


@app.route('/hello')
@app.route('/hello/<user_name>')
def hello_name(user_name=None):
    return render_template('hello.html', user_name=user_name)


@app.route("/post", methods=["POST", "PUT", "DELETE"])
def show_post():
    return str(request.values["user_name"])


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
    sys.exit(0)

