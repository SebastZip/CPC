class Reporte:
    def __init__(self, fecha, tickets):
        self.__fecha = fecha
        self.__tickets = tickets

    # Getter para el atributo fecha
    def get_fecha(self):
        return self.__fecha

    # Setter para el atributo fecha
    def set_fecha(self, fecha):
        self.__fecha = fecha

    # Getter para el atributo tickets
    def get_tickets(self):
        return self.__tickets

    # Setter para el atributo tickets
    def set_tickets(self, tickets):
        self.__tickets = tickets
 