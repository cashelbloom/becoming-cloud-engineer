from party import Party
from anthem import Anthem

class Candidate:
    def __init__(self, name, gender, age, party):
        self.name = name
        self.gender = gender
        self.age = age
        self.party = party

    def do_campaign(self):
        pass

    def make_promise(self):
        pass


dem_anthem = Anthem('dem"s anthem', 'Dems anthem lyrics')
dem_party = Party('Democrat', 'Donkey','blhablah', 'JB', dem_anthem)
my_dem_candidate = Candidate('John', 'Male', 40, dem_party)
my_dem_candidate.party.sing_party_anthem()
#
repub_anthem = Anthem('Republican"s anthem', 'Sing Republican anthem lyrics')
repub_party = Party('Republican', 'Elephant', 'hihihi', 'DT', repub_anthem)
my_republican_candidate = Candidate('Joe', 'Male', 30, repub_party)
my_republican_candidate.party.sing_party_anthem()