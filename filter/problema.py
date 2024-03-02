data = ["manzana.10","banana.20","cereza.30"]

nombres = list(map(lambda x: str.upper(x.split(".")[0]),filter(lambda x: int(x.split(".")[1])>15, data)))

print(nombres)