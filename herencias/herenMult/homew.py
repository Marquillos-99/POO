class Empresas:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"


class TipoIndustria(Empresas):
    def __init__(self, nombre, rubro):
        super().__init__(nombre)
        self.rubro = rubro

    def __str__(self):
        return f"{self.nombre} es una empresa del rubro {self.rubro}"


class Enlatado(TipoIndustria):
    def __init__(self, nombre, tipo_envase):
        super().__init__(nombre, "Alimentos")
        self.tipo_envase = tipo_envase

    def __str__(self):
        return f"{self.nombre} envasa en {self.tipo_envase}"


class Comida(TipoIndustria):
    def __init__(self, nombre, tipo_producto):
        super().__init__(nombre, "Alimentos")
        self.tipo_producto = tipo_producto

    def __str__(self):
        return f"{self.nombre} produce {self.tipo_producto}"


class Atun(Enlatado, Comida):
    def __init__(self, nombre, tipo_envase, especie):
        super().__init__(nombre, tipo_envase)
        Comida.__init__(self, nombre, "atún enlatado")
        self.especie = especie

    def __str__(self):
        return f"{self.nombre} es un atún envasado en {self.tipo_envase}, de la especie {self.especie}"


atun = Atun("Atún Programador", "lata", "aleta amarilla")

print(atun)
print(atun.rubro,atun.nombre,atun.tipo_envase,atun.especie,atun.tipo_producto)
