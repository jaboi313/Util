from typing import Literal

class Dictionary(dict):
    def __init__(self, dictionary:dict={}) -> None:
        self.__dictionary = dictionary
        self.__sort_order_options_all = 'ascending', 'descending', 'asc', 'des'
        self.__sort_order_options_ascending = 'ascending', 'asc', 
        self.__sort_order_options_descending = 'descending', 'des'

    def __str__(self) -> str:    # TODO: add functionality
        return "str"
    
    def __repr__(self) -> str:    # TODO: add functionality
        return "rpr"
    
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
    
    def count_keys(self, no_empty:bool=False) -> int:    # TODO: add functionality
        """Returns the amount of keys in the dictionary.\n
        If `no_empty` is `False` empty keys will be counted.\n
        If `True` empty keys will be skipped
        """
        return 1
    
    def count_values(self, no_empty:bool=False) -> int:    # TODO: add functionality
        """Returns the amount of values in the dictionary.\n
        If `no_empty` is `False` empty values will be counted.\n
        If `True` empty values will be skipped
        """
        return 2

    def sort_by_key(self, sort_order: Literal['ascending', 'descending', 'asc', 'des'] = 'ascending') -> dict:    # TODO: add docstrings # TODO: fix literal not using self.__sort_order_options_all
        if not isinstance(sort_order, str):
            raise TypeError(f"Invalid sort_order '{sort_order}'. sort_order must be a string. Choose from: {self.__sort_order_options_all}.")

        if sort_order in self.__sort_order_options_ascending:
            reverse = False
        elif sort_order in self.__sort_order_options_descending:
            reverse = True
        else:
            raise ValueError(f"Invalid sort_order '{sort_order}'. Choose from: {self.__sort_order_options_all}.")

        sorted_items = sorted(self.__dictionary.items(), key=lambda item: item[0], reverse=reverse)
        return dict(sorted_items)
    
    def sort_by_value(self, sort_order: Literal['ascending', 'descending', 'a', 'd'] = 'ascending') -> dict:    # TODO: add docstrings # TODO: fix literal not using self.__sort_order_options_all
        if not isinstance(sort_order, str):
            raise TypeError(f"Invalid sort_order '{sort_order}'. sort_order must be a string. Choose from: {self.__sort_order_options_all}.")

        if sort_order in self.__sort_order_options_ascending:
            reverse = False
        elif sort_order in self.__sort_order_options_descending:
            reverse = True
        else:
            raise ValueError(f"Invalid sort_order '{sort_order}'. Choose from: {self.__sort_order_options_all}.")

        sorted_items = sorted(self.__dictionary.items(), key=lambda item: item[1], reverse=reverse)
        return dict(sorted_items)

