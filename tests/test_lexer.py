from unittest import TestCase # Clase para hacer testing

# Se procede a definir lo que falta despues del testing
from typing import List

from lpp.token import (
    Token,
    TokenType,
)
from lpp.lexer import Lexer


class LexerTest(TestCase): # Se extiende de TestCase para hacer testing, es una clase para hacer test
    # Cada uno de los tests se harán dentro de una función
    def testIllegal(self) -> None:  # Primer test es probar que el lexer regrese los tokens ilegales
        source: str = '¡¿@'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = [] # No existe por ahora pero los tests nos van guiando
        for i in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@'),
        ]

        # Ultimo paso del test, todos los test siguen esta estructura
        # Assemble, act, assertion
        self.assertEquals(tokens, expected_tokens)
