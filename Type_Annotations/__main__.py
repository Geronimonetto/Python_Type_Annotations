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


# Tipagem de inteiros e float
def soma(x: int, y: int, z: float) -> float:
    return x + y + z


# Tipagem de listas
lista_a: list = [1, 2, 3, 'a']
lista_b: list[int] = [1, 2, 3, 4]
lista_c: list[tuple] = [('a', 1)(1, 2)]
lista_d: list[list] = [[1, 2, 3, 'a'][3, 2, 3, 's']]
lista_e: list[list[int]] = [[1, 2, 3, 4, 5][2, 3]]
lista_f: list[str] = ['a', 's', 'd']

# Tipagem em dicionários
dicionario: dict[str, list[int]] = {'nome': [1, 2]}


# Type Union
letra_e_numero: str | int = 1  # Posso colocar um valor inteiro ou uma string
set_union: list[str | int] = {'a', 1}


def multiplica(x: int, y: float = None) -> float:
    return x * y


multiplica(1)

# Resultado ==> 0
