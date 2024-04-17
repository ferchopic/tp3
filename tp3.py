import time

# Punto 1: Clase para calcular factorial con patrón Singleton
class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n-1)

# Punto 2: Clase para el cálculo de impuestos
class TaxCalculator:
    def calculate_taxes(self, base_amount):
        iva = base_amount * 0.21
        iibb = base_amount * 0.05
        municipal_contributions = base_amount * 0.012
        total_taxes = iva + iibb + municipal_contributions
        return total_taxes

# Punto 3: Clase para la comida rápida "hamburguesa"
class Hamburguesa:
    def entrega(self, metodo):
        print(f"La hamburguesa se entregará por {metodo}")

# Punto 4: Clase para generar facturas con diferentes tipos de IVA
class Factura:
    def __init__(self, importe, tipo_iva):
        self.importe = importe
        self.tipo_iva = tipo_iva

    def generar_factura(self):
        if self.tipo_iva == "Responsable":
            print("Factura con IVA Responsable")
        elif self.tipo_iva == "No Inscripto":
            print("Factura con IVA No Inscripto")
        elif self.tipo_iva == "Exento":
            print("Factura con IVA Exento")
        else:
            print("Tipo de IVA no válido")

# Punto 5: Clase para construir aviones
class Avion:
    def __init__(self):
        self.body = "Body del avión"
        self.turbinas = ["Turbina 1", "Turbina 2"]
        self.alas = ["Ala 1", "Ala 2"]
        self.tren_de_aterrizaje = "Tren de aterrizaje"

# Punto 6: Clase para simular anidamientos con carga de procesamiento
class Procesamiento:
    def cargar(self):
        time.sleep(2)
        print("Procesamiento completado")

class Anidamiento:
    def __init__(self):
        self.procesamiento = Procesamiento()

    def cargar_anidamientos(self, n):
        for _ in range(n):
            self.procesamiento.cargar()

# Punto 7: Patrón Abstract Factory
from abc import ABC, abstractmethod

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def crear_producto(self):
        pass

# Concrete Factory 1
class ConcreteFactory1(AbstractFactory):
    def crear_producto(self):
        return Producto1()

# Concrete Factory 2
class ConcreteFactory2(AbstractFactory):
    def crear_producto(self):
        return Producto2()

# Abstract Product
class AbstractProduct(ABC):
    @abstractmethod
    def operacion(self):
        pass

# Concrete Product 1
class Producto1(AbstractProduct):
    def operacion(self):
        print("Operación del Producto 1")

# Concrete Product 2
class Producto2(AbstractProduct):
    def operacion(self):
        print("Operación del Producto 2")

# Uso de las clases

# Punto 1
factorial_calculator = FactorialCalculator()
print(factorial_calculator.calculate_factorial(5))  # Output: 120

# Punto 2
tax_calculator = TaxCalculator()
print(tax_calculator.calculate_taxes(1000))  # Output: 238.2

# Punto 3
hamburguesa = Hamburguesa()
hamburguesa.entrega("mostrador")  # Output: La hamburguesa se entregará por mostrador

# Punto 4
factura1 = Factura(100, "Responsable")
factura1.generar_factura()  # Output: Factura con IVA Responsable

# Punto 5
avion = Avion()
print(avion.body)
print(avion.turbinas)
print(avion.alas)
print(avion.tren_de_aterrizaje)

# Punto 6
anidamiento = Anidamiento()
anidamiento.cargar_anidamientos(20)

# Punto 7
factory1 = ConcreteFactory1()
producto1 = factory1.crear_producto()
producto1.operacion()  # Output: Operación del Producto 1

factory2 = ConcreteFactory2()
producto2 = factory2.crear_producto()
producto2.operacion()  # Output: Operación del Producto 2
