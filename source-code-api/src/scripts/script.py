import json

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
        return max(usuario['id'] for usuario in dados) + 1
    else:
        return 1  # Se não houver usuários, começa com ID 1

# Função para processar os dados do novo usuário
def processar_usuario(nome, idade):

    dados = ler_dados()  # Lê os dados existentes
    novo_usuario = {
        'id': gerar_id(dados),
        'nome': nome,
        'idade': idade
    }
    
    # Adiciona o novo usuário à lista
    dados.append(novo_usuario)
    
    # Salva os dados atualizados no arquivo JSON
    salvar_dados(dados)
    
    return novo_usuario  # Retorna o novo usuário