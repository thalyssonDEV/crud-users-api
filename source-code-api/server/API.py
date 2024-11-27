from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Função para ler os dados do arquivo JSON
def ler_dados():
    try:
        with open('usuarios.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Caso o arquivo não exista, retorne uma lista vazia

# Função para salvar os dados no arquivo JSON
def salvar_dados(dados):
    with open('usuarios.json', 'w') as f:
        json.dump(dados, f, indent=4)

# Função para gerar o próximo ID automaticamente
def gerar_id(dados):
    if dados:
        # Pega o maior ID e adiciona 1 para gerar o novo ID
        return max(usuario['id'] for usuario in dados) + 1
    else:
        return 1  # Se não houver usuários, começa com ID 1

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    dados = ler_dados()
    return jsonify(dados)

@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    dados = ler_dados()
    usuario = next((u for u in dados if u['id'] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"mensagem": "Usuário não encontrado"}), 404

@app.route('/usuarios', methods=['POST'])
def add_usuario():
    dados = ler_dados()
    novo_usuario = request.get_json()
    
    # Gerar o próximo ID automaticamente
    novo_usuario['id'] = gerar_id(dados)

    # Adicionar o novo usuário à lista
    dados.append(novo_usuario)
    salvar_dados(dados)
    return jsonify(novo_usuario), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    dados = ler_dados()
    usuario = next((u for u in dados if u['id'] == id), None)
    
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404

    dados.remove(usuario)
    atualizado = request.get_json()
    usuario.update(atualizado)
    dados.append(usuario)
    salvar_dados(dados)
    return jsonify(usuario)

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    dados = ler_dados()
    usuario = next((u for u in dados if u['id'] == id), None)
    
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404

    dados.remove(usuario)
    salvar_dados(dados)
    return jsonify({"mensagem": "Usuário deletado com sucesso"})

@app.route('/usuarios', methods=['DELETE'])
def delete_all_users():
    dados = ler_dados()

    dados.clear()

    salvar_dados(dados)
    return jsonify({"mensagem": "Usuários deletados com sucesso"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)