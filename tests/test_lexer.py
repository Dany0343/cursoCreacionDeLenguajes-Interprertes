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


    def test_one_character_operator(self) -> None: # Test para reconocer los operadores de un caracter
        source: str = '=+'
        lexer: Lexer = Lexer(source) # Inicializamos el Lexer pasandole como argumento el source
        tokens: List[Token] = [] # Se genera la lista de tokens que el lexer debería de devolver
        for i in range(len(source)): # Se hace un loop a lo largo de Lexer y en cada loop se llama a next_token para ir populando o añadiendo cada Token a la lista de tokens
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
        ]
        self.assertEquals(tokens, expected_tokens)
    
    
    def test_eof(self) -> None: # Test para revisar si ya se acabo el programa
        source: str = '+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1): # Se le suma + 1 para que nos regrese el token eof
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, '')
        ]
        self.assertEquals(tokens, expected_tokens) # Se revisa que los tokens que aviente el lexer sean especificamente los tokens que tenemos en expected tokens
    

    # Challenge
    def test_delimiters(self) -> None:
        source = '(){},;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]
        self.assertEquals(tokens, expected_tokens) # Se revisa que los tokens que aviente el lexer sean especificamente los tokens que tenemos en expected tokens