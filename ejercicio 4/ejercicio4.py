class Pokeball:
    def __init__(self, peso, nombre, precio, fecha):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
        print(f"Se ha creado la pokeball con exito")

    def __str__(self):
        return f"Peso: {self.peso}, nombre:{self.nombre}, precio:{self.precio}, fecha:{self.fecha}"
