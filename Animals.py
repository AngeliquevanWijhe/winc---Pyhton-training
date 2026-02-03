class Tiger():

  def attack(self):
    return 'Bwam!'

  def noise(self):
    return 'RAAAWR'


class Fly():

  def attack(self):
    return 'Bwam!'

  def noise(self):
    return ''


class Snake():

  def attack(self):
    return 'Bwam!'

  def noise(self):
    return 'Hissssss'


class Bear():

  def attack(self):
    return 'Bwam!'

  def noise(self):
    return 'RAAAWR'


baloo = Bear()
print(baloo.attack())
# 'Bwam!'

class Animal():

  def attack(self):
    return 'Bwam!'


class Tiger(Animal):

  def noise(self):
    return 'RAAAWR'


class Fly(Animal):

  def noise(self):
    return ''


class Snake(Animal):

  def noise(self):
    return 'Hissssss'


class Bear(Animal):

  def noise(self):
    return 'RAAAWR'


baloo = Bear()
print(baloo.noise())
# 'Bwam!'
