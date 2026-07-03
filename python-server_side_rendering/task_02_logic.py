#!/usr/bin/env python3
from flask import Flask, render_template
import os    # Required to get the json source
import json  # Required to get structured data from json text stream
import logging  # Useful to track how script behaves.


app = Flask(__name__)
script_dir = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger('flask_server')
logging.basicConfig(
    filename='task_02_traces.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    json_source = ['1', '2']
    json_filename = 'items.json'
    source_path = os.path.join(script_dir, json_filename)
    if not os.path.exists(source_path):
        log.error(f"JSON source {source_path} not found on filesystem!")
        json_source = {'items': []}
    else:
        with open(source_path, 'r') as raw_json:
            json_source = json.load(raw_json)
            if 'items' not in json_source:
                json_source['items'] = []
    return render_template('items.html', items=json_source['items'])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
