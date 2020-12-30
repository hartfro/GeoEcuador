import Provincia
from console import console


def mostrar_menu(provincias):
    nombres_provincias = list(provincias.keys())

    console.print("[bold red]Ingresar el número de la provincia: \n")

    for i, nombre in enumerate(nombres_provincias):
        console.print(f"[green]{i+1}.[/] {nombre}")

    print()
    eleccion = 0

    while True:
        try: 
            eleccion = int(input(": ")) - 1

            if not (eleccion >= 0 and eleccion <= len(nombres_provincias)):
                raise("Elección fuera de límites.")

            provincia = nombres_provincias[eleccion]
            provincia = provincias[provincia]

            provincia.mostrar_informacion()
            break
        except:
            console.print("Número inválido, intente de nuevo.")


if __name__ == "__main__":
    console.clear()
    provincias = Provincia.cargar_provincias()
    
    mostrar_menu(provincias)