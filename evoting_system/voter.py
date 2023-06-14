class Voter:
    def __init__(self, *, id, name, dob, constituency):
        self.id = id
        self.name = name
        self.constituency = constituency
        self.dob = dob

    def __str__(self):
        return f'Vote ID is: {self.id}, name: {self.name} is from the constituency: {self.constituency} ' \
               f'and dob is: {self.dob}'


new_voter = Voter(id=1, constituency='Sivaganga', name='Ganesan Perumal', dob='01/01/1970')
print(f'Then new voter added is: {new_voter}')