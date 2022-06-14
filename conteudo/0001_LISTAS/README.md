# Listas

Listas são umas das estruturas mais básicas, é também a mais comum de se ver, e a primeira sempre a ser estudada.  
Possui muitos nomes diferentes, que variam de acordo com a linguagem usada, no python, por exemplo, é chamada de Lista (_List_), no JavaScript e outras linguas é conhecida como Array.  
Normalmente são ordenadas, ou seja, seu itens são processados na ordem em que aparecem.  
No [Python](www.python.org) e no [QGIS](www.qgis.org) são estruturas homogêneas.

Na calculadora de campo do [QGIS](www.qgis.org) há um grupo dedicado para trabalhar com arrays, sendo cada expressão dentro do grupo faz a função de algum método presente no array.

As listas (_Arrays_) permitem fazer a inserção de item em qualquer posição, permitem fazer a substituição de um item por outro.  
Além de poder fazer a contagem dos itens dentro dela

Exemplo em python:

```SQL
lista = [1, 2, 3, 4] -- No Python listas são sempre entre colchetes
lista.apend('jabuticaba') # Adiciona item no final da lista
print(lista)
-- [1, 2, 3, 4, 'jabuticaba']
lista[0] = 'laranja' # Modifica o item 0 da lista
print(lista)
-- ['laranja', 2, 3, 4, 'jabuticaba']
```

## Posição - indices

Todos os elementos de uma lista possui um _índice_ (posição), e normalmente o indice sempre se inicia do 0 (indice de base zero). Ou seja, o primeiro elemento da lista é o de índice 0.

```python
lista = ['primeiro', 'segundo', 'terceiro', 'quarto', 'n....']
indice       0            1         2           3        4
```

Para acessar um elemendo de uma lista, basta usar a notação `lista[indice]`

```SQL
lista = ['primeiro', 'segundo', 'terceiro', 'quarto', 'n....']
print(lista[3])
-- quarto
```

Também é possível acessar elementos numa lista usando indices negativos, sendo nesse caso partindo do final para o começo da lista

```python
lista = ['primeiro', 'segundo', 'terceiro', 'quarto', 'n....']
indice       0            1         2           3        4
negativo    -5           -4        -3          -2       -1
```

## Métodos de uma lista

Como já dito antes, as estruturas de dados possuem alguns métodos que permitem que trabalhemos com elas.  
Os metodos são básicamente ações que atuam na esturura, como por exemplo, contar elementos, encontrar elementos e por aí vai.  
E como estamos usando o [Python](www.python.org) como base, vamos ver alguns métodos básicos que podemos usar em uma lista, e comparar com o Array do [QGIS](www.qgis.org) ( sempre nessa forma `python` | `QGIS`).

* `len(_lista_)` | `array_length(_array_)` -> Esses metodos retornam a quantidade de elementos dentro da estrutura, sempre é um número inteiro.

exemplos:

Python

```sql
lista = [1, 2, 3, 4, 5, 'QGIS é top']
len(lista)
-- 6
```

[QGIS](www.qgis.org)

```SQL
-- Na calculadora de campo do qgis
array_length(array(1,2,3)) → 3
```

* `lista.append(elementos)` | `array_append(array, element)` -> Esse métodos adicionam um elemento ao final da estrutura.

exemplos:

Python

```sql
lista = [1, 2, 3, 4, 5, 'QGIS é top']
lista.append('I Love QGIS')
len(lista)
-- [1, 2, 3, 4, 5, 'QGIS é top', 'I Love QGIS']
```

[QGIS](www.qgis.org)

```SQL
-- Na calculadora de campo do qgis
array_append(array(1,2,3), 'I Love QGIS') → [1, 2, 3, 4, 5, 'QGIS é top', 'I Love QGIS']
```

* `lista.sort(*, key=None, reverse=False)` | `array_sort(array[,ascending=true])` -> Esses métodos fazem a ordenação dos itens na lista, os argumentos são opcionais.

:caution: Em listas mistas, o sort do [Python](www.python.org) vai gerar um erro, e no [QGIS](www.qgis.org) o comportamento é um pouco estranho, vale a pena conferir antes.

exemplos:

Python

```sql
lista = [1, 2, 3, 4, 5, 0]
lista.sort()
print(lista)
-- [0, 1, 2, 3, 4, 5]
-- Invertendo a ordenação
lista.sort(reverse=True)
print(lista)
-- [5, 4, 3, 2, 1, 0]
```

[QGIS](www.qgis.org)

```SQL
-- Na calculadora de campo do qgis
array_sort(array(1, 2, 3, 4, 5, 0)) → [0, 1, 2, 3, 4, 5]
-- Invertendo o aordenação
array_sort(array(1, 2, 3, 4, 5, 0), ascending=true) → [5, 4, 3, 2, 1, 0]
```

* `lista.reverse()` | `array_reverse(array)` -> Esses métodos invertem a ordem dos itens na lista.

exemplos:

Python

```sql
lista = [0, 1, 2, 3, 4, 5]
lista.reverse()
print(lista)
-- [5, 4, 3, 2, 1, 0]
```

[QGIS](www.qgis.org)

```SQL
-- Na calculadora de campo do qgis
array_reverse(array(0, 1, 2, 3, 4, 5)) → [5, 4, 3, 2, 1, 0]
```

## Exemplos de uso

Vamos voltar ao nosso exemplo dos times de futebol e suas vitórias no Campeonato Brasileiro.  
No lugar de termos um campo para cada ano que o time venceu o campeonato como demonstrado na tabela abaixo.

|time                  |ano_2000|ano_2001|ano_2002|ano_2003|ano_2004|ano_2005|ano_2006|ano_2007|
|:--------------------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
|Corinthians           |SIM     |NÃO     |NÃO     |NÃO     |NÃO     |NÃO     |NÃO     |SIM     |
|Clube Atlético Mineiro|NÃO     |SIM     |NÃO     |NÃO     |NÃO     |NÃO     |NÃO     |NÃO     |
|Cruzeiro              |NÃO     |NÃO     |SIM     |NÃO     |NÃO     |SIM     |NÃO     |NÃO     |
|Íbis                  |NÃO     |NÃO     |NÃO     |NÃO     |NÃO     |NÃO     |NÃO     |NÃO     |
|São Paulo             |NÃO     |NÃO     |NÃO     |SIM     |NAO     |NÃO     |NÃO     |NÃO     |
|Tabajara FC           |NÃO     |NÃO     |NÃO     |NÃO     |SIM     |NÃO     |SIM     |NÃO     |

> Pelo bem da explicação apenas os nomes dos times são reais

Podemos ter apenas uma coluna que recebe uma lista de anos em que o time foi campeão.

|time                  |campeao |
|:--------------------:|:------:|
|Corinthians           |[2000, 2007]|
|Clube Atlético Mineiro|[2001,]|
|Cruzeiro              |[2002, 2005]|
|Íbis                  |[]|
|São Paulo             |[2003,]|
|Tabajara FC           |[2004, 2006]|

Um outro exemplo disso, seria listar todos os municípios de um estado em uma coluna

## Observações

Vale muito a pena checar a documentação das ferramentas para saber mais sobre os métodos que trabalham com listas/arrays.

* [Arrays no QGIS](https://docs.qgis.org/3.22/en/docs/user_manual/expressions/functions_list.html#array-functions)

* [Listas no Python](https://docs.qgis.org/3.22/en/docs/user_manual/expressions/functions_list.html#array-functions)

