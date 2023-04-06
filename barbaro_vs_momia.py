import random

class Personaje ():
    '''Clase Personaje, que contiene los atributos nombre, vida, ataque y defensa con los metodos atacar y estar_vivo

    ARGS
    -nombre: nombre del personaje
    -vida: cantidad de vida del personaje
    -ataque: valor de ataque del personaje
    -defensa: valor de defensa del personaje
    '''
    def __init__(self, nombre = None, vida = None, ataque = None, defensa = None):
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa

    #funcion atacar, por cada valor de ataque=(x) que tenga el Pj, se tiraran los dados X veces
    #en cada tirada si el numero que sale es mayor a la mitad de la cantidad de valores de los dados
    #la ronda del ataque sera valida, en caso contrario, no lo sera
    def atacar(self, dado):
        damage = 0
        for i in range(self.__ataque):
            self.__x = dado.tirar()
            if self.__x >= (dado.cara_de_dado/2):
                damage += 1
        return damage

    #funcion que determina si la vida es mayor a 0 (en caso de serlo el pj esta vivo)
    def estar_vivo(self):
        if self.__vida > 0:
            return True
        else:
            return False

    #getter
    @property
    def nombre (self):
        return self.__nombre

    #setter
    @nombre.setter
    def nombre (self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    #getter
    @property
    def vida (self):
        return self.__vida

    #setter
    @vida.setter
    def vida (self, nueva_vida):
        self.__vida = nueva_vida

    #getter
    @property
    def ataque (self):
        return self.__ataque

    #setter
    @ataque.setter
    def ataque (self, nuevo_ataque):
        self.__ataque = nuevo_ataque

    #getter
    @property
    def defensa (self):
        return self.__defensa

    #setter
    @defensa.setter
    def defensa(self, nueva_defensa):
        self.__defensa = nueva_defensa

    def __str__(self):
        return '''Personaje
    -Nombre: {}
    -Vida: {}
    -Ataque: {}
    -Defensa: {}'''.format(self.__nombre, self.__vida, self.__ataque, self.__defensa)

class Momia (Personaje):
    '''Clase Momia, que contiene los atributos nombre, vida, ataque y defensa con los metodos atacar, defender y estar_vivo

    ARGS
    -nombre: nombre del personaje
    -vida: cantidad de vida del personaje
    -ataque: valor de ataque del personaje
    -defensa: valor de defensa del personaje
    '''
    def __init__(self,  nombre = None, vida = None,
                 ataque = None, defensa = None):
        super().__init__(nombre, vida, ataque, defensa)

    #metodo defender que recibe el numero de impactos recibidos, la defensa del pj y el dado
    #por cada valor de defensa tira el dado aleatoriamente y si alcanza el valor necesario
    #se genera 1 valor de defendido, al final el numero de impactos recibido se le resta el numero de defendido
    #en caso de el resultado ser positivo, lo retorna
    #en caso de ser 0 o negativo, retorna 0
    def defender (self, dado, num_impactos):
        defendido = 0
        for i in range(self.defensa):
            x = dado.tirar()
            if x == dado.cara_de_dado:
                defendido += 1
        damage_taken = (num_impactos - defendido)
        if damage_taken > 0:
            return damage_taken
        else:
            return 0


    def __str__(self):
        return super().__str__()

class Barbaro (Personaje):
    '''Clase Barbaro, que contiene los atributos nombre, vida, ataque y defensa con los metodos atacar, defender y estar_vivo

    ARGS
    -nombre: nombre del personaje
    -vida: cantidad de vida del personaje
    -ataque: valor de ataque del personaje
    -defensa: valor de defensa del personaje
    '''
    def __init__(self,  nombre = None, vida = None,
                 ataque = None, defensa = None):
        super().__init__(nombre, vida, ataque, defensa)

    #metodo defender que recibe el numero de impactos recibidos, la defensa del pj y el dado
    #por cada valor de defensa tira el dado aleatoriamente y si alcanza el valor necesario
    #se genera 1 valor de defendido, al final el numero de impactos recibido se le resta el numero de defendido
    #en caso de el resultado ser positivo, lo retorna
    #en caso de ser 0 o negativo, retorna 0
    def defender (self, dado, num_impactos):
        defendido = 0
        for i in range (self.defensa):
            x = dado.tirar()
            if x >= round(dado.cara_de_dado*.66):
                defendido += 1
        damage_taken = (num_impactos - defendido)
        if damage_taken > 0:
            return damage_taken
        else:
            return 0

    def __str__(self):
        return super().__str__()

class Dado():
    '''clase Dado, permite seleccion aleatoria entre numeros dados por usuario

    ARGS:
        -cara_de_dado: cantidad de de opciones a elegir
    FUNCIONES:
        -TIRAR: retorna seleccion aleatoria entera desde 1 hasta "cara_de_dado"
    '''
    def __init__(self, cara_de_dado):
        self.__cara_de_dado = cara_de_dado

    #funcion para seleccion aleatoria de 1 al 6
    def tirar (self):
        cara_mostrada = random.randrange(1, self.__cara_de_dado, 1)
        return cara_mostrada

    #getter
    @property
    def cara_de_dado(self):
        return self.__cara_de_dado

    #setter
    @cara_de_dado.setter
    def cara_de_dado(self, nuevas_caras):
        self.__cara_de_dado = nuevas_caras

    def __str__(self):
        return '''dado
    caras: {}'''.format(self.__cara_de_dado)

if __name__ == "__main__":

    dado = Dado(6)
    momia = Momia("Melisa", 10, 3,3)
    barbaro = Barbaro("Uthred", 10,3,3)

    rondas = int(input("cuantos turnos durara el combate?: "))
    ronda = 0

    while ronda < rondas and (momia.estar_vivo() == True and barbaro.estar_vivo() == True):


        print("Ronda: {}".format(ronda+1))

        if ronda % 2 == 0:
            print("ataca el Barbaro")
            ataque_barbaro = barbaro.atacar(dado)
            defensa_momia = momia.defender(dado, ataque_barbaro)

            if defensa_momia == 0:
                print("""la momia {} bloqueo totalmente el ataque y 
                queda con {} puntos de vida""".format(momia.nombre, momia.vida))
            else:
                print("""la momia {} no pudo bloquear {} impactos
                y queda con {} puntos de vida""".format(momia.nombre, defensa_momia, momia.vida))
            momia.vida -= defensa_momia
        else:
            print("ataca la Momia")
            ataque_momia = momia.atacar(dado)
            defensa_barbaro = barbaro.defender(dado, ataque_momia)

            if defensa_barbaro == 0:
                print("""el barbaro {} bloqueo totalmente el ataque y
                 queda con {} puntos de vida""".format(barbaro.nombre, barbaro.vida))
            else:
                print("""el barbaro {} no pudo bloquear {} impactos 
                y queda con {} puntos de vida""".format(barbaro.nombre, defensa_barbaro, barbaro.vida))
            barbaro.vida -= defensa_barbaro

        ronda += 1

    if barbaro.estar_vivo() == True and momia.estar_vivo() == True:
        print("""TABLAS
        -Barbaro {} tiene {} de vida
        -Momia {} tiene {} de vida""".format(barbaro.nombre, barbaro.vida, momia.nombre, momia.vida))

    elif barbaro.estar_vivo() == True and momia.estar_vivo() == False:
        print("""GANADOR BARBARO {}
        -Barbaro {} tiene {} de vida
        -Momia {} MUERTA""".format(barbaro.nombre, barbaro.nombre, barbaro.vida, momia.nombre))

    elif momia.estar_vivo() == True and barbaro.estar_vivo() == False:
        print("""GANADOR MOMIA {}
        -Momia {} tiene {} de vida
        -Barbaro {} MUERTO""".format(momia.nombre, momia.nombre, momia.vida, barbaro.nombre))