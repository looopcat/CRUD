from urllib import request
import json

class Indicadores:
    def mostrar_info_api(self):
        url = 'https://mindicador.cl/api'
        try:
            pagina = request.urlopen(url)
            datos = pagina.read().decode("utf-8")
            data = json.loads(datos)
            pretty_json = json.dumps(data, indent=2)
            print("Datos recibidos de la API:")
            print(pretty_json)
        except Exception as e:
            print(f"Error al conectarse a la API: {e}")

        