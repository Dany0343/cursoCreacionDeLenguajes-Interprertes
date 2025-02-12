from typing import (
    Optional, 
    List,
)

from lpp.ast import Identifier, LetStatement, Program, Statement
from lpp.lexer import Lexer
from lpp.token import (
    Token,
    TokenType,
)

class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self._lexer = lexer
        self._current_token: Optional[Token] = None # Se le pone tipo a este porque el otro se trae de los parametros y este es una variable nueva
        self._peek_token: Optional[Token] = None
        self._errors: List[str] = []

        self._advance_tokens() # Se pone dos veces para poder inicializar ambas variables current_token y peek_token
        self._advance_tokens()

    @property # Esta funcion se utiliza para poder proteger que nadie pueda escribir un error adentro de la variable errores, solo se puede leer y por eso regresa la variable privada errores
    def errors(self) -> List[str]:
        return self._errors

    def parse_program(self) -> Program:
        program: Program = Program(statements=[])

        assert self._current_token is not None # Programacion defensiva
        while self._current_token.token_type != TokenType.EOF:
            statement = self._parse_statement()
            if statement is not None:
                program.statements.append(statement)

            self._advance_tokens()

        return program

    def _advance_tokens(self) -> None:
        self._current_token = self._peek_token
        self._peek_token = self._lexer.next_token()

    def _expected_token(self, token_type: TokenType) -> bool:
        assert self._peek_token is not None
        if self._peek_token.token_type == token_type:
            self._advance_tokens()

            return True

        self._expected_token_error(token_type)
        return False

    def _expected_token_error(self, token_type: TokenType) -> None:
        assert self._peek_token is not None
        error = f'Se esperaba que el siguiente token fuera {token_type} ' + f'pero se obtuvo {self._peek_token.token_type}'
        self._errors.append(error)

    def _parse_let_statement(self) -> Optional[LetStatement]:
        assert self._current_token is not None # Programacion defensiva
        let_statement = LetStatement(token=self._current_token)

        if not self._expected_token(TokenType.IDENT):
            return None

        let_statement.name = Identifier(token=self._current_token, value=self._current_token.literal)

        if not self._expected_token(TokenType.ASSIGN):
            return None
        
        # TODO terminar cuando sepamos parsear expresiones
        while self._current_token.token_type != TokenType.SEMICOLON and self._current_token.token_type != TokenType.EOF:
            self._advance_tokens()
        
        return let_statement
    
    def _parse_statement(self) -> Optional[Statement]:  # Este es un método privado, aquí la unica interfaz publica es parse_program
        assert self._current_token is not None # Programacion defensiva
        if self._current_token.token_type == TokenType.LET:
            return self._parse_let_statement()
        else:
            return None