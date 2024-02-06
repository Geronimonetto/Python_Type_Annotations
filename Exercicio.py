from typing import TypeVar


# O parâmetro que for usado como variável tbm deve ser usado no TypeVar
T = TypeVar('T')  


def get_item(list: list[T], index: int) -> T:
	return list[index]


list_int = get_item([1, 2, 3], 1)
list_str = get_item(['a', 'b', 'c'], 1)