#!/usr/bin/env python3
from flask import Flask, render_template, request
import os    # Required to get the json source
import json  # Required to get structured data from json text stream
import csv   # Required to get structured data from csv text stream
import logging  # Useful to track how script behaves.


# =============== LOGGER SETUP AND CONFIGURATION ===============
script_dir = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger('flask_server')
logging.basicConfig(
    filename='task_03_traces.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')


# =============== SOURCE EXTRACTION FROM FILES ===============
def get_json_from_file(file_basename):
    """Returns a dict created from parsing json file, or empty dict"""
    source_path = os.path.join(script_dir, file_basename + '.json')
    log.debug(f"Get json: requested source path is {source_path}")
    if not os.path.exists(source_path):
        log.error(f"Source file {file_basename}.json not found!")
        return {}
    else:
        with open(source_path, 'r') as raw_json:
            return json.load(raw_json)


def get_csv_from_file(file_basename):
    """Returns a dict created from parsing csv file, or empty dict"""
    source_path = os.path.join(script_dir, file_basename + '.csv')
    log.debug(f"Get csv: requested source path is {source_path}")
    if not os.path.exists(source_path):
        log.error(f"Source file {file_basename}.csv not found!")
        return {}
    else:
        with open(source_path, 'r') as raw_csv:
            log.debug(raw_csv)
            csv_reader = csv.DictReader(raw_csv)
            return list(csv_reader)


SOURCE_HANDLERS = {
  "json": get_json_from_file,
  "csv": get_csv_from_file
}


# =============== FLASK WEBSERVER ===============
app = Flask(__name__)


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


@app.route('/products')
def products():

    error = None
    products_set = None
    # ONLY SUPPORTED VALUES: 'csv' and 'json'
    source = request.args.get('source')
    log.debug(f"Source parameter is: {source}")
    # OPTIONAL filter
    product_id = request.args.get('id')
    log.debug(f"Product id parameter is: {product_id}")

    # FIRST ENSURE we have actual data to leverage
    #   = supported source type and existing+readable file
    #   otherwise set an "error variable" valued as "invalid_source"
    #   so in template it's the "error message" which is displayed.
    file_handler = SOURCE_HANDLERS.get(source)
    if not file_handler:
        log.error("Handler not found!")
        error = "invalid_source"
    else:
        products_set = file_handler('products')
        log.debug(f"Products set retrieved is: {products_set}")
        # Unextractable file or empty dict
        if not products_set:
            log.debug("No products could be retrieved from given filename")
            error = "invalid_source"
    # THEN prepare the final dataset "products_set" to send to template:
    # EMPTY if nothing exploitable in source
    # ALL if no id specified
    # If id specified but not found set error value as "product_not_found"
    return render_template(
        'product_display.html',
        error=error,
        products_set=products_set
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
