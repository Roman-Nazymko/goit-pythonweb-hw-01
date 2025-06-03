import logging
from colorama import Fore, Back, init

# Ініціалізація бібліотеки colorama для кольорового виводу
init(autoreset=True)

# Налаштування логера
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)
