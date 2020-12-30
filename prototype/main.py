import Provincia
from console import console


def mostrar_informacion(provincia):
    console.clear()

    console.print(f'''
[bold red]{provincia.nombre}[/]\n
[green]Región:[/] {provincia.region.nombre}\n
[green]Capital:[/] {provincia.capital}\n
[green]Descripción:[/]\n\n{provincia.descripcion}\n 
[green]Puntos de interés:[/]\n\n[white]{", ".join(provincia.puntos_interes)}
    ''')


def mostrar_menu(provincias):
    nombres_provincias = list(provincias.keys())

    console.print("[bold red]Ingresar el número de la provincia: \n")

    for i, nombre in enumerate(nombres_provincias):
        console.print(f"[green]{i+1}.[/] {nombre}")

    print()
    eleccion = 0

    eleccion = int(input(": ")) - 1
    provincia = nombres_provincias[eleccion]
    provincia = provincias[provincia]

    mostrar_informacion(provincia)


if __name__ == "__main__":
    console.clear()
    provincias = Provincia.inicializar_provincias()
    
    mostrar_menu(provincias)