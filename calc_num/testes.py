import numpy as np

def lista_2_exer_5_1(x):
    x_quad = x * x
    ln_x = np.log(x)
    resultado = x_quad + ln_x
    return resultado

print(lista_2_exer_5_1(0.5))
print(lista_2_exer_5_1(1))

def lista_2_exer_5_2(x):
    x_e_x = x*(np.e**x)
    resultado = x_e_x - 1
    return resultado

print(lista_2_exer_5_2(0.5))
print(lista_2_exer_5_2(1))