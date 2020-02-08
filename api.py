from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/api/v1/products', methods=['GET'])
def get_products():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/products/<id>', methods=['GET'])
def get_product(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/products/', methods=['POST'])
def create_product():
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
    
