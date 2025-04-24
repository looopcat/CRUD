import requests
from prettytable import PrettyTable

class IndicadoresController:
    
    def consultar_dolar(self):
        indicador = "dolar"
        url = f"https://mindicador.cl/api/{indicador}"
        response = requests.get(url)
        data = response.json()

        print(f"Valor actual del {data['nombre']}:")
        print(f"${data['serie'][0]['valor']}")
    
    def consultar_euro(self):
        indicador = "euro"
        url = f"https://mindicador.cl/api/{indicador}"
        response = requests.get(url)
        data = response.json()

        print(f"Valor actual del {data['nombre']}:")
        print(f"${data['serie'][0]['valor']}")    
        
    def consultar_uf_reciente(self):
        indicador = "uf"
        url = f"https://mindicador.cl/api/{indicador}"
        response = requests.get(url)
        data = response.json()

        table = PrettyTable()
        table.field_names = ["Fecha", "Valor"]

        for item in data['serie'][:10]:  # Mostrar los últimos 10 valores
            table.add_row([item['fecha'][:10], f"${item['valor']}"])

        print(f"Valores recientes de {data['nombre']}:")
        print(table)