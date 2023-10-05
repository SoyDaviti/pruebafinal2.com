class Autos:
    def __init__(self, modelo_auto, anio_auto, precio_auto, auto_detalle):
        self.modelo_auto = modelo_auto
        self.anio_auto = anio_auto
        self.precio_auto = precio_auto
        self.auto_detalle = auto_detalle

    def toDBCollection(self):
        return{
            'modelo_auto':self.modelo,
            'anio_auto': self.anio_auto,
            'precio_auto': self.precio_auto,
            'auto_detalle': self.auto_detalle
        }
