from classes.Developer import Developer
from classes.Dom import Dom
from classes.Mieszkanie import Mieszkanie
from classes.Zamowienie import Zamowienie

deweloper = Developer("Pol-Dev", "1980", "Katowice", 10)
dom = Dom("100a", "Zielona 20, Katowice", 100, 2000)
mieszkanie = Mieszkanie("213cc", "Brązowa 30, Katowice", 50, 2500, "10a")
zamowienie = Zamowienie("2021-10-01/100/dfdfd", "213cc", 50, 2500)

print(zamowienie)
