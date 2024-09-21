import datetime

class Fecha:
    def __init__(self,dia,mes,ano,horas=None,minutos=None,segundos=None):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.hor = horas
        self.min = minutos
        self.seg = segundos

    def imprimirFecha(self):
        if self.hor:
            print(self.dia,'/',self.mes,'/',self.ano,':',self.hor,'h',self.min,"'",self.seg,'"')
        else:
            print(self.dia,'/',self.mes,'/',self.ano)

    def getFechaSTR(self):
        if self.hor:
            return str(self.dia)+'/'+str(self.mes)+'/'+str(self.ano)+':'+str(self.hor)+':'+str(self.min)+':'+str(self.seg)
        else:
            return str(self.dia)+'/'+str(self.mes)+'/'+str(self.ano)
    def setFecha(self,dia,mes,ano,horas=None,minutos=None,segundos=None):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.hor = horas
        self.min = minutos
        self.seg = segundos

    def computarEdad(self):
#         print(datetime.date.today().day,datetime.date.today().month,datetime.date.today().year)
        if datetime.date.today().month < self.mes and datetime.date.today().day < self.dia:
            return(datetime.date.today().year - self.ano -1)
        elif datetime.date.today().month == self.mes and datetime.date.today().day < self.dia:
            return(datetime.date.today().year - self.ano -1)
        else:
            return (datetime.date.today().year - self.ano )


#### verificación ####
# fecha = Fecha(29,12,1989)
# # print(fecha.getFecha())
# fecha.imprimirFecha()
# print(fecha.computaEdad(),"anos")
print('<< Fecha is ok! >>')