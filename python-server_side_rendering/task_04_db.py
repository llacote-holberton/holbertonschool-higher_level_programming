#!/usr/bin/env python3
from flask import Flask, render_template, request
import os    # Required to get the json source
import json  # Required to get structured data from json text stream
import csv   # Required to get structured data from csv text stream
import sqlite3  # Required to interact with a SQLite database file
import logging  # Useful to track how script behaves.


# =============== LOGGER SETUP AND CONFIGURATION ===============
script_dir = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger('flask_server')
logging.basicConfig(
    filename='task_04_traces.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s')


# =============== SOURCE EXTRACTION FROM FILES ===============
def get_products_from_json_file(file_basename):
    """Returns a dict created from parsing json file, or empty dict"""
    source_path = os.path.join(script_dir, file_basename + '.json')
    log.debug(f"Get json: requested source path is {source_path}")
    if not os.path.exists(source_path):
        log.error(f"Source file {file_basename}.json not found!")
        return {}
    else:
        with open(source_path, 'r') as raw_json:
            return json.load(raw_json)


def get_products_from_csv_file(file_basename):
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


def get_products_from_sqlite_file(file_basename):
    """Returns a dict created from parsing SQLite db file, or empty dict"""
    source_path = os.path.join(script_dir, file_basename + '.db')
    log.debug(f"Get SQLite db: requested source path is {source_path}")
    if not os.path.exists(source_path):
        log.error(f"Source file {file_basename}.db not found!")
        return {}
    else:
        db_conn = sqlite3.connect(source_path)
        # WARNING: REQUIRED to be able to convert rows as dictionaries
        #   because by default sqlite3 just returns "flat values tuples"
        #   without the related columns's names.
        db_conn.row_factory = sqlite3.Row
        with db_conn:
            query = "SELECT * FROM products ORDER BY id"
            cursor = db_conn.cursor()
            products_data = cursor.execute(query)
            # Using list comprehension on fetchall as shorthand
            return [dict(row) for row in products_data.fetchall()]


SOURCE_HANDLERS = {
  "json": get_products_from_json_file,
  "csv": get_products_from_csv_file,
  "sql": get_products_from_sqlite_file
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

    source = request.args.get('source')  # Only SOURCE_HANDLERS keys supported
    log.debug(f"Source parameter is: {source}")
    product_id = request.args.get('id')  # None/invalid provided -> list all.
    log.debug(f"Product id parameter is: {product_id}")

    file_handler = SOURCE_HANDLERS.get(source)
    if not file_handler:
        log.error("Handler not found!")
        error = "invalid_source"
    else:
        products_set = file_handler('products')
        log.debug(f"Products set retrieved is: {products_set}")
        if not products_set:  # Unextractable file or empty dict
            log.debug("No products could be retrieved from given filename")
            error = "invalid_source"

    if error is None and product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            log.error(f"Couldn't read parameter as an integer")
            error = "product_not_found"
        else:
            product = next(
                # Forced conversion to str required because id is read as str
                #   in csv BUT as int in json. And str is guaranteed to work
                #   while an int conversion can fail.
                (p for p in products_set
                 if str(p.get('id')) == str(product_id)),
                None
            )
            if product is None:
                log.info(f"No product with id {product_id} found")
                error = "product_not_found"
            else:
                products_set = [product]

    # EMPTY (will display table header) if no exploitable source
    # ALL if no id specified
    # SINGLE if id specified and found
    return render_template(
        'product_display.html',
        error=error,
        products_set=products_set
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
