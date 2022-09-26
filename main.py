# Importa as variáveis do arquivo estoque.py
from estoque import estoque_fim_jan, estoque_fim_fev, estoque_fim_mar, estoque_fim_abr


def obter_produtos_unicos(*args):
    """Retorna uma lista de produtos únicos

    Parâmetros:
        *args (list): lista de tuplas, com cada tupla informando SKU e estoque

    Retorna:
        produtos_unicos (list): lista com SKUs únicos
    """

    lista_produtos = []

    # Percorre cada um dos itens da tupla, sendo que cada item é uma lista
    for registros in args:
        for sku, qtde_estoque in registros:
            lista_produtos.append(sku)

    produtos_unicos = list(set(lista_produtos))
    return produtos_unicos


lista_produtos_unicos = obter_produtos_unicos(
    estoque_fim_jan,
    estoque_fim_fev,
    estoque_fim_mar,
    estoque_fim_abr
)

print(f"Há {len(lista_produtos_unicos)} produtos únicos.")
print("São estes:")
print("\n".join(lista_produtos_unicos))
