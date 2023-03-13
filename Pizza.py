import csv
import datetime
class Pizza:
   def __init__(self, description, cost):
        self.description = description
        self.cost = cost
   def get_description(self):
        return self.description
   def get_cost(self):
        return self.cost
class Klasik(Pizza):
   cost=100.0
   def __init__(self):
        self.description = "KlasikPizza: Sucuk,Domates Sosu ve Salam."
        print(self.description + "\n")
class Margarita(Pizza):
    cost=115.50
    def __init__(self):
        self.description = "Margarita: Domates, Mozarella,Mantar ve Zeytin."
        print(self.description + "\n")
class TürkPizza(Pizza):
 cost = 102.0
 def __init__(self):
        self.description = "TürkPizza: Extra Kaşar,İnce Hamur, Soğan, Biber ve Sucuk"
        print(self.description + "\n")
class SadePizza (Pizza):
      cost = 108.50
      def get_cost(self):
        self.description = "SadaPizza: Kaşar,İnce Hamur ,Mısır ve Salam"
        print(self.description + "\n")
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
Pizza.get_cost(self)
    def get_description(self):
        return self.component.get_description() + \
            ' ' + Pizza.get_description(self)
class Zeytin(Decorator):
    cost = 3.9
    def _init_(self, topping):
        Decorator._init_(self, topping)
class Mantarlar(Decorator):
    cost = 3
    def _init_(self, topping):
        Decorator._init_(self, topping)
class KeçiPeyniri(Decorator):
    cost = 3.6
    def _init_(self, topping):
        Decorator._init_(self, topping)
class Et(Decorator):
    cost = 5
    def _init_(self, topping):
        Decorator._init_(self, topping)
class Soğan(Decorator):
    cost = 2.6
    def _init_(self, topping):
        Decorator._init_(self, topping)
class Mısır(Decorator):
    cost = 2.7
    def _init_(self, topping):
        Decorator._init_(self, topping)
def main():
    with open("Menu.txt") as mus_menu:
        for i in mus_menu:
            print(i, end="")
    class_dict = {1: Klasik,
                  2: Margarita,
                  3: TürkPizza,
                  4: SadePizza,
                  5: Zeytin,
                  6: Mantarlar,
                  7: KeçiPeyniri,
                  8: Et,
                  9: Soğan,
                  10:Mısır}
    request = input("Lütfen,istediğiniz pizza çeşidini seçin: ")
    while request not in ["1", "2", "3", "4"]:
        request = input("sadece 1 ile 4 arasındaki seçeneklerimiz mevcuttur. ")
    order = class_dict[int(request)]()
    while request != "#":
        request = input(("Ek malzeme için bir isteğiniz var mı ? İstediğiniz bir malzeme yoksa siparişi sonlandırmak için # basın : "))
        if request in ["5", "6", "7", "8", "9", "10"]:
            order = class_dict[int(request)](order)
            print("istediğiniz numara kullanılmamaktadır.")
    print("\n Aldığınız Pizza: " + order.get_description().strip() + "\n Fiyatı: "+str(order.get_cost()) +";"" TL'dir")
    isim = input("Adınızı giriniz: ")
    ID = input("Kimlik numaranızı giriniz: ")
    kredi_kartı= input("Kredi Kartı numaranızı giriniz: ")
    kredi_kartı_numarası = input("Kredi kartı şifrenizi giriniz ")
    kredi_kartı_numarası = datetime.datetime.now()
    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([isim, ID, kredi_kartı, kredi_kartı_numarası, order.get_description(), kredi_kartı_numarası])        
if __name__ == "__main__":
  main() 
