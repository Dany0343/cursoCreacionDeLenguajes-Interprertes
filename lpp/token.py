# Se van a importar varias cosas
from enum import (
    auto, # Permite que automaticamente se asigne un valor al enum
    Enum, # Se trae clase Enum
    unique, # Decorador el cual permite definir que los enums son unicos
)
from typing import NamedTuple 

@unique # Se le añade el decorador unique pora saber que los tokens son unicos, un decorador recibe como parametro una funcion, le añade cosas, la ejecuta y retorna a esta misma función pero ya modificada, por eso se dice que retorna una función diferente
class TokenType(Enum):
    # Es buena practica ponerlos en orden alfabetico
    ASSIGN = auto()
    COMMA = auto()
    EOF = auto()
    FUNCTION = auto()
    IDENT = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    # Dounder method string que permite saber cuando se imprime el token que hay dentro
    # __str__ permite controlar la funcion global o el built-in function str
    # En python se pueden controlar que es lo que hace el simbolo de suma, len, comparaciones, todos con dunder methods
    def __str__(self) -> str: # La flecha significa en el mundo de typing de python que esta función va a regresar un string
        return f'Type: {self.token_type}, Literal: {self.literal}'