# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
class Player():
    #Initializer
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
        
        if speed < 0 or speed > 1 or endurance < 0 or endurance > 1 or accuracy < 0 or accuracy > 1:
          raise ValueError("Waarde moet tussen 0 en 1 zijn.")
    
     #Method
    def introduce(self):
        print(f"Hello everyone, my name is {self.name}")

    def top_stat(self):
        best = (None, 0)
        for attr in ["speed", "endurance", "accuracy"]:
            value = getattr(self, attr)
            if value > best[1]:
                best = (attr, value)
        return best
    
    def sum_player(self):
        total = 0
        for attr in ["speed", "endurance", "accuracy"]:
            value = getattr(self, attr)
            total += value
        total = round(total,2)
        print(f"Opgeteld: {self.name} {total:.2f}")
        return total
    
    def compare_players(self, other, attr):
        for attr in ["speed", "endurance", "accuracy"]:

            self_value = getattr(self, attr)
            other_value = getattr(other, attr)

            if self_value > other_value:
                return self.name
            elif other_value > self_value:
                return other.name
            else:
                return "Tie"
      


    
class Commentator():
    #Initializer
    def __init__(self, name):
        self.name = name

Bob = Player('Bob', 0.4, 0.2, 0.6)
Alice = Player('Alice', 0.8, 0.2, 0.6)
print(Bob.top_stat())
Bob.introduce()
Bob.sum_player()
Ray = Commentator("Ray Hudson")
print (Ray.name)
print(Bob.compare_players(Alice, 'speed'))
print(Bob.compare_players(Alice, 'endurance'))
print(Alice.compare_players(Bob, 'accuracy'))