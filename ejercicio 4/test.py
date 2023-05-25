import unittest
from ejercicio4 import Pokeball
from colaPrioridad import Cola

honorball = Pokeball(0.1, "Honorball", 100, "1-1-2020")
superball = Pokeball(0.2, "Superball", 200, "2-1-2020")
ultraball = Pokeball(0.3, "Ultraball", 300, "1-1-2020")
masterball = Pokeball(0.4, "Masterball", 9999, "1-1-2020")
turnoball = Pokeball(0.2, "Turnoball", 400, "1-3-2020")

class TestPokeball(unittest.TestCase):
    def testmostrarValores(self):
        lista = Cola()
        lista.añadir(honorball, honorball.fecha)
        lista.añadir(superball, superball.fecha)
        lista.añadir(ultraball, ultraball.fecha)
        lista.añadir(masterball, masterball.fecha)
        lista.añadir(turnoball, turnoball.fecha)
        self.assertEqual(honorball.__str__(), "Peso: 0.1, nombre:Honorball, precio:100, fecha:1-1-2020")
        self.assertEqual(ultraball.__str__(), "Peso: 0.3, nombre:Ultraball, precio:300, fecha:1-1-2020")
        self.assertEqual(masterball.__str__(), "Peso: 0.4, nombre:Masterball, precio:9999, fecha:1-1-2020")
        self.assertEqual(turnoball.__str__(), "Peso: 0.2, nombre:Turnoball, precio:400, fecha:1-3-2020")
        self.assertEqual(superball.__str__(), "Peso: 0.2, nombre:Superball, precio:200, fecha:2-1-2020")

    def modificar(self):
        honorball.precio = 300
        self.assertEqual(honorball.precio, 300)

if __name__ == "__main__":
    unittest.main()