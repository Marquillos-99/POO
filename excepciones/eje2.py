try:
    x = 2/0
except:
    print("entra en exception, error")
finally:
    print("entra en finally, se ejecuta el bloque")