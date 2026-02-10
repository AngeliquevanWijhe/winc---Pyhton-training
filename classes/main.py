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
        return(f"Hello everyone, my name is {self.name}.")

    def strength(self):
        best = (None, 0)
        for attr in ["speed", "endurance", "accuracy"]:
            value = getattr(self, attr)
            if value > best[1]:
                best = (attr, value)
        return best
    
class Commentator():
    #Initializer
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        total = 0
        for attr in ["speed", "endurance", "accuracy"]:
            value = getattr(player, attr)
            total += value
        total = round(total,2)
        print(f"Opgeteld: {player.name} {total:.2f}")
        return total
    
    def compare_players(self,player, other, attr):
        player_value = getattr(player, attr)
        other_value = getattr(other, attr)
        best = player.strength()
        totalP = self.sum_player(player)
        totalO = self.sum_player(other)


        if player_value > other_value:
            return player.name
        elif other_value > player_value:
            return other.name
        else:
            if best[1]>other.strength()[1]:
                return player.name
            elif other.strength()[1]>best[1]:
                return other.name
            else:
                if totalP>totalO:
                    return player.name
                elif totalO>totalP:
                    return other.name
                else:
                    return("These two players might as well be twins!")

      


    


bob = Player('Bob', 0.9, 0.2, 0.4)
alice = Player('Alice', 0.8, 0.2, 0.6)
print(bob.strength())
print(bob.introduce())
Ray = Commentator("Ray Hudson")
Ray.sum_player(bob)
print (Ray.name)
print(Ray.compare_players(bob, alice, 'speed'))
print(Ray.compare_players(bob, alice, 'endurance'))
print(Ray.compare_players(bob, alice, 'accuracy'))