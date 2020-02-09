from flask import Flask
from flask import jsonify
from flask import request
from metodos.lista import *
from metodos.crear import *
from metodos.delete import *

app = Flask(__name__)

@app.route('/api/v1/<table_name>', methods=['GET'])
def get_table(table_name):
    response = list_all_table(table_name)
    return jsonify(response)

@app.route('/api/v1/<table_name>/id=<id>', methods=['GET'])
def get_row_id(table_name, id):
    response = list_table_id(table_name, id)
    return jsonify(response)

@app.route('/api/v1/<table_name>', methods=['POST'])
def post_row(table_name):
    data = request.form
    response = insert_into_table(table_name, data)
    return jsonify(response)

@app.route('/api/v1/<table_name>/<id>', methods=['POST'])
def update_product(id, table_name, data):
    response = update_table(id, table_name, data)
    return jsonify(response)

@app.route('/api/v1/<table_name>/id=<id>', methods=['DELETE'])
def delete_row_by_id(table_name, id):
    response = delete_row(table_name, id)
    return jsonify(response)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
