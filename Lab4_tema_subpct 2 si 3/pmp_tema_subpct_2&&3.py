import math 

def subpct2():
    alpha = -(15 * math.log(2.71828) / math.log(0.05))
    return alpha

        
def subpct3():
   
    t_mediu = math.log(1.6) / 7.5 * math.log(2.71828)
    convertire_t_mediu = t_mediu * 60 / 1
    print("rezulatatul la exercitiul 3 este ")
    print("timpul mediu ", t_mediu, ", minute ", convertire_t_mediu)


if __name__=="__main__":
    a=subpct2()
    print("rezultatul la subpct 2 este ",a)
    subpct3()

#La subpunctul 3 convertim alpha din minute in procent(cat la suta dintr-o ora inseamna),
#impartim la 100 si ne legam de faptul ca sunt 20 de clienti pe ora (distributia Poisson).
#Facem egalitatea intre formula distributiei exponentiale si cea a distributiei Poisson
#Necunoscuta in egalitate va fi x care va rezulta in procentul dintr-o ora a rezultatului pe care l convertim in minute
