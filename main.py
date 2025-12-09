import requests

def dish_fetch(num):
    try:
        url = "https://api-colombia.com/api/v1/TypicalDish"
        response = requests.get(url)
        data = response.json()  

        if num < 1 or num > len(data):
            return {"error": "Plato no encontrado"}

        plato = data[num - 1]  
        return {
            "id": plato.get("id"),               
            "name": plato.get("name"),           
            "description": plato.get("description", "No hay descripción"),
            "region": plato.get("region", "No especificada")
        }

    except requests.exceptions.RequestException:
        return {"error": "No se pudo conectar con la API"}


def main():
    print("¡Hola, estudiante! Bienvenido al menú de platos típicos de Colombia.\n")

    print("Elige un plato por su número:")
    print("1 - Plato 1")
    print("2 - Plato 2")
    print("3 - Plato 3")
    print("... etc (depende de cuántos platos haya en la API)")

    try:
        opcion = int(input("Ingresa el número de tu plato: "))
        info = dish_fetch(opcion)

        if "error" in info:
            print(info["error"])
        else:
            
            print(f"\nID: {info['id']}")
            print(f"Nombre: {info['name']}")
            print(f"Descripción: {info['description']}")
            print(f"Región: {info['region']}")

    except ValueError:
        print("Por favor, ingresa un número válido.")


if __name__ == "__main__":
    main()

