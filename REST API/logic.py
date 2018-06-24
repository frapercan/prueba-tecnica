import numpy as np
import requests
import pandas as pd
import base64

# string : boolean
def es_palindromo(cadena):
    cadena = cadena.replace(' ','')
    cadena = cadena.lower()
    return cadena == cadena[::-1]

# string : int
def contador_de_palabras(cadena):
    return len(cadena.split())

# int : int
def factorial(numero):
    return np.prod(range(1,numero+1))


# string -- array de bytes : base64
def cifrador(cadena):
    cadena_ws = bytearray(cadena,'utf-8').replace(b' ',b'-')  #ws - sin espacios
    cadena_rd_ws = rotar_derecha_bytearray(cadena_ws)       #rd - rotada a la derecha un bit
    return base64.b64encode(cadena_rd_ws).decode('ascii')

# base64 -- array de bytes : string
def descifrador(byte_array):
    cadena_rd_ws = bytearray(base64.b64decode(byte_array)) 
    cadena = rotar_izquierda_bytearray(cadena_rd_ws).replace(b'-',b' ')
    return cadena.decode('utf-8')


# bytearray : bytearray    
def rotar_derecha_bytearray(cadena):
    for i in range(len(cadena)):
        cadena[i] = rotar_derecha(cadena[i])
    return cadena

# bytearray : bytearray  
def rotar_izquierda_bytearray(cadena):
    for i in range(len(cadena)):
        cadena[i] = rotar_izquierda(cadena[i])
    return cadena

# byte : byte
def rotar_izquierda(num, bits = 8):
    bit = num & (1 << (bits-1))
    num <<= 1
    if(bit):
        num |= 1
    num &= (2**bits-1)
    return num

# byte : byte
def rotar_derecha(num, bits = 8):
    num &= (2**bits-1)
    bit = num & 1
    num >>= 1
    if(bit):
        num |= (1 << (bits-1))
    return num

#string : pandas.core.frame.DataFrame
def encontrar_paises_por_capital(capital):
    base_url = 'https://restcountries.eu/rest/v2/all'
    paises_del_mundo_df = pd.DataFrame(requests.get(base_url).json())
    if capital in paises_del_mundo_df.capital.values:
        return paises_del_mundo_df[paises_del_mundo_df.capital==capital].name.values[0]
    
    



