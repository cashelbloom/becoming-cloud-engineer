from anthem import Anthem as ant

class Party:
    def __init__(self, name, symbol, manifesto, president, anthem):
        self.name = name
        self.symbol = symbol
        self.manifesto = manifesto
        self.president = president
        self.anthem = anthem

    def provide_funds(self):
        pass

    def enthuse_base(self):
        pass

    def select_candidates(self):
        pass

    def sing_party_anthem(self):
        self.anthem.play_anthem()

