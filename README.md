# Tipagem de dados

Antes de tudo precisamos instalar a biblioteca mypy para fazer os testes de Tipagem de dados

```
pip install mypy
```

Quando o assunto é Tipagem de dados - do inglês Type annotations - podemos mencionar que o Python é uma linguagem fortemente tipada. 

vou citar alguns exemplos de como funciona a Tipagem de dados em Python

```python
# Tipo de String
uma_string: str = 'Um valor'

# Tipo de Inteiro
um_inteiro: int = 12345 

# Tipo de float
um_float: float = 1.23

# Tipo de boolean
um_boolean: bool = True 

# Tipo de set
um_set: set = {1, 2, 3}

# Tipo de lista
uma_lista: list = []

# Tipo de tupla
uma_tupla: tuple = ()

# Tipo de dicionário
um_dicionario: dict = {}
```

O escopo da Tipagem básica é essa:

```python 
variavel: tipo = 'valor da variavel'`
```

Quando definimos o tipo de uma variável, quando utilizamos a variável em outro local no código não deve-se usar um valor de outro tipo.

Exemplo:

```python
variavel: str = 'string'

variavel = 1

# Quando utilizamos o mypy para fazer o teste de tipagem encontra-se um erro de incompatibilidade

```

Se estamos utilizando um tipo de variável *float* podemos usar um valor *int* pois o int é uma subclasse do float, porém isso não pode ser feito de forma inversa, por que o int não poderá ser utilizado um float.

vejamos o exemplo de uma função que soma números:

```python
def soma(x: int, y: int, z: float) -> float:

    return x + y + z

# O retorno da função será um float, logo no lugar de z posso usar tanto um número float como um número inteiro, porém no x e y não posso usar um valor float, será apresentando um problema de incompatibilidade
```

Em se tratar de incompatibilidade isso auxilia bastante os desenvolvedores, que por outro lado quando utilizarem a função será apresentado o erro de incompatibilidade informando a tipagem.

### Listas

Listas podem ser uma tipagem um pouco mais complexa, mas iremos desmistificar isso no trecho abaixo.

```python
lista_a: list = [1,2,3, 'a']
lista_b: list[int] = [1,2,3,4]
lista_c: list[tuple] = [('a',1)(1,2)]
lista_d: list[list] = [[1,2,3,'a'][3,2,3,'s']]
lista_e: list[list[int]] = [[1,2,3,4,5][2,3]]
lista_f: list[str] = ['a','s','d']
```

As listas podem ser representadas de diversas formas, podendo ser uma lista de inteiros, strings, ou até listas dentro de listas, com isso podemos observar que sempre que indicar o tipo da lista devemos também indicar o tipo de dados dessa lista (se preciso), se quiser apenas uma lista de inteiros, uso o *list[int]*, ou se precisar de uma lista de listas com inteiros use o *list[list[int]]* e assim seguimos, existe um método chamado *union* que veremos logo a frente que serve para utilizarmos mais de uma tipagem de dados.


### Dicionário

Assim como nas listas os dicionários também podem ser tipados de formas parecidaas, podemos usar vários tipos para os dados.

```python
dicionario = dict[str, list[int]] = {
'A':[1,5],
'B':[5,2],
'C':[6,3]
}
```

### Tuplas e Sets

As Tuplas e Sets funcionam parecidos com os dicionários e as listas, podemos utilizar de diversas formas.

```python
set: set[int] = {1,2,3}
set_str: set[str] = {'alow', 'nome', 'teste'}
```

```python
tupla_int: tuple[int] = (1,2,3,4)
tupla_lista: tuple[list[int]] = ([1,2,4])
```

### Type Alias

Em alguns casos quando necessário devemos utilizar um método chamado Type Alias, que nada mais é que usar variáveis para armazenar uma tipagem, ou seja usamos uma variável *x = list[int]*,
porém são mais usados quando se trata de uma tipagem maior.

Exemplo:

```python

# A tipagem é grande, logo podemos usar dessa forma
TipagemGrande = list[dict[str, [list[str]]]]  

```

E da mesma forma que uma variável funciona podemos também utilizar o Type Alias como uma tipagem já que armazenamos o valor em uma variável chamada *TipagemGrande*

```python

Value: TipagemGrande = [{'alow',['nome', 'senha']}]

```

Podendo também ser usado para outro Type Alias

```python
DicionarioAlias = list[TipagemGrande]
```

### Type Union

O método Type Union é usado quando a nossa tipagem tende a ter mais de 1 tipagem, por exemplo, nos exemplos que vimos acima, as listas, tuplas, sets e dicionários sempre tem o mesmo tipo, ou é inteiro[int] ou é string[str], portanto o union - representado por **|** - resolve essa questão.

Exemplo:

```python
letra_e_numero: str | int = 1  # Posso colocar um valor inteiro ou uma string
set_union: list[str | int] = {'a',1}

```

Observamos que o set tem 2 tipos diferentes, primeiro (str) e depois (int) ou seja, são 2 tipos diferentes usando o union.

**Atalho:** O sinal de union no teclado pode ser usado com - alt + 124

Existe também a possibilidade de ser usado um valor direto na variável tipada para não necessariamente precisar do valor para executar a função.

Exemplo:

```python
def multiplica(x: int, y: float = 0) -> float:
		return x * y

multiplica(1)

# Resultado ==> 0
```
