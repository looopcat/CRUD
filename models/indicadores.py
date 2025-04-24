from urllib import request
import json

class Indicadores:
    def InfoApi(self):
        url = 'https://mindicador.cl/api'
        pagina = request.urlopen(url)
        datos = pagina.read().decode("utf-8")
        data = json.loads(datos)
        pretty_json = json.dumps(data, indent=2)
        print("Datos recibidos de la API:")
        print(pretty_json)
        return data


if __name__ == "__main__":
    ind = Indicadores()
    datos = ind.InfoApi()
    
    if 'serie' in datos and datos['serie']:
        primer_dato = datos['serie'][0]
        print("\nPrimer valor obtenido del indicador:")
        print(f"Fecha: {primer_dato['fecha'][:10]}, Valor: ${primer_dato['valor']}")
    else:
        print("No se encontraron datos en la respuesta de la API.")
        