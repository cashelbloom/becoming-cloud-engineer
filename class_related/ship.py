class Ship:
    def __init__(self, port_anchored):
        self.port_anchored = port_anchored

    def sail(self, port_of_destination):
        print(f'I am sailing to this port to anchor for some time: {port_of_destination}')

    def set_anchor(self, port_of_destination):
        print(f'I have anchored here for next 5 days: {port_of_destination}')

my_ship = Ship('Chennai')
my_ship.sail('Vizag')
my_ship.set_anchor('Vizag')