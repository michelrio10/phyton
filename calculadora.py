

class Calculadora:
  
  def __init__(self):
        self.altura = input("enter your height (altura ex 1.85) in m: ")
        self.peso = input("enter your weight (peso) in kg: ")


  def imc(self):
    return int ( (float(self.peso) / float(self.altura) **2) )


