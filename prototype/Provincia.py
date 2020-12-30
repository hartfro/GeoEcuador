class Region():
    def __init__(self, nombre):
        self.nombre = nombre


class Provincia():
    def __init__(self, nombre, region, descripcion, capital, puntos_interes=[], bandera="", paisaje=""):
        self.nombre = nombre
        self.region = region
        self.descripcion = descripcion
        self.capital = capital
        self.puntos_interes = puntos_interes
        self.bandera = bandera
        self.paisaje = paisaje


def leer_descripcion(path):
    descripcion = ""
    with open(path, 'r', encoding='utf-8') as file:
        descripcion = file.read()

    return descripcion



def inicializar_provincias():
    sierra = Region("Sierra")
    costa = Region("Costa")
    amazonia = Region("Amazonía")
    galapagos = Region("Galápagos")

    lista_provincias = [
        ["Azuay", sierra, leer_descripcion("descripciones/provincias/azuay.txt"), "Cuenca", ["Parque Nacional Cajas"]],
        ["Bolívar", sierra, leer_descripcion("descripciones/provincias/bolivar.txt"), "Guaranda", ["Carnaval de Guaranda"]],
        ["Cañar", sierra, leer_descripcion("descripciones/provincias/canar.txt"), "Azogues", ["Ruinas de Ingapirca"]],
        ["Carchi", sierra, leer_descripcion("descripciones/provincias/carchi.txt"), "Tulcán", ["Cementerio Municipal de Tulcán",
                                                                                                "Reserva Bioantropológica Awa"]],
        ["Chimborazo", sierra, leer_descripcion("descripciones/provincias/chimborazo.txt"), "Riobamba", ["Volcán Chimborazo"]],
        ["Cotopaxi", sierra, leer_descripcion("descripciones/provincias/cotopaxi.txt"), "Latacunga", ["Volcán Cotopaxi"]],
        ["El Oro", costa, leer_descripcion("descripciones/provincias/el_oro.txt"), "Machala", ["Archipiélago de Jambelí"]],
        ["Esmeraldas", costa, leer_descripcion("descripciones/provincias/esmeraldas.txt"), "Esmeraldas", ["Esmeraldas"]],
        ["Galápagos", galapagos, leer_descripcion("descripciones/provincias/galapagos.txt"), "Puerto Baquerizo Moreno", ["Bahía Tortuga"]],
        ["Guayas", costa, leer_descripcion("descripciones/provincias/guayas.txt"), "Guayaquil", ["Las Peñas", "Malecón 2000"]],
        ["Imbabura", sierra, leer_descripcion("descripciones/provincias/imbabura.txt"), "Ibarra", ["Laguna de Cuicocha"]],
        ["Loja", sierra, leer_descripcion("descripciones/provincias/loja.txt"), "Loja", ["Parque Nacional Codocarpus"]],
        ["Los Ríos", costa, leer_descripcion("descripciones/provincias/los_rios.txt"), "Babahoyo", ["La Casa de Olmedo"]],
        ["Manabí", costa, leer_descripcion("descripciones/provincias/manabi.txt"), "Portoviejo", ["Playa de los Frailes"]],
        ["Morona Santiago", amazonia, leer_descripcion("descripciones/provincias/morona_santiago.txt"), "Macas", ["Laguna Negra"]],
        ["Napo", amazonia, leer_descripcion("descripciones/provincias/napo.txt"), "Tena", ["Río Misahuallí"]],
        ["Orellana", amazonia, leer_descripcion("descripciones/provincias/orellana.txt"), "Coca", ["Parque Nacional Yasuní"]],
        ["Pastaza", amazonia, leer_descripcion("descripciones/provincias/pastaza.txt"), "Puyo", ["Ruta de los Shamanes"]],
        ["Pichincha", sierra, leer_descripcion("descripciones/provincias/pichincha.txt"), "Pichincha", ["Centro Histórico de Quito"]],
        ["Santa Elena", costa, leer_descripcion("descripciones/provincias/santa_elena.txt"), "Santa Elena", ["Punto Rocoso de La Chocolatera"]],
        ["Santo Domingo de los Tsáchilas", sierra, leer_descripcion("descripciones/provincias/santo_domingo.txt"), "Santo Domingo", ["Parque Zaracay"]],
        ["Sucumbíos", amazonia, leer_descripcion("descripciones/provincias/sucumbios.txt"), "Nueva Loja", ["Reserva de Producción Faunística Cuyabeno"]],
        ["Tungurahua", sierra, leer_descripcion("descripciones/provincias/tungurahua.txt"), "Ambato", ["Baños de Agua Santa"]],
        ["Zamora Chinchipe", amazonia, leer_descripcion("descripciones/provincias/zamora_chinchipe.txt"), "Zamora", ["Centinela del Cóndor"]]
    ]

    provincias = {}
    
    for lista in lista_provincias:
        nombre = lista[0]
        region = lista[1]
        descripcion = lista[2]
        capital = lista[3]
        puntos_interes = lista[4]

        provincia = Provincia(nombre, region, descripcion, capital, puntos_interes)
        provincias[nombre] = provincia

    return provincias