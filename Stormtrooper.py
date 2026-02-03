class Stormtrooper:
    def __init__(self, name, tours, eliminations, awards):
        self.name = name
        self.tours = tours
        self.eliminations = eliminations
        self.awards = awards

    def top_stat(self):
        best = (None, 0)
        for attr in ["tours", "eliminations", "awards"]:
            #value = self.attr 
            #This won't work, as attr is not part of Stooormtroper 
            value = getattr(self, attr)
            if value > best[1]:
                best = (attr, value)
        return best




if __name__ == "__main__":
    tk109 = Stormtrooper("TK-109", 5, 200, 5)
    tr8r = Stormtrooper("TR-8R", 1, 3, 5)
    kyle_katarn = Stormtrooper("Kyle Katarn", 20, 10, 15)

    print(tr8r.top_stat())
    print(tk109.top_stat())
    print(kyle_katarn.top_stat())