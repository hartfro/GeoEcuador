#Minijuego de la aplicación GEOEcuador: comprueba tu conocimiento
import random

#Preguntas al azar (capital, región o punto de interés) hasta acabar con la lista de preguntas o hasta que el usuario decida terminar la partida

lista_preguntas = ["capitales", "regiones", "puntos de interés"]

while True:

    pregunta_escogida = random.choice(lista_preguntas)

    if pregunta_escogida == "capitales":

    #Preguntas capitales

        dict = {"Azuay":"Cuenca", "Bolívar":"Guaranda", "Cañar":"Azogues", "Carchi":"Tulcán", "Chimborazo":"Riobamba", "Cotopaxi":"Latacunga", "El Oro":"Machala", "Esmeraldas":"Esmeraldas", "Galápagos":"Puerto Baquerizo Moreno", "Guayas":"Guayaquil", "Imbabura":"Ibarra", "Loja":"Loja", "Los Ríos":"Babahoyo", "Manabí":"Portoviejo", "Morona Santiago":"Macas", "Napo":"Tena", "Orellana":"Coca", "Pastaza":"Puyo", "Pichincha":"Quito", "Santa Elena":"Santa Elena", "Santo Domingo de los Tsáchilas":"Santo Domingo", "Sucumbíos":"Nueva Loja", "Tungurahua":"Ambato", "Zamora Chinchipe":"Zamora"}

        prov_keys = dict.keys()
        provinces= []
        for element in prov_keys:
            provinces.append(element)

        random_province = random.choice(provinces)
        capital = dict.get(random_province)

        options = []
        options.append(capital)


        while len(options) < 4:
            rand_option = dict.get(random.choice(provinces))
            if rand_option not in options:
                options.append(rand_option)

        random.shuffle(options)

        print("¿Cuál es la capital de", random_province, "?")
        print("Opciones: ")
        for option in options:
            print(option)

        answer = input("Ingresa tu respuesta: ")
        if answer == capital:
            print("¡Muy bien!")
        else:
            print("Lo siento, es incorrecto :(")

        answer = input("¿Seguir jungando? (si o no)")
        if answer == "no":
            break

    if pregunta_escogida == "regiones":

    #Preguntas regiones

        dict = {"Azuay":"Sierra", "Bolívar":"Sierra", "Cañar":"Sierra", "Carchi":"Sierra", "Chimborazo":"Sierra", "Cotopaxi":"Sierra", "El Oro":"Costa", "Esmeraldas":"Costa", "Galápagos":"Insular", "Guayas":"Costa", "Imbabura":"Sierra", "Loja":"Sierra", "Los Ríos":"Costa", "Manabí":"Costa", "Morona Santiago":"Amazonía", "Napo":"Amazonía", "Orellana":"Amazonía", "Pastaza":"Amazonía", "Pichincha":"Sierra", "Santa Elena":"Costa", "Santo Domingo de los Tsáchilas":"Sierra", "Sucumbíos":"Amazonía", "Tungurahua":"Sierra", "Zamora Chinchipe":"Amazonía"}

        prov_keys = dict.keys()
        provinces= []
        for element in prov_keys:
            provinces.append(element)

        random_province = random.choice(provinces)
        region = dict.get(random_province)

        options = []
        options.append(region)


        while len(options) < 4:
            rand_option = dict.get(random.choice(provinces))
            if rand_option not in options:
                options.append(rand_option)

        random.shuffle(options)

        print("¿En qué región se encuentra la provincia de", random_province, "?")
        print("Opciones: ")
        for option in options:
            print(option)

        answer = input("Ingresa tu respuesta: ")
        if answer == region:
            print("¡Muy bien!")
        else:
            print("Lo siento, es incorrecto :(")

        answer = input("¿Seguir jungando? (si o no)")
        if answer == "no":
            break

    if pregunta_escogida == "puntos de interés":

    #Preguntas puntos de interés o eventos representativos

        dict = {"Azuay":"Parque Nacional Cajas", "Bolívar":"Carnaval de Guaranda", "Cañar":"Ruinas de Ingapirca", "Carchi":"Cementerio Municipal de Tulcán", "Chimborazo":"Volcán Chimborazo", "Cotopaxi":"Volcán Cotopaxi", "El Oro":"Archipiélago de Jambelí", "Esmeraldas":"Playa de Tonsupa", "Galápagos":"Bahía Tortuga", "Guayas":"Las Peñas", "Imbabura":"Laguna de Cuicocha", "Loja":"Parque Nacional Podocarpus", "Los Ríos":"La Casa de Olmedo", "Manabí":"Playa de los Frailes", "Morona Santiago":"Laguna Negra", "Napo":"Río Misahuallí", "Orellana":"Parque Nacional Yasuní", "Pastaza":"Ruta de los Shamanes", "Pichincha":"Centro histórico de Quito", "Santa Elena":"Punto rocoso de La Chocolatera", "Santo Domingo de los Tsáchilas":"Parque Zaracay", "Sucumbíos":"Reserva de Producción Faunística Cuyabeno", "Tungurahua":"Baños de Agua Santa", "Zamora Chinchipe":"Centinela del Cóndor"}

        prov_keys = dict.keys()
        provinces= []
        for element in prov_keys:
            provinces.append(element)

        random_province = random.choice(provinces)
        puntoint = dict.get(random_province)

        options = []
        options.append(puntoint)


        while len(options) < 4:
            rand_option = dict.get(random.choice(provinces))
            if rand_option not in options:
                options.append(rand_option)

        random.shuffle(options)

        print("¿Cuál de los siguientes es un punto de interés o un evento representativo de la provincia de", random_province, "?")
        print("Opciones: ")
        for option in options:
            print(option)

        answer = input("Ingresa tu respuesta: ")
        if answer == puntoint:
            print("¡Muy bien!")
        else:
            print("Lo siento, es incorrecto :(")

        answer = input("¿Seguir jungando? Si ya no quieres jugar, escribe no: ")
        if answer == "no":
            break
