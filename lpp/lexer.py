from re import match
from lpp.token import (
    Token,
    TokenType,
)


class Lexer:
    def __init__(self, source: str) -> None: # Constructor

        # Se inicializan variables privadas
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        # Cuando se inicializa se necesita correr por primera vez para que los caracteres se pongan correctamente
        self._read_character()


    def next_token(self) -> Token:
        # Se va a revisar con expresiones regulares
        """
        En Python las expresiones regulares empiezan con cadenas row
        # Comience al principio de la cadena, encuentre un igual y que termine en esto, se quiere un igual desde el principio hasta el final
        """
        if match(r'^=$', self._character):
            token = Token(TokenType.ASSIGN, self._character)
        elif match(r'^\+$', self._character): 
            token = Token(TokenType.PLUS, self._character)
        elif match(r'^\($', self._character):
            token = Token(TokenType.LPAREN, self._character)
        elif match(r'^\)$', self._character):
            token = Token(TokenType.RPAREN, self._character)
        elif match(r'^\{$', self._character):
            token = Token(TokenType.LBRACE, self._character)
        elif match(r'^\}$', self._character):
            token = Token(TokenType.RBRACE, self._character)
        elif match(r'^,$', self._character):
            token = Token(TokenType.COMMA, self._character)
        elif match(r'^;$', self._character):
            token = Token(TokenType.SEMICOLON, self._character)
        elif match(r'^$', self._character):
            token = Token(TokenType.EOF, self._character)            
        else: # Si no reconoce entonces dirá que es un Token ilegal
            token = Token(TokenType.ILLEGAL, self._character)
        """
        Se tiene que escapar especificamente el caracter de suma porque suma significa algo especifico en las expresiones regulares, significa que haga match por lo menos una o mas veces pero aqui no interesa la funcionalidad sino especificamente el caracter, se escapa con la diagonal
        """
        # Escapar: hacer que el caractér sea tomado cómo texto plano en lugar de su significado por defecto en la expreción regular.

        
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