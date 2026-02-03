wanted_droids = [
  {"name":"C3PO", "type":"astromechanic"},
  {"name": "R2D2", "type": "astromechanic"}
]


#write your code here:
class Droids():
  def __init__(self, name, type):
    self.name = name
    self.type = type

  def comparison(self):
    names_wanted=[droid["name"]for droid in wanted_droids]
    if self.name in names_wanted :
        print(f'This is {self.name}, this droid is wanted') 
    else:
        print(f'This is {self.name}, this droid is not wanted')
 
        
      
#Check if your code works with this:
Droid1 = Droids('R2D2', 'astromechanic')
Droid2 = Droids('C3PO', 'Interpreter')
Droid3 = Droids('IG88', 'Assasin')

Droid1.comparison()
Droid3.comparison()
Droid2.comparison()