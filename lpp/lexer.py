from lpp.token import (
    Token,
    TokenType,
)
class Lexer:
    def __init__(self, source: str) -> None: # Constructor

        # Se inicializa una variable privada
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        # Cuando se inicializa se necesita correr por primera vez para que los caracteres se pongan correctamente
        self._read_character()

    def next_token(self) -> Token:
        token = Token(TokenType.ILLEGAL, self._character)
        
        # Se necesita correrlo despues de que se genere el token y antes de regresarlo
        self._read_character()
        
        return token # Se regresa el token
    

    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else: 
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1