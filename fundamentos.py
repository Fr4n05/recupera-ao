#Herança
#Polimorfismo

#Objetivo: reaproveitamento de codigo.

#Exemplo:
from abc import ABC, abstractmethod

#herança
class Pessoa(ABC):
    nome:str # atributo nome
    idade: int
  
  #polimorfismo
    @abstractmethod
    def deveres (self):
        pass
   

class Aluno(Pessoa):
  ra: str
  def deveres (self):
   return "estudar"

class Professor(Pessoa):
   matricula: str
def deveres (self):
   return "ensinar"

#Instanciando:
aluno = Aluno()
aluno.nome = input("Digite seu nome:")
aluno.ra = input("Digite se RA:")
aluno.deveres

professor = Professor()
professor.nome = input ("Digite seu nome:")
professor.matricula = input("Digite sua matricula:")
professor.deveres