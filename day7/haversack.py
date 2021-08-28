class Haversack():

    def __init__(self, colour):
        self.colour = colour
        self.contents = []

    def __len__(self):
        return len(self.contents)

    def add(self, othersack: 'Haversack'):
        self.contents.append(othersack)

    @property
    def counts(self):
        out = {}
        for sack in self.contents:
            if sack.colour not in out.keys():
                out[sack.colour] = 1
            else:
                out[sack.colour] += 1
        return out
