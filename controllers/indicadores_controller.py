import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.indicadores import Indicadores

class IndicadoresController:
    def __init__(self):
        self.ind = Indicadores()

    def mostrar_todos_los_indicadores(self):
        self.ind.mostrar_info_api()
