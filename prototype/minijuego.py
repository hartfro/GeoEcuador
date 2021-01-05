#TODO: Guardar puntaje
#TODO: Evitar preguntas repetidas.
#TODO: Importar y utilizar rich para mejorar la presentación.

# Minijuego de la aplicación GeoEcuador: comprueba tu conocimiento.
import random

class SetPreguntas:
    """Clase que representa un conjunto de preguntas que son consideradas del mismo tipo/categoría."""
    def __init__(self, nombre, nucleos, formato):
        """
        Construir un SetPreguntas.

        Parámetros
        ----------
            nombre {str} -- nombre del set.
            nucleos {dict} -- pares key-value de "núcleos" de pregunta con su respuesta.
                Ej. {"Azuay": "Cuenca", "Pichincha", "Quito"}
            formato {func} -- determina el formato al imprimir la pregunta."
                Ej. lambda nucleo: f"¿Cuál es la capital de {nucleo}?"
        """
        self.nombre = nombre
        self.nucleos = nucleos
        self.formato = formato

    def obtener_pregunta(self, nucleo):
        return self.formato(nucleo)

    def obtener_respuesta(self, nucleo):
        return self.nucleos[nucleo]

    def obtener_nucleo_aleatorio(self):
        nucleos_pregunta = list(self.nucleos.keys())
        nucleo_aleatorio = random.choice(nucleos_pregunta)
        return nucleo_aleatorio

    def obtener_respuestas_aleatorias(self, respuesta_correcta="", n=4):
        """Devuelve una lista de respuestas aleatorias.
        respuesta_correcta será siempre añadida si es provista."""
        nucleos_pregunta = list(self.nucleos.keys())

        options = []

        if respuesta_correcta:
            options.append(respuesta_correcta)


        for i in range(n):
            if nucleos_pregunta:
                rand_pregunta = random.choice(nucleos_pregunta)
                rand_respuesta = self.obtener_respuesta(rand_pregunta)

                if rand_respuesta not in options and rand_pregunta in nucleos_pregunta:
                    options.append(rand_respuesta)
                    del nucleos_pregunta[nucleos_pregunta.index(rand_pregunta)]
            else:
                nucleos_pregunta = list(self.nucleos.keys())

        random.shuffle(options)
        return options


def iniciar_minijuego():
    nucleos_capitales = {
        "Azuay": "Cuenca",
        "Bolívar": "Guaranda",
        "Cañar": "Azogues",
        "Carchi": "Tulcán",
        "Chimborazo": "Riobamba",
        "Cotopaxi": "Latacunga",
        "El Oro": "Machala",
        "Esmeraldas": "Esmeraldas",
        "Galápagos": "Puerto Baquerizo Moreno",
        "Guayas": "Guayaquil",
        "Imbabura": "Ibarra",
        "Loja": "Loja",
        "Los Ríos": "Babahoyo",
        "Manabí": "Portoviejo",
        "Morona Santiago": "Macas",
        "Napo": "Tena",
        "Orellana": "Coca",
        "Pastaza": "Puyo",
        "Pichincha": "Quito",
        "Santa Elena": "Santa Elena",
        "Santo Domingo de los Tsáchilas": "Santo Domingo",
        "Sucumbíos": "Nueva Loja",
        "Tungurahua": "Ambato",
        "Zamora Chinchipe": "Zamora"
    }
    nucleos_regiones = {
        "Azuay": "Sierra",
        "Bolívar": "Sierra",
        "Cañar": "Sierra",
        "Carchi": "Sierra",
        "Chimborazo": "Sierra",
        "Cotopaxi": "Sierra",
        "El Oro": "Costa",
        "Esmeraldas": "Costa",
        "Galápagos": "Insular",
        "Guayas": "Costa",
        "Imbabura": "Sierra",
        "Loja": "Sierra",
        "Los Ríos": "Costa",
        "Manabí": "Costa",
        "Morona Santiago": "Amazonía",
        "Napo": "Amazonía",
        "Orellana": "Amazonía",
        "Pastaza": "Amazonía",
        "Pichincha": "Sierra",
        "Santa Elena": "Costa",
        "Santo Domingo de los Tsáchilas": "Sierra",
        "Sucumbíos": "Amazonía",
        "Tungurahua": "Sierra",
        "Zamora Chinchipe": "Amazonía"
    }
    nucleos_puntos_interes = {
        "Azuay": "Parque Nacional Cajas",
        "Bolívar": "Carnaval de Guaranda",
        "Cañar": "Ruinas de Ingapirca",
        "Carchi": "Cementerio Municipal de Tulcán",
        "Chimborazo": "Volcán Chimborazo",
        "Cotopaxi": "Volcán Cotopaxi",
        "El Oro": "Archipiélago de Jambelí",
        "Esmeraldas": "Playa de Tonsupa",
        "Galápagos": "Bahía Tortuga",
        "Guayas": "Las Peñas",
        "Imbabura": "Laguna de Cuicocha",
        "Loja": "Parque Nacional Podocarpus",
        "Los Ríos": "La Casa de Olmedo",
        "Manabí": "Playa de los Frailes",
        "Morona Santiago": "Laguna Negra",
        "Napo": "Río Misahuallí",
        "Orellana": "Parque Nacional Yasuní",
        "Pastaza": "Ruta de los Shamanes",
        "Pichincha": "Centro histórico de Quito",
        "Santa Elena": "Punto rocoso de La Chocolatera",
        "Santo Domingo de los Tsáchilas": "Parque Zaracay",
        "Sucumbíos": "Reserva de Producción Faunística Cuyabeno",
        "Tungurahua": "Baños de Agua Santa",
        "Zamora Chinchipe": "Centinela del Cóndor"
    }

    # Inicializar sets de preguntas.
    set_capitales = SetPreguntas("Capitales", nucleos_capitales, lambda provincia: f"¿Cuál es la capital de {provincia}?")
    set_regiones = SetPreguntas("Regiones", nucleos_regiones, lambda provincia: f"¿En qué región se encuentra la provincia de {provincia}?")
    set_puntos_interes = SetPreguntas("Puntos de Interés", nucleos_puntos_interes,
        lambda provincia: f"¿Cuál de los siguientes es un punto de interés o un evento representativo de la provincia de {provincia}")

    lista_sets = [set_capitales, set_regiones, set_puntos_interes]

    while True:
        # Elegir un set aleatorio
        random_set = random.choice(lista_sets)
        random_nucleo = random_set.obtener_nucleo_aleatorio()
        random_question = random_set.obtener_pregunta(random_nucleo)

        respuesta_correcta = random_set.obtener_respuesta(random_nucleo)
        opciones = random_set.obtener_respuestas_aleatorias(respuesta_correcta)

        print(random_question, "\n")

        # Imprimir opciones
        for i, opcion in enumerate(opciones):
            print(f"{i+1}. {opcion}")

        # Pedir input
        while True:
            try:
                eleccion = int(input(f"\n: "))
                eleccion = eleccion - 1
                break
            except:
                print("Input inválido.")
                continue

        respuesta_elegida = opciones[eleccion]

        # Revisar respuesta elegida
        if respuesta_elegida == respuesta_correcta:
            print("\n¡Muy bien! ¡Respuesta correcta!")
        else:
            print(f"Lo siento, es incorrecto :( La respuesta correcta es {respuesta_correcta}")

        # Preguntar si quiere jugar de nuevo
        jugar_de_nuevo = ""
        while True:
            try:
                jugar_de_nuevo = input("\n¿Seguir jungando? (s/n): ").lower()

                if jugar_de_nuevo == "s":
                    print("\n")
                    jugar_de_nuevo = True
                elif jugar_de_nuevo == 'n':
                    jugar_de_nuevo = False
                else:
                    raise Exception

                break
            except Exception as e:
                print("Input inválido. Intente de nuevo.")
                continue

        if jugar_de_nuevo:
            continue
        else:
            print("\nGracias por jugar c:")
            break


# # Preguntas al azar (capital, región o punto de interés) hasta acabar con la lista de preguntas o hasta que el usuario decida terminar la partida.
# def iniciar_minijuego():
#     tipos_preguntas = ["capitales", "regiones", "puntos de interés"]

#     while True:

#         pregunta_escogida = random.choice(tipos_preguntas)

#         if pregunta_escogida == "capitales":

#         # Preguntas capitales

#             preguntas = {
#                 "Azuay": "Cuenca",
#                 "Bolívar": "Guaranda",
#                 "Cañar": "Azogues",
#                 "Carchi": "Tulcán",
#                 "Chimborazo": "Riobamba",
#                 "Cotopaxi": "Latacunga",
#                 "El Oro": "Machala",
#                 "Esmeraldas": "Esmeraldas",
#                 "Galápagos": "Puerto Baquerizo Moreno",
#                 "Guayas": "Guayaquil",
#                 "Imbabura": "Ibarra",
#                 "Loja": "Loja",
#                 "Los Ríos": "Babahoyo",
#                 "Manabí": "Portoviejo",
#                 "Morona Santiago": "Macas",
#                 "Napo": "Tena",
#                 "Orellana": "Coca",
#                 "Pastaza": "Puyo",
#                 "Pichincha": "Quito",
#                 "Santa Elena": "Santa Elena",
#                 "Santo Domingo de los Tsáchilas": "Santo Domingo",
#                 "Sucumbíos": "Nueva Loja",
#                 "Tungurahua": "Ambato",
#                 "Zamora Chinchipe": "Zamora"
#             }

#             prov_keys = preguntas.keys()
#             provinces= []
#             for element in prov_keys:
#                 provinces.append(element)

#             random_province = random.choice(provinces)
#             capital = preguntas.get(random_province)

#             options = []
#             options.append(capital)


#             while len(options) < 4:
#                 rand_option = preguntas.get(random.choice(provinces))
#                 if rand_option not in options:
#                     options.append(rand_option)

#             random.shuffle(options)

#             print("¿Cuál es la capital de", random_province, "?\n")
#             for i, option in enumerate(options):
#                 print(f"{i+1}. {option}")

#             answer = input("\nIngresa tu respuesta: ")
#             if answer == capital:
#                 print("¡Muy bien!")
#             else:
#                 print("Lo siento, es incorrecto :(")

#             answer = input("¿Seguir jungando? (si o no)")
#             if answer == "no":
#                 break

#         if pregunta_escogida == "regiones":

#         # Preguntas regiones

#             preguntas = {
#                 "Azuay": "Sierra",
#                 "Bolívar": "Sierra",
#                 "Cañar": "Sierra",
#                 "Carchi": "Sierra",
#                 "Chimborazo": "Sierra",
#                 "Cotopaxi": "Sierra",
#                 "El Oro": "Costa",
#                 "Esmeraldas": "Costa",
#                 "Galápagos": "Insular",
#                 "Guayas": "Costa",
#                 "Imbabura": "Sierra",
#                 "Loja": "Sierra",
#                 "Los Ríos": "Costa",
#                 "Manabí": "Costa",
#                 "Morona Santiago": "Amazonía",
#                 "Napo": "Amazonía",
#                 "Orellana": "Amazonía",
#                 "Pastaza": "Amazonía",
#                 "Pichincha": "Sierra",
#                 "Santa Elena": "Costa",
#                 "Santo Domingo de los Tsáchilas": "Sierra",
#                 "Sucumbíos": "Amazonía",
#                 "Tungurahua": "Sierra",
#                 "Zamora Chinchipe": "Amazonía"
#             }

#             prov_keys = preguntas.keys()
#             provinces= []
#             for element in prov_keys:
#                 provinces.append(element)

#             random_province = random.choice(provinces)
#             region = preguntas.get(random_province)

#             options = []
#             options.append(region)


#             while len(options) < 4:
#                 rand_option = preguntas.get(random.choice(provinces))
#                 if rand_option not in options:
#                     options.append(rand_option)

#             random.shuffle(options)

#             print("¿En qué región se encuentra la provincia de", random_province, "?\n")
#             for i, option in enumerate(options):
#                 print(f"{i+1}. {option}")

#             answer = input("\nIngresa tu respuesta: ")
#             if answer == region:
#                 print("¡Muy bien!")
#             else:
#                 print("Lo siento, es incorrecto :(")

#             answer = input("¿Seguir jungando? (si o no)")
#             if answer == "no":
#                 break

#         if pregunta_escogida == "puntos de interés":

#         # Preguntas puntos de interés o eventos representativos

#             preguntas = {
#                 "Azuay": "Parque Nacional Cajas",
#                 "Bolívar": "Carnaval de Guaranda",
#                 "Cañar": "Ruinas de Ingapirca",
#                 "Carchi": "Cementerio Municipal de Tulcán",
#                 "Chimborazo": "Volcán Chimborazo",
#                 "Cotopaxi": "Volcán Cotopaxi",
#                 "El Oro": "Archipiélago de Jambelí",
#                 "Esmeraldas": "Playa de Tonsupa",
#                 "Galápagos": "Bahía Tortuga",
#                 "Guayas": "Las Peñas",
#                 "Imbabura": "Laguna de Cuicocha",
#                 "Loja": "Parque Nacional Podocarpus",
#                 "Los Ríos": "La Casa de Olmedo",
#                 "Manabí": "Playa de los Frailes",
#                 "Morona Santiago": "Laguna Negra",
#                 "Napo": "Río Misahuallí",
#                 "Orellana": "Parque Nacional Yasuní",
#                 "Pastaza": "Ruta de los Shamanes",
#                 "Pichincha": "Centro histórico de Quito",
#                 "Santa Elena": "Punto rocoso de La Chocolatera",
#                 "Santo Domingo de los Tsáchilas": "Parque Zaracay",
#                 "Sucumbíos": "Reserva de Producción Faunística Cuyabeno",
#                 "Tungurahua": "Baños de Agua Santa",
#                 "Zamora Chinchipe": "Centinela del Cóndor"
#             }

#             prov_keys = preguntas.keys()
#             provinces= []
#             for element in prov_keys:
#                 provinces.append(element)

#             random_province = random.choice(provinces)
#             puntoint = preguntas.get(random_province)

#             options = []
#             options.append(puntoint)


#             while len(options) < 4:
#                 rand_option = preguntas.get(random.choice(provinces))
#                 if rand_option not in options:
#                     options.append(rand_option)

#             random.shuffle(options)

#             print("¿Cuál de los siguientes es un punto de interés o un evento representativo de la provincia de", random_province, "?\n")
#             for i, option in enumerate(options):
#                 print(f"{i+1}. {option}")

#             answer = input("\nIngresa tu respuesta: ")
#             if answer == puntoint:
#                 print("\n¡Muy bien!")
#             else:
#                 print("\nLo siento, es incorrecto :(")

#             answer = input("¿Seguir jungando? Si ya no quieres jugar, escribe no: ")
#             if answer == "no":
#                 break

# For testing
if __name__ == "__main__":
    iniciar_minijuego()