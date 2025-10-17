def busca_preco(produtos, nome_produto):

    if nome_produto in produtos:
        return produtos[nome_produto]
    else:
        return "Produto não encontrado"

# Exemplo de dicionário de produtos
produtos = {
    "Arroz": 20.0,
    "Feijão": 7.5,
    "Macarrão": 5.0,
    "Óleo": 8.5
}

produto = input("Digite o nome do produto: ")

resultado = busca_preco(produtos, produto)

print(f"Resultado: {resultado}")

print("Resultado: {}".format(resultado))
