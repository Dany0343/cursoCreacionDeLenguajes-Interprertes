'''
Las clases abstractas, como su nombre lo indica, son algo abstracto, no representan algo específico y las podemos usar para crear otras clases. No pueden ser instanciadas, por lo que no podemos crear nuevos objetos con ellas.
También podemos hacer lo mismo con los métodos: si una clase tiene métodos abstractos, entonces nuestra clase deberá ser abstracta.
'''
from abc import ( # abc es abstract base class, una clase abstracta es basicamente una receta para posteriores clases que la van a heredar, tienen que tener los mismos métodos 
    ABC,
    abstractmethod,
)

from lpp.token import Token


class ASTNode(ABC):
    @abstractmethod # Se utiliza la funcion como decorador para señalar que es un método abstracto
    def token_literal(self) -> str: # Se usa principalmente para generar debugging y ver que todo funciona dentro de los nodos
        pass # Si se trata de inicializar ASTNode daría un error, si se intenta inicializar una subclase que no implementa uno de estos métodos tambien daría error el interprete de Python

    @abstractmethod
    def __str__(self) -> str:
        pass

# Estos 2 nodos de abajo no se van a inicializar jamás, se podría pero no se hará. Ya que solo se van a utilizar como referencias de tipos

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


