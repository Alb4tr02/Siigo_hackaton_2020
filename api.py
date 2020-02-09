from flask import Flask
from flask import jsonify
from flask import request
from metodos.lista import *
from metodos.crear import *

app = Flask(__name__)

@app.route('/api/v1/<table_name>', methods=['GET'])
def get_table(table_name):
    response = list_all_table(table_name)
    return jsonify(response)

@app.route('/api/v1/<table_name>/id=<id>', methods=['GET'])
def get_row_id(table_name, id):
    response = list_table_id(table_name, id)
    return jsonify(response)


@app.route('/api/v1/products', methods=['POST'])
def create_product():
    data = request.form
    #falta crear funcion para verificar la validez de las claves primarias y foraneas
    crear_ac_products(data)
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/products/<id>', methods=['PUT'])
def update_product(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/products/<id>', methods=['DELETE'])
def delete_product(id):
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
