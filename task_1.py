from abc import ABC, abstractmethod
import logging
from colorama import Fore, Back, Style, init

# Ініціалізація бібліотеки colorama для кольорового виводу
init(autoreset=True)

# Налаштування системи логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Базовий абстрактний клас для транспортних засобів
class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec: str = "Generic"):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        pass

# Клас автомобіля, який наслідує Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f"{Back.BLUE}{Fore.WHITE} {self.make} {self.model} ({self.region_spec} Spec): Двигун запущено"
        )

# Клас мотоцикла, який наслідує Vehicle
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f"{Back.MAGENTA}{Fore.WHITE} {self.make} {self.model} ({self.region_spec} Spec): Мотор заведено"
        )

# Абстрактна фабрика для створення транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass

# Фабрика для американського ринку
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US")

# Фабрика для європейського ринку
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU")

# Демонстрація роботи фабрик
if __name__ == "__main__":

    # Створення фабрики для США
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Dodge", "Charger")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Fat Boy")

    us_car.start_engine()
    us_motorcycle.start_engine()

    # Створення фабрики для Європи
    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("Audi", "A8")
    eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Panigale V4")

    eu_car.start_engine()
    eu_motorcycle.start_engine()

   