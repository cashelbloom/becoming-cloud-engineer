from voter import Voter

class MaleVoter(Voter):
    def __init__(self, *, id, name, constituency, dob, gender ):
        super().__init__(id=id, name=name, constituency=constituency, dob=dob)
        self.gender = gender


    def __str__(self):
        super_str = super().__str__()
        return super_str +  f' and the gender is: {self.gender}'

male_voter = MaleVoter(id=2, name='Rama', constituency='Ayodhya', dob='unknown', gender='God')
print(male_voter)