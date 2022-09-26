# Criando Lista de Produtos Únicos

Este programa processa as quatro listas do arquivo `estoque.py`. Os itens de cada lista são tuplas, as quais informam o código de um produto (SKU) e sua quantidade em estoque.

Veja abaixo a estrutura inicial de uma das listas:

```python
estoque_fim_jan = [
    ('BSA2199', 396),
    ('PPF5239', 251),
    ('BSA1212', 989),
    ....
```

O problema que estamos tentando solucionar é este: quais são os SKUs únicos?

No programa, é criada uma lista auxiliar chamada `lista_produtos` inicialmente vazia. Por meio de uma estrutura de repetição, acrescentamos todos os SKUs a essa lista.

Em seguida, passamos essa lista como argumento para a função `set` a fim de criar um conjunto com todos os elementos únicos da lista.

Por fim, esse conjunto é transformado numa lista por meio da função `list`.

Ao término de sua execução o programa exibe uma mensagem para informar o total de SKUs únicos e seus respectivos códigos.
