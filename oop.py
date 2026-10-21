class Pastry:
    def __init__(self, typename):
        self.type = typename
        self.eatcount = 0
        self.bites = []
        self.seconds = None             # I added this after the video
       
    def eat(self):
        self.eatcount += 1
        prefix = ''
        if len(self.bites) > 0:
            prefix = ", ".join(self.bites) + ", "
        print(f"{prefix}ate the {self.type}, that makes {self.eatcount} times")

        if self.seconds:                # I added this after the video
            self.seconds.eat()          # I added this after the video

    def bite(self, noise):
        self.bites.append(noise)


c = Pastry("cannoli")
d = Pastry("danish")
e = Pastry("eclair")

d.bite("chomp")
d.bite("nom")
d.bite("chew")

d.eat()

d.seconds = e                           # I added this after the video

c.bite("slurp")

c.eat()
d.eat()