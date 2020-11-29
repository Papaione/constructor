class Water:
    def __init__(self, volume, unit = "L"):
        self.volume = volume
        self.unit   = unit

    def __str__(self):
        return f"WATER({self.volume}{self.unit}) "

    def __len__(self):
        return self.volume
    
    def __add__(self, w):
        if self.unit == "ml" and w.unit == "L":
            self.volume = self.volume / 1000
            w.volume = w.volume * 1
        elif w.unit == "ml" and self.unit == "L":
            w.volume = w.volume / 1000
            self.volume = self.volume * 1
        elif self.unit and w.unit == "ml":
            w.volume = w.volume / 1000
            self.volume = self.volume / 1000
        return Water( self.volume + w.volume )

    def __sub__(self, w):
        return Water( self.volume - w.volume )

    def __gt__(self, w):
        if self.volume > w.volume:
            return Water

    def __lt__(self, w):
        if self.volume < w.volume:
            return Water
        
    def __eq__(self, w):
        if self.volume == w.volume:
            return Water
########################################
water1 = Water(6, "L")
water2 = Water(300, "ml")

water = water1 + water2
    
print(water1)
print(water2)
print(water)

if water1 > water2:
    print("first is more")
elif water1 < water2:
    print("second is more")
elif water1 == water2:
    print("EGAL")
#print(len(water1))