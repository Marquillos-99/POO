try:
    with open('folio.txt') as file:
        read_data = file.read()
except IOError:
    print('No se pudo abrir')