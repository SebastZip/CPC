class Vehiculo:
    def __init__(self, idVehiculo, placa, ubicacion):
        self.__idVehiculo = idVehiculo
        self.__placa = placa
        self.__ubicacion = ubicacion

    # Getter para el atributo idVehiculo
    def get_idVehiculo(self):
        return self.__idVehiculo

    # Setter para el atributo idVehiculo
    def set_idVehiculo(self, idVehiculo):
        self.__idVehiculo = idVehiculo

    # Getter para el atributo placa
    def get_placa(self):
        return self.__placa

    # Setter para el atributo placa
    def set_placa(self, placa):
        self.__placa = placa

    # Getter para el atributo ubicacion
    def get_ubicacion(self):
        return self.__ubicacion

    # Setter para el atributo ubicacion
    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion
