from re import match
from lpp.token import (
    Token,
    TokenType,
    lookup_token_type,
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
        Comience al principio de la cadena, encuentre un igual y que termine en esto, se quiere un igual desde el principio hasta el final
        """
        self._skip_whitespace() # Se ignoraran los espacios en blanco siempre al empezar un nuevo token

        if match(r'^=$', self._character):
            token = Token(TokenType.ASSIGN, self._character)
        elif match(r'^\+$', self._character): 
            token = Token(TokenType.PLUS, self._character)
        elif match(r'^$', self._character):
            token = Token(TokenType.EOF, self._character)
        elif match(r'^\($', self._character):
            token = Token(TokenType.LPAREN, self._character)
        elif match(r'^\)$', self._character):
            token = Token(TokenType.RPAREN, self._character)
        elif match(r'^{$', self._character):
            token = Token(TokenType.LBRACE, self._character)
        elif match(r'^}$', self._character):
            token = Token(TokenType.RBRACE, self._character)
        elif match(r'^,$', self._character):
            token = Token(TokenType.COMMA, self._character)
        elif match(r'^;$', self._character):
            token = Token(TokenType.SEMICOLON, self._character)
        elif match(r'^<$', self._character):
            token = Token(TokenType.LT, self._character)
        # Funciones auxiliares, en lugar de generar una expresion regular se generan funciones auxiliares
        elif self._is_letter(self._character): # Ahora si nos encontramos frente a un caracter lo que se quiere es generar una literal, donde se genera una funcion y luego se conoce que tipo de Token es
            literal = self._read_identifier()
            # Ahora como podemos tener un identifier o keyword se genera esta funcion
            token_type = lookup_token_type(literal) # Esta funcion se genera en token.py

            return Token(token_type, literal) # Se regresa lo que mande la funcion lookup y la literal
        # Se necesita saber si estamos frente a un numero
        elif self._is_number(self._character):
            literal = self._read_number()

            return Token(TokenType.INT, literal)
        else: # Si no reconoce entonces dirá que es un Token ilegal
            token = Token(TokenType.ILLEGAL, self._character)

        """
        Se tiene que escapar especificamente el caracter de suma porque suma significa algo especifico en las expresiones regulares, significa que haga match por lo menos una o mas veces pero aqui no interesa la funcionalidad sino especificamente el caracter, se escapa con la diagonal
        """
        # Escapar: hacer que el caractér sea tomado cómo texto plano en lugar de su significado por defecto en la expreción regular.

        
        # Se necesita correrlo despues de que se genere el token y antes de regresarlo
        self._read_character()
        
        return token # Se regresa el token
    
    
    # Esta funcion permite saber si estamos frente a una letra que podemos reconocer, recibe como parametro el caracter
    def _is_letter(self, character: str) -> bool:
        return bool(match(r'^[a-záéíóúA-ZÁÉÍÓÚñÑ_]$', character)) # Aqui match se convierte en booleano porque vamos a regresar un booleano, se hace un caracter set con las letras que entiende el lenguaje


    def _is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character)) # Expresion abreviada para encontrar digitos
        

    def _read_number(self) -> str:
        initial_position = self._position  # Se va a leer hasta que se encuentre el final de un numero
        while self._is_number(self._character):
            self._read_character()

        return self._source[initial_position:self._position] 

    def _read_identifier(self) -> str:
        initial_position = self._position

        while self._is_letter(self._character):
            self._read_character() # Funcion que se implemento en el pasado, avanza un caracter

        return self._source[initial_position:self._position]


    def _skip_whitespace(self) -> None:
        while match(r'^\s$', self._character): # \s significa white space
            self._read_character()


    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else: 
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1