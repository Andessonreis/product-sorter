from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Product
from strategies import ByName, ByRating, ByPrice

app = Flask(__name__)
CORS(app)

products = []  # Lista global de produtos

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    nome = data['nome']
    avaliacao = float(data['avaliacao'])
    preco = float(data['preco'])

    new_product = Product(nome, avaliacao, preco)
    products.append(new_product)
    
    print(f"Produto adicionado: {new_product}")  # Verifica o produto adicionado
    print(f"Lista atual de produtos: {products}")  # Verifica a lista de produtos atual
    
    # Retorna a lista completa de produtos após a adição
    products_data = [
        {'nome': product.name, 'avaliacao': product.rating, 'preco': product.price}
        for product in products
    ]

    return jsonify(products_data), 200

@app.route('/sort_products', methods=['POST'])
def sort_products():
    data = request.get_json()
    estrategia = data['estrategia']  # Usando 'estrategia' conforme solicitado
    
    if estrategia == 'nome':
        sorted_products = ByName().sort(products)
    elif estrategia == 'avaliacao':
        sorted_products = ByRating().sort(products)
    elif estrategia == 'preco':
        sorted_products = ByPrice().sort(products)
    else:
        return jsonify({'message': 'Estratégia inválida'}), 400

    print(f"Produtos ordenados: {sorted_products}")  # Verifica a lista ordenada
    
    sorted_products_data = [
        {'nome': product.name, 'avaliacao': product.rating, 'preco': product.price}
        for product in sorted_products
    ]

    return jsonify(sorted_products_data), 200

if __name__ == "__main__":
    app.run(debug=True)

