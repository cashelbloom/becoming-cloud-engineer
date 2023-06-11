class Anthem:
    def __init__(self,party_name, lyrics):
        self.party_name = party_name
        self.lyrics = lyrics

    def play_anthem(self):
        print(f'{self.party_name} lyrics is {self.lyrics}')