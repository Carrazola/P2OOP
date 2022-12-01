import datetime




class carro():
    def __init__(self, marca="SUV") -> None:
        self.marca= marca
        pass
    pass



class Usuario():
    def __init__(self, nombre="Andres", edad=20) -> None:
            self.nombre= nombre
            self.edad= edad
            self.pago=0
            pass

    pass

    



class Espacio():
    today = datetime.datetime.today 
    posicion = 1
    marca1= "compacto"
    marca2= "SUV"
    marca3= "Van"


    def __init__(self, marca="SUV") -> None:
        self.disponible = True
        self.marca = marca
        self.posicion = Espacio.posicion
        Espacio.posicion = Espacio.posicion +1
        
        pass

    

    
    def reservar(self, fechainicial=datetime, fechafinal=datetime, usuario=Usuario):
        self.disponible = False
        self.fechafinal = fechafinal
        self.fechainicial = fechainicial
        self.usuarioDebe = usuario
    pass


    def liberar(self, usuario=Usuario):
            
            tiempo= self.fechafinal -self.fechainicial
            self.disponible = True
            tiemposec = tiempo.seconds//3600
            if(self.marca=="Compacto"):
                
                usuario.pago = tiemposec *5000
                print( "debe pagar" + str(usuario.pago))


            elif(self.marca=="SUV"):
                
                usuario.pago = tiemposec *6000
                print( "debe pagar" + str(usuario.pago))

            elif(self.marca=="Van"):
                
                usuario.pago = tiemposec *7000
                print( "debe pagar" + str(usuario.pago))
        

    pass


    def reservadiasiguiente(self, today=datetime, usuario= Usuario):
            self.disponible= False
            self.fechainicial= today
            self.fechafinal = today + datetime.timedelta(days = 1)
            pass



usuario1 = Usuario("andres", 20)



Espacio1 = Espacio("SUV")
fechainicial = datetime.datetime(2022, 11, 30, 10, 59, 11)
fechareserva = datetime.datetime(2022, 11, 30, 20, 59, 11)
tiempo= fechareserva-fechainicial
print(tiempo)
tiemposec = tiempo.seconds//3600
print(tiemposec)

Espacio1.reservar(fechainicial, fechareserva, usuario1)
print(Espacio1.disponible)
print(Espacio1.posicion)
Espacio1.liberar(usuario1)
print(usuario1.pago)

Espacio2 = Espacio("Compacto")
print(Espacio2.posicion)

today = datetime.datetime.today()
print(today)
tomorrow = today + datetime.timedelta(days = 1)
print(tomorrow)




Espacio1.reservadiasiguiente(today, usuario1)
print(Espacio1.fechainicial)
print(Espacio1.fechafinal)

