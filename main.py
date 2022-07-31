
'''
#Função type para saber o tipo de uma variável
varX = 1_000_000.00
print(type(varX))

#Convertendo para inteiro com int()
varX = int(varX)
print(type(varX))
'''

'''
# Calcularadora IMC
from calculadora import Calculadora
c = Calculadora()
resultado = c.imc()
print(f'Seu índice de massa corporal (IMC) é {resultado} kg/m2')
'''


# Mostra o resultado de uma divisão
from impar import Impar
i = Impar()
resultado = i.avaliar()

if resultado==0:
 print ('Par')
else:
 print ('Impar')

