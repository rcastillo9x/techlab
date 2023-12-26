# app.py
from flask import Flask, request, jsonify
from datetime import datetime
import os
import threading


app = Flask(__name__)

# Shared dictionary of products
products = {}

# Lock for thread-safe operations on the dictionary
lock = threading.Lock()


@app.route('/products', methods=['POST'])
def create_product():
    with lock:
        product = request.json
        products[product['id']] = product
        product['date_request'] = datetime.now().isoformat()
        product['time_request'] = datetime.now().strftime("%H:%M:%S")
        return jsonify(product)

@app.route('/products/<int:product_id>', methods=['GET'])
def read_product(product_id):
    with lock:
        producto = products.get(product_id)
        if not producto:
            return jsonify({'message': 'Product not found'}), 404
        return jsonify(producto)

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    with lock:
        if product_id not in products:
            return jsonify({'message': 'Product not found'}), 404
        producto = request.json
        products[product_id] = producto
        return jsonify(producto)

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    with lock:
        if product_id not in products:
            return jsonify({'message': 'Product not found'}), 404
        del products[product_id]
        return jsonify({'message': 'Product removed'})

if __name__ == '__main__':
    port = os.getenv('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
