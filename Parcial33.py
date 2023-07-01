class Hora():
    def __init__(self):
        self.h = 0
        self.m = 0
        self.s = 0

    def getH(self):
        return self.h

    def setH(self, h):
        self.h =h

    def getM(self):
        return self.m

    def setM(self, m):
        self.m = m

    def getS(self):
        return self.s

    def setS(self, s):
        self.s = s

    def validar(self):
        hora_valida = True
        if ( self.h < 0 or self.h > 23):
            hora_valida = False

        if ( self.m < 0 or self.m > 59):
            hora_valida = False

        if ( self.s < 0 or self.s > 59):
            hora_valida = False

        if not hora_valida:
            self.h = 0
            self.m = 0
            self.s = 0

    def aSegundos(self):
        return self.h * 60 * 60 + self.m * 60 + self.s

    def deSegundos(self, segundos):
        self.h = segundos // 3600
        self.m = ( segundos % 3600 ) // 60
        self.s = segundos - self.h * 3600 - self.m * 60


    def segundosDesde(self, hora):
        return abs( self.aSegundos() - hora.aSegundos() )

    def siguiente(self):
        # Paso a segundos y sumo 1, si el resultados ed 86400
        # la hora pasa a ser 00:00:00
        segundos = self.aSegundos()
        segundos += 1
        if segundos >= 86400:
            segundos = 0
        self.deSegundos(segundos)

    def anterior(self):
        # Paso a segundos y resto 1
        # en el caso que segundos sea 0, la hora
        # pasara a ser 23:59:59
        segundos = self.aSegundos()
        segundos -= 1
        if segundos <= 0:
            segundos = 86399
        self.deSegundos(segundos)

    def copia(self):
        h = Hora()
        h.setH(self.h)
        h.setM(self.m)
        h.setS(self.s)
        return h

    def __repr__(self):
        return "{:02d}hs. {:02d}ms. {:02d}s.".format(
            self.h,
            self.m,
            self.s
        )
