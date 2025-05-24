from flask import Flask, request, jsonify

app = Flask(__name__)

nomes = []

# Endpoint Get
@app.route('/nomes', methods=['GET'])
def get_nomes():
    return jsonify(nomes), 200

# Endpoint Post
@app.route('/nomes', methods=['POST'])
def add_nomes():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'O campo "name" é obrigatório'}), 400

    new_nome = {
        'id': len(nomes) + 1,
        'name': data['name']
    }
    nomes.append(new_nome)
    return jsonify(new_nome), 201

if __name__ == '__main__':
    app.run(debug=True)
