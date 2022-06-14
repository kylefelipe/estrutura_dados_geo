# Dicionários

Todos já conhecemos como funciona um dicionário, procuramos por uma palavra e conseguimos os seus significados, e na estrutura de dados não se difere muito disso.

A estrutura de dados conhecida como dicionário (dict, [Python](www.python.org)) ou como __MAPA__ (__map__, [QGIS](www.qgis.org), não confunda com o mapa cartográfico), tem o funcionamento imitando o "pai dos burros", onde temos uma __chave__ (__key__) e um __valor__ (__value__) delimitado por chaves (o símbolo, {}, __braces__) na seguinte forma de pares `{'chave': 'valor'}`, sendo que normalmente a chave é uma string ou um número inteiro, e o valor pode ser de qualquer tipo, inclusive outras estruturas de dados também e seus itens são separados por vírgulas.

Esta estrutura nos permite fazer armazenamento e recuperação de valores utilizando as chaves (por isso não há importãncia da ordenação no dicionário).

Na calculadora de campo do [QGIS](www.qgis.org) há um grupo de expressões próprias para trabalhar com __mapas__ (__maps__), e da mesma forma que os __[arrays](../0001_LISTAS/README.md)__ cada função dentro do grupo faz a função de algum método do dicionário.

Um fato interessante sobre os dicionários é que as chaves dentro deles são únicas (como chaves primárias em um banco de dados).

## Posição

Sua indexação (acesso aos seus itens) é feita através das chaves, e não através de indice numérico como as [listas](../0001_LISTAS/README.md) e por conta disso, a ordenação de um dicionário não importa tanto, sendo que para acessar um determinado valor basta informar sua chave:

```python
dicionario = {'melhor_sig': 'QGIS', 'melhor_banco': 'PostgreSQL', 'melhor_linguagem': 'Python'}
print(dicionario['melhor_sig'])

>>> QGIS
```

Caso a chave solicitada não exista no dicinário, um erro será gerado, no caso do [Python](www.python.org) será um `_KeyError_`. Mas há formas de verfificar se uma chave existe dentro de um dicionário, para evitar problemas com erros assim.

No [Python](www.python.org) as chaves de um dicionário podem ser de qualquer tipo, desde que este não permita a sua alteração (tipo imutáveis), mesmo que esse tipo seja uma estrutura, como as **TUPLAS**, que são uma forma de lista mas que não permitem a alteração de seus itens, como inserção, remoção ou alteração do valor, iremos tratar das tuplas mais a frente.

## Métodos de um dicionário

Ja vimos alguns métodos nas [__listas__](../0001_LISTAS/README.md), e também já foi falado que esses métodos podem ser compartilhado entre estruturas diferentes, o método `len(dicionario)` | `map_length(map)` é um exemplo, onde podemos saber a quantidade de elementos que nossa estrutura possui.

> As chaves nestes exemplos são os geocódigos do IBGE para os municípios

### Criando dicionários

Aqui, a forma que o [QGIS](www.qgis.org) trata a estrutura é um pouquinho diferente que as coisas em [Python](www.python.org) pois para termos um dicionario na calculadora não podemos seguir o mesmo modelo das [listas](../0001_LISTAS/README.md), precisamos utilizar a expressão `map(chave1, valor1, chave2, valor2... chaven, valorn)` para que ele monte um dicionário, ou podemos montar o dicionario a partir de um __JSON__ (__JavaScript Object Notation__, sobre o qual veremos mais tarde) `from_json('string')`

Exemplo:

[Python](www.python.org)

```python
dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
print(dicionario)

>>> { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
```

Ou

```python
dicionario = dict([(3106200, 'Belo Horizonte'), (1600501, 'Oiapoque'), (4005439, 'Chuí') ])
print(dicionario)

>>> { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
```

[QGIS](www.qgis.org)

```SQL
map(3106200, 'Belo Horizonte', 1600501, 'Oiapoque', 4005439, 'Chuí')
→ {3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí'}

```

Dicionario a partir de um __JSON__.

[Python](www.python.org)

```python
import json
string_json = "{ 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }"
dicionario = json.loads(string_json)
print(dicionario)

>>> { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
```

[QGIS](www.qgis.org)

```sql
from_json("{ 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }")
→ { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
```

### Inserindo dados em um dicionário

A forma de inserir dados é diferente de uma lista. Devemos tomar cuidado pois a forma de inserir novos dados em um dicionário também faz alteração dos dados caso a chave já exista.

exemplo:

[Python](www.python.org)

```python
dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
dicionario[5300108] = 'Brasília'
print(dicionario)

>>> dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí', 5300108: 'Brasília' }
```

[QGIS](www.qgis.org)

```sql
map_insert(map(3106200, 'Belo Horizonte', 1600501, 'Oiapoque', 4005439, 'Chuí'), 5300108, 'Brasília')
→ { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí', 5300108: 'Brasília' }
```

Alterando um dado em um dicionario

[Python](www.python.org)

```python
dicionario = { 3106200: 'Belzont', 1600501: 'Oiapoque', 4005439: 'Chuí' }
dicionario[3106200] = 'Belo Horizonte'
print(dicionario)

>>> dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí'}
```

[QGIS](www.qgis.org)

```sql
map_insert(map(3106200, 'Belzont', 1600501, 'Oiapoque', 4005439, 'Chuí'), 3106200, 'Belo Horizonte')
→ { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí'}
```

### Listando chaves de um dicionário

Podemos obter uma [lista](../0001_LISTAS/README.md) contendo todas as chaves de um dicionário.

```python
dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
print(dicionario.keys())

>>> [ 3106200, 1600501, 4005439 ]
```

[QGIS](www.qgis.org)

```sql
map_akeys(map(3106200, 'Belo Horizonte', 1600501, 'Oiapoque', 4005439, 'Chuí'))
→ [ 3106200, 1600501, 4005439 ]
```

### Listando valores de um dicionário

Podemos obter uma lista contendo todos os valores de um dicionário.

Exemplos:

[Python](www.python.org)

```python
dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
print(dicionario.values())

>>> [ 'Belo Horizonte','Oiapoque', 'Chuí' ]
```

[QGIS](www.qgis.org)

```sql
map_avals(map(3106200, 'Belo Horizonte', 1600501, 'Oiapoque', 4005439, 'Chuí'))
→ [ 'Belo Horizonte','Oiapoque', 'Chuí' ]
```

### Pegando valores sem disparar erros

Como já foi falado, ao tentar recuperar um dado de um dicionario, se a chave não existir isso faz com que dispare um erro, portanto usar um método que tente 'pegar' a chave (`get`) e caso não exista retorne um valor `None` | `NULL` é uma boa prática.

Exemplos:

[Python](www.python.org)

```python
dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
print(dicionario.get(123456))

>>> None
```

[QGIS](www.qgis.org)

```sql
map_get(map(3106200, 'Belo Horizonte', 1600501, 'Oiapoque', 4005439, 'Chuí'), 123456)
→ NULL
```

### Removendo valores

Assim como nas [listas](../0001_LISTAS/README.md), também é possível remover um item de um dicionário usando a instrução `del dicionario['chave']`:

Exemplos:

[Python](www.python.org)

```python
dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
del dicionario[3106200]
print(dicionario)

>>> { 1600501: 'Oiapoque', 4005439: 'Chuí' }
```

[QGIS](www.qgis.org)

```sql
map_delete(map(3106200, 'Belo Horizonte', 1600501, 'Oiapoque', 4005439, 'Chuí'), 3106200)
→ { 1600501: 'Oiapoque', 4005439: 'Chuí' }
```

### Transformando em um JSON

Como alguns formatos de dados cartográficos não suportam o tipo __JSON__ uma forma de armazenarmos esses valores é salvar na tabela em formato de texto. No caso do [QGIS](www.qgis.org) a função `from_json(map)` retorna uma string formatada como um __[JSON](https://www.json.org/json-pt.html)__ que pode ser salva na tabela, no [Python](www.python.org) é conhecido como fazer um `dump` dos dados.

Exemplos:

[Python](www.python.org)

```python
import json
dicionario = { 3106200: 'Belo Horizonte', 1600501: 'Oiapoque', 4005439: 'Chuí' }
print(json.dumps(dicionario))

>>> '{ "3106200": "Belo Horizonte", "1600501": "Oiapoque", "4005439": "Chuí" }'
```

[QGIS](www.qgis.org)

```sql
to_json(map(3106200, 'Belo Horizonte', 1600501, 'Oiapoque', 4005439, 'Chuí'))
→ '{ "3106200": "Belo Horizonte", "1600501": "Oiapoque", "4005439": "Chuí" }'
```

## Exemplos de uso

Vamos imaginar que queremos mapear produtos vendidos e a quantidade por município. Então teríamos produtos como trator, computador, smartphones, colheitadeiras de milho, colheitadeiras de soja e por aí vái. O que normalmente uma pessoa faria é uma tabela da seguinte forma.

|municipio|produto_1|quant_prod_1|
|:-:|:-:|:-:|
|Belo Horizonte|computador|1200|
|Ladainha|Ordenhadeira|70|
|São Paulo|Colheitadeira Soja|0|
|Abelardo Luiz|Colheitadeira Soja|300|
|Patos de Minas|Colheitadeira Milho|100|
|Franca|Maq Costura| 3000|

Armazenar os dados nessa forma geraria grandes problemas, pois, nem todos os produtos vão ser vendidos em todas as cidades, em cidades voltadas para setor agrícola, os produtos para esse setor serião mais vendidos do que em cidades mais urbanas (quem na cidade de São Paulo teria uma colheitadeira de Soja na garagem!?), novos produtos poderiam  armazenar esses dados em forma de dicionários na tabela seria uma boa idéia.

|municipio|produtos_vendidos|
|:-:|:-:|
|Belo Horizonte|{'Computador':1200, 'Tv': 5000}|
|Ladainha|{Ordenhadeira:70, 'Tv': 200}|
|São Paulo|{'Smartphone': 12000, 'Adubo': 300}|
|Abelardo Luiz|{'Colheitadeira Soja': 300, 'Adubo': 3000}|
|Patos de Minas|{'Colheitadeira Milho': 100, 'Adubo': 4000}}|
|Franca|{'Maq Costura': 3000, 'Linha de costura': 40000, 'borracha': 130000}|

## Observações

Existem bancos de dados e formatos de dados que se baseiam nessa forma de guardar as informações, um dos bancos mais conhecidos é o __[MongoDB](https://www.mongodb.com)__, um banco **[NOSQL](https://blog.geekhunter.com.br/banco-de-dados-nosql-um-manual-pratico-e-didatico/#:~:text=NoSQL%20significa%20'n%C3%A3o%20relacional'.,dados%20constam%20no%20mesmo%20registro.)** que armazena os dados em uma forma *não estruturada*,  ou seja, um dado pode ter atributos diferente do outro, diferente de um banco estruturado, como os __SQLs__, e dos formatos, já vimos falar do __[JSON](https://www.json.org/json-pt.html)__ e provavelmente já ouviu falar do __[GeoJSON](https://geojson.org)__ que segue a linha dos dicionários para armazenagem dados.

O __[JSON](https://www.json.org/json-pt.html)__ é um fromato de dado que foi criado no __[JavaScript](https://www.javascript.com)__ (o nome é um acronimo de JavaScript Object Notation, pois no JavaScript esse tipo de estrutura é chamado de _Objeto_*) e que ficou muito popular devido a sua facilidade em ser usado na comunicação entre aplicações ou armazenamento de dados e a partir dele foi criada uma uma forma de utilizar dados geográficos também (vetores).

Obs:

* Não confunda o _Objeto_ (_Object_) do JavaScript com o _Objeto_ (_Object_) do paradigma **POO** (Programação Orientada a Objetos).

## Materiais Auxiliares

* [MAPS no QGIS](https://docs.qgis.org/3.22/en/docs/user_manual/expressions/functions_list.html#maps-functions)
* [Dicionários no PYTHON](https://docs.python.org/pt-br/3/library/stdtypes.html#mapping-types-dict)
* [Tutorial de Dicionário - Python](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries)
* [JSON](https://www.json.org/json-pt.html)
* [GeoJSON](https://geojson.org)
