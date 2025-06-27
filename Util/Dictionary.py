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
        lit = self.literal()
        inv = self.invert()
        ak = self.count_keys(no_empty=False)
        av = self.count_values(no_empty=False)
        akne = self.count_keys(no_empty=True)
        avne = self.count_values(no_empty=True)
        sbka = self.sort_by_key(sort_order='asc')
        sbkd = self.sort_by_key(sort_order='des')
        sbva = self.sort_by_value(sort_order='asc')
        sbvd = self.sort_by_value(sort_order='des')
        return f"""\nLiteral dictionary: {lit}\nInverted dictionary: {inv}\nAmount of key's: {ak}\nAmount of values: {av}\nAmount of key's (no empty): {akne}\nAmount of values (no empty): {avne}\nSorted by key - ascending: {sbka}\nSorted by key - descending: {sbkd}\nSorted by value - ascending: {sbva}\nSorted by value - descending: {sbvd}\n"""
    
    def literal(self) -> dict:
        """Returns the literal dictionary in dict form"""
        return self.__dictionary

    def invert(self) -> dict:    # TODO: add functionality
        """Returns the inverted dictionary in dict form"""
        return self.__dictionary
    
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

        sorted_items = sorted(self.__dictionary.items(), key=lambda item: item[0], reverse=reverse)
        return dict(sorted_items)
    
    def sort_by_value(self, sort_order: SortOrderLiteral = 'ascending') -> 'Dictionary':
        """Returns the sorted dictionary by value\n
        Ascending = `low -> high` : `a, b, c` or `1,2,3`"""
        if sort_order in SORT_ORDER_OPTIONS_ASC:
            reverse = False
        elif sort_order in SORT_ORDER_OPTIONS_DESC:
            reverse = True
        else:
            raise ValueError(f"Invalid sort_order '{sort_order}'. Choose from: {SORT_ORDER_OPTIONS_ALL}.")

        sorted_items = sorted(self.__dictionary.items(), key=lambda item: item[1], reverse=reverse)
        return dict(sorted_items)

