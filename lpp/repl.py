# Se importa el código previamente escrito para el correcto funcionamiento
from lpp.lexer import Lexer
from lpp.token import (
    Token,
    TokenType
)


EOF_TOKEN: Token = Token(TokenType.EOF, '') # Variable global que nos indica el fin de la oracion


def start_repl() -> None:   # Aquí no tenemos self como parametro ya que es una función global, no pertenece a una clase, no regresa nada

    # Walrus Operator permite generar una asignación al mismo tiempo que se puede generar algún tipo de chequeo dentro de esta variable que se comienza a asignar, muy util dentro de while loops, for loops
    while (source := input('>> ')) != 'salir()':
        lexer: Lexer = Lexer(source)

        while (token :=  lexer.next_token()) != EOF_TOKEN:
            print(token)