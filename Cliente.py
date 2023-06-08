class Cliente:
    def __init__(self, idCliente, nombre, contacto, vehiculos=None, tickets=None, prioridad=None):
        self.__idCliente = idCliente
        self.__nombre = nombre
        self.__contacto = contacto
        self.__vehiculos = [] if vehiculos is None else vehiculos
        self.__tickets = [] if tickets is None else tickets
        self.__prioridad = prioridad

    # Getter para el atributo idCliente
    def get_idCliente(self):
        return self.__idCliente

    # Setter para el atributo idCliente
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente

    # Getter para el atributo nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para el atributo nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter para el atributo contacto
    def get_contacto(self):
        return self.__contacto

    # Setter para el atributo contacto
    def set_contacto(self, contacto):
        self.__contacto = contacto

    # Getter para el atributo vehiculos
    def get_vehiculos(self):
        return self.__vehiculos

    # Setter para el atributo vehiculos
    def set_vehiculos(self, vehiculos):
        self.__vehiculos = vehiculos

    # Getter para el atributo tickets
    def get_tickets(self):
        return self.__tickets

    # Setter para el atributo tickets
    def set_tickets(self, tickets):
        self.__tickets = tickets

    # Getter para el atributo prioridad
    def get_prioridad(self):
        return self.__prioridad

    # Setter para el atributo prioridad
    def set_prioridad(self, prioridad):
        self.__prioridad = prioridad
