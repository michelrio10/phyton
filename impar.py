
class Impar:
  
  def __init__(self):
        self.valor = input(f' Entre com um número ')

  def avaliar(self):
    resultado = int(self.valor) % 2
    return resultado
    

