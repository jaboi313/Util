from typing import Literal

SORT_ORDER_OPTIONS_ALL = 'ascending', 'descending', 'asc', 'desc', 'a', 'd'
SORT_ORDER_OPTIONS_ASC = 'ascending', 'asc', 'a'
SORT_ORDER_OPTIONS_DESC = 'descending', 'desc', 'd'

SortOrderLiteral = Literal['ascending', 'descending', 'asc', 'desc', 'a', 'd']

EMPTY = (None, '', [], {}, ())


class Dictionary(dict):
    def __init__(self, dictionary:dict=None) -> None:
        if dictionary is None:
            dictionary = {}
            
        super().__init__(dictionary)

    def __str__(self) -> str:
        return f"{dict(self)}"

    def __repr__(self) -> str:
        return f"Dictionary({dict(self)})"

    def describe(self) -> str:
        """Returns general info about the dictionary.\n
        Info returned:\n
        - literal dictionary
        - reversed dictionary
        - inverted dictionary
        - amount of key's
        - amount of values
        - amount of key's (no empty)
        - amount of values (no empty)
        - sorted by key - ascending
        - sorted by key - descending
        - sorted by value - ascending
        - sorted by value - descending
        """
        lit = dict(self)
        rev = self.reverse()
        inv = self.invert()
        ak = self.count_keys(no_empty=False)
        av = self.count_values(no_empty=False)
        akne = self.count_keys(no_empty=True)
        avne = self.count_values(no_empty=True)
        sbka = self.sort_by_key(sort_order='asc')
        sbkd = self.sort_by_key(sort_order='desc')
        sbva = self.sort_by_value(sort_order='asc')
        sbvd = self.sort_by_value(sort_order='desc')
        return "\n".join(["",
            f"Literal dictionary: {lit}",
            f"Reversed dictionary: {rev}",
            f"Inverted dictionary: {inv}",
            f"Amount of keys: {ak}",
            f"Amount of values: {av}",
            f"Amount of keys (no empty): {akne}",
            f"Amount of values (no empty): {avne}",
            f"Sorted by key - ascending: {sbka}",
            f"Sorted by key - descending: {sbkd}",
            f"Sorted by value - ascending: {sbva}",
            f"Sorted by value - descending: {sbvd}", ""])

    def invert(self) -> 'Dictionary':
        """Returns the inverted dictionary (swap the key & value)\n
        Example: `{'a': 1, 'b': 2, 'c': 1, 'd':3}` -> `{1: ['a', 'c'], 2:'b', 3:'d'}`"""
        inverted = Dictionary()
        flattend_inverted = Dictionary()
        for key, value in self.items():
            if value in inverted:
                inverted[value].append(key)
            else:
                inverted[value] = [key]
        
        for key, value in inverted.items():
            if isinstance(value, list) and len(value) == 1:
                flattend_inverted[key] = value[0]
            else:
                flattend_inverted[key] = value
        return flattend_inverted
    
    def reverse(self) -> 'Dictionary':
        """Returns the reversed dictionary\n
        Example: `{'a': 1, 'b': 2, 'c': 1, 'd':3}` -> `{'d':3, 'c': 1, 'b': 2, 'a': 1}`"""
        return Dictionary(reversed(self.items()))
    
    def count_keys(self, no_empty:bool=False) -> int:
        """Returns the amount of keys in the dictionary.\n
        If `no_empty` is `False` empty keys will be counted.\n
        If `True` empty keys will be skipped
        """
        if no_empty:
            return sum(1 for key in self.keys() if key not in EMPTY)
        return len(self.keys())
    
    def count_values(self, no_empty:bool=False) -> int:
        """Returns the amount of values in the dictionary.\n
        If `no_empty` is `False` empty values will be counted.\n
        If `True` empty values will be skipped
        """
        if no_empty:
            return sum(1 for value in self.values() if value not in EMPTY)
        return len(self.values())

    def sort_by_key(self, sort_order: SortOrderLiteral = 'ascending') -> 'Dictionary':
        """Returns the sorted dictionary by key\n
        Ascending = `low -> high` : `a, b, c` or `1,2,3`"""
        if sort_order in SORT_ORDER_OPTIONS_ASC:
            reverse = False
        elif sort_order in SORT_ORDER_OPTIONS_DESC:
            reverse = True
        else:
            raise ValueError(f"Invalid sort_order '{sort_order}'. Choose from: {SORT_ORDER_OPTIONS_ALL}.")

        sorted_items = sorted(self.items(), key=lambda item: str(item[0]), reverse=reverse)
        return Dictionary(sorted_items)
    
    def sort_by_value(self, sort_order: SortOrderLiteral = 'ascending') -> 'Dictionary':
        """Returns the sorted dictionary by value\n
        Ascending = `low -> high` : `a, b, c` or `1,2,3`"""
        if sort_order in SORT_ORDER_OPTIONS_ASC:
            reverse = False
        elif sort_order in SORT_ORDER_OPTIONS_DESC:
            reverse = True
        else:
            raise ValueError(f"Invalid sort_order '{sort_order}'. Choose from: {SORT_ORDER_OPTIONS_ALL}.")

        sorted_items = sorted(self.items(), key=lambda item: str(item[1]), reverse=reverse)
        return Dictionary(sorted_items)

