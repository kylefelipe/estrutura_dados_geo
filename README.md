# Estrutura de dados e geo

Aprender sobre estruturas de dados para quem está aprendendo programação é algo que se faz desde o começo.  
Então aprender sobre Arrays|Listas, Maps|Dicionarios|Objetos, é corriqueiro e acaba se tornando natural.  
Mas nem sempre quem utiliza no geoprocessamento no dia a dia vê sobre tais formas de representação de dados.  
Até então, quem trabalha com geoprocessamento vê muitos tipos primitivos de dados, como `strings` (normalmente usado para representar textos ), `integers` (inteiros), `float|double|real|` (normalmente usados para representar números decimais) dentre outros, mas estes são para representar a forma mais simples de dados, seria um nome de rua, o número de uma casa, quantidade de dinheiro na sua conta bancária, esteja ela no negativo ou no positivo. 

## O que são, o que comem, como se reproduzem

Em alguns casos, precisamos trabalhar com grupos de dados, *estruturá-los* em **conjuntos** de dados para simplificar um pouco mais as coisas.  
Imagine que queira mapear todos os times brasileiros e saber quando foram campeões e quando foram vice no campeonato brasileiro, seria um martírio ter uma coluna para cada ano do brasileirão, e neles estarem escrito 'campeao' ou 'vice', pois teriamos de ter uma coluna para cada ano desde 1971 (não sei em que ano estão lendo isso, então façam as contas aí...). Para resolver problemas assim surgiram as estruras de dados, que são uma forma de podermos agrupar dados em um local, facilitando leitura, armazenamento, quantização e outros dados. Assim nasceram filas, pilhas, listas, dicionários, grafos e vários outros.  
Cada tipo de estrutura tem seus conjuntos de métodos, que em alguns casos podem compartilhar métodos, como o método que diz quantos items há dentro da estrutura ou inserir um dado em uma determinada posição. Esses métodos podem variar de linguagem para linguagem e ainda podemos acrescentar novos métodos que acharmos interessante colocar.

As estruturas ainda podem ter classificadas com as seguintes características:

- Lineares (arrays) ou não lineares (grafos);  
- homogêneas (só podem conter dados do mesmo tipo), ou heterogênea (contém vários tipos de dados)
- estáticas (posuem tamanho/capacidade fixo) ou dinãmicas (podem crescer ou diminuir sua capacidade)

Básicamente falando, as estruturas de dados são conjuntos de dados, agregados dependendo da forma que serão utilizados.

>-Sim  
>-Como aprendemos na escola?  
>-Básicamente, sim  
>-Então vai ser chato?  
>-Só se você quiser que seja, mas já te digo, vai ser legal.

Há algumas peculiaridades nas estruturas que são referentes à implementação, como forma de armazenamento em memória, modificação de items, que só irei tratar quando for realmente necessário, para não confundir muito a cabeça, mas deixarei dicas de pesquisa e curiosidades no desenrolar do conteúdo.  
Como o [Python](www.python.org) é bastante usado no mudo geo, farei umas comparações com a linguagem, e também com o [QGIS](www.qgis.org) que tem apresentado muitas formas de trabalhar algumas estruturas de dados na calculadora de campo nativamente.

Vale a pena salientar que trabalhar com estruturas de dados pode receber uma certa influênca dos formatos de dados geográficos que estamos utilizando, um exemplo é que o tão utilizado (eka) __shapefile__ não possui suporte para muitos tipos de dados nas colunas da tabela de atributos, então podemos converter a estrutura em formato de texto para salvar no __shp__ e fazer o caminho inverso para utilizarmos a estrutura. Já o [PostgreSQL](https://www.postgresql.org)/[Postgis](https://postgis.net) possuem suporte nativo para esse novo tipo de dado (sim, estruturas podem ser um tipo também)

[Sumário](./SUMARIO.md)
