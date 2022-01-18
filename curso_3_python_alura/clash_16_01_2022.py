#CLASSE DOS CAMPEOES

class TheLastDance:

    def __init__(self, top, jg, mid, adc, sup, time):
        print("{} está sendo salvo em {}".format(time, self))
        self.top = top
        self.jg = jg
        self.mid = mid
        self.adc = adc
        self.sup = sup
        self.time = time
        print()

    def imprime_time(self):
        print("O time {} é composto por:".format(self.time))
        print("Top: {}".format(self.top))
        print("Jg: {}".format(self.jg))
        print("Mid: {}".format(self.mid))
        print("Adc: {}".format(self.adc))
        print("Sup: {}".format(self.sup))


#KMTS = TheLastDance("Nivboy", "Ninja", "KMT Yang", "Avery Lestrange", "Man ComPraPink", "The Last Dance")
#KMTS.imprime_time()

#Trotos = TheLastDance("Brunao", "Kenzao", "Sartz", "Caiao", "Enzao", "Trotos")
#Trotos.imprime_time()
#Trotos = None
#print(Trotos)
#Trotos.imprime_time()