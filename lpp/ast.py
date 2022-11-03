'''
Las clases abstractas, como su nombre lo indica, son algo abstracto, no representan algo específico y las podemos usar para crear otras clases. No pueden ser instanciadas, por lo que no podemos crear nuevos objetos con ellas.
También podemos hacer lo mismo con los métodos: si una clase tiene métodos abstractos, entonces nuestra clase deberá ser abstracta.
'''
from abc import ( # abc es abstract base class, una clase abstracta es basicamente una receta para posteriores clases que la van a heredar, tienen que tener los mismos métodos 
    ABC,
    abstractmethod,
)

from lpp.token import Token
from typing import (
    List,
    Optional,
)

class ASTNode(ABC):
    @abstractmethod # Se utiliza la funcion como decorador para señalar que es un método abstracto
    def token_literal(self) -> str: # Se usa principalmente para generar debugging y ver que todo funciona dentro de los nodos
        pass # Si se trata de inicializar ASTNode daría un error, si se intenta inicializar una subclase que no implementa uno de estos métodos tambien daría error el interprete de Python

    @abstractmethod
    def __str__(self) -> str:
        pass

# Estos 2 nodos son los nodos principales, no se van a inicializar jamás, se podría pero no se hará. Ya que solo se van a utilizar como referencias de tipos

class Statement(ASTNode): 
    def __init__(self, token: Token) -> None: # Constructor que recibe un token, no regresa nada y lo unico que hace es inicializar este token en una variable llamada token
        self.token = token

    def token_literal(self) -> str: # Se tienen que implementar los métodos del padre
        return self.token.literal # Simplemente el pedazo de string del programa que está en ese token

    # No se va a implementar el dunder __str__ dentro de Statement, lo cual provoca que no se pueda inicializar porque habría un error de ASTNode porque la clase abstracta dice que tenemos que implementarlo, pero no hay problema porque nunca se va a inicializar Statement de manera directa


class Expression(ASTNode):
    def __init__(self, token: Token) -> None:
        self.token = token

    def token_literal(self) -> str:
        return self.token.literal


class Program(ASTNode):
    def __init__(self, statements: List[Statement]) -> None:
        self.statements = statements

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal() # Para Debugging, llama a la funcion token_literal de la clase Statement

        return '' # Si no hay nada se regresa un string vacío
    
    def __str__(self) -> str: # Como este si se inicializa si se implementa el dunder method, ya que es parte de la clase abstracta
        out: List[str] = []
        for statement in self.statements:
            out.append(str(statement))

        return ''.join(out) # Se regresa una concatenacion de todos los statements


class Identifier(Expression): # Se pone arriba de LetStatement porque los scripts se leen de arriba hacía abajo
    def __init__(self, token: Token, value: str) -> None:
        super().__init__(token)
        self.value = value
    
    def __str__(self) -> str:
        return self.value


class LetStatement(Statement): # Es un nodo de tipo statement
    # Optional es algo nuevo de typing, por ejemplo nombre puede ser o un identificador o None esa es su sintaxis
    def __init__(self, token: Token, name: Optional[Identifier] = None, value: Optional[Expression] = None) -> None:
        super().__init__(token) # Se inicializa la super clase ya que se está extendiendo statement y statement necesita un token para inicializarse
        self.name = name
        self.value = value

    def __str__(self) -> str: # token_literal ya lo implementa statement, a menos que se quiera hacer un override a token_literal se puede utilizar el método de statement que estamos heredando al ser una subclase de statement
        return f'{self.token_literal()} {str(self.name)} = {str(self.value)};'