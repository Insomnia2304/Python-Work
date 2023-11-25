class Franchise:
  def __init__(self, name, address, menus):
    self.name = name
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "This is the {} located at {}!".format(self.name, self.address)
  def available_menus(self, time):
    # because 12am is actually 24 in 24h time-format
    if time[:-2] == "12":
      time = time.replace("p", "a", 1) if time[-2] == "p" else time.replace("a", "p", 1)
    currTime = (int)(time[:-2]) if time[-2] == "a" else ((int)(time[:-2])) + 12
    available = []
    for menu in self.menus:
      startHour = (int)(menu.start_time[:-2]) if menu.start_time[-2] == "a" else ((int)(menu.start_time[:-2])) + 12
      endHour = (int)(menu.end_time[:-2]) if menu.end_time[-2] == "a" else ((int)(menu.end_time[:-2])) + 12
      # print(startHour, endHour)
      if startHour <= currTime and currTime <= endHour:
        available.append(menu)
    return available

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    if hasattr(self, "name"):
      return "{name} menu available from {start_time} to {end_time}".format(name = self.name, start_time = self.start_time, end_time = self.end_time)
    else:
      return "menu not available"
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
       total += self.items[item]
    return total

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    string = self.name + " business with franchises at: "
    for franchise in self.franchises:
      string += franchise.name + ", "
    # without the last ", "
    return string[:-2]

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, "11am", "4pm")

early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, "3pm", "6pm")

dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, "5pm", "11pm")

kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, "11am", "9pm")

print(brunch.__repr__())
print(early_bird.__repr__())
print(dinner.__repr__())
print(kids.__repr__())

print(Menu.calculate_bill(brunch, ['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

all_menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("flagship store", "1232 West End Road", all_menus)
new_installment = Franchise("new_installment", "12 East Mulberry Street", all_menus)

print(flagship_store.__repr__())
print(new_installment.__repr__())

for menu in flagship_store.available_menus("12pm"):
  print(menu.name, end = " ")
print()
print(flagship_store.available_menus("5pm"))

Basta_Fazoolin = Business("Bastaa Fazoolin", [flagship_store, new_installment])

arepas_menu = Menu("Take a\' Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, "10am", "8pm")

arepas_place = Franchise("arepas rest", "189 Fitzgerald Avenue", [arepas_menu])

arepas_business = Business("Take a' Arepa", [arepas_place])
print(arepas_business.__repr__())
print(Basta_Fazoolin.__repr__())
