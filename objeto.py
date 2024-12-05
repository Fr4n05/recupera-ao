#Programaçao Orientada a Objeto- POO

#Objeto?
#quando usa-se uma classe para definir caracteristicas.

#Exemplo: 
class Pessoa:
    nome:str # atributo nome
    idade: int
    peso:float
    
#instanciar objeto
variavel = Pessoa()

#Exemplo 

variavel.nome = input("Digite seu nome:")
variavel.idade = int("Digite sua idade:")
variavel.float = float("Digite seu peso:")