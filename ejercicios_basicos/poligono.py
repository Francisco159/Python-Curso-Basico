# POLIGONOS

"""
* Crea una funcion unica (importante que solo sea una) que sea capaz de calcular y retornar
el area de un poligono
- la funcion recibira por parametro un solo poligono a la vez
- los poligonos soportados seran triangulo, cuadrado y rectangulo
- imprime el calculo del area del poligono de cada tipo
"""
"""
def area_poligono(tipo, base, altura):
    
    Areas de poligonos:
    1: Area del triangulo
    2: Area del cuadrado
    3: Area del rectangulo
    
    if tipo == 1:
        return ((base * altura) / 2)
    elif tipo == 2:
        return (base ** 2)
    elif tipo == 3:
        return (base * altura)
        

if __name__ == "__main__":
    area = area_poligono(1, 4, 5)
    print(f"Area del triangulo: {area}")
    area = area_poligono(2, 4, 5)
    print(f"Area del cuadrado: {area}")
    area = area_poligono(3, 4, 5)
    print(f"Area del rectangulo: {area}")
"""

class Polygon():
    def area(self):
        pass
    def print_area(self):
        pass

class Triangule(Polygon):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return ((self.base * self.altura) / 2)
    
    def print_area(self):
        area_polygon = self.area()
        print(area_polygon)
    
class Square(Polygon):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return ((self.base * self.altura))
    
    def print_area(self):
        area_polygon = self.area()
        print(area_polygon)
        
class Rectangule(Polygon):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return ((self.base * self.altura) / 2)
    
    def print_area(self):
        area_polygon = self.area()
        print(area_polygon)
        

def main():
    area_polygon = Triangule(5, 10)
    area_polygon.print_area()
    area_polygon = Square(5, 18)
    area_polygon.print_area()
    area_polygon = Rectangule(10, 10)
    area_polygon.print_area()


if __name__ == "__main__":
    main()

