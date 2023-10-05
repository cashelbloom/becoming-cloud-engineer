class Ship:
    def __init__(self, ship_name, port_anchored):
        self.ship_name = ship_name
        self.port_anchored = port_anchored

    def sail(self, port_of_destination):
        print(f'I am - {self.ship_name} - sailing to this port to anchor for some time: {port_of_destination}')

    def set_anchor(self, port_of_destination):
        print(f'I - {self.ship_name} have anchored here for next 5 days: {port_of_destination}')
        self.port_anchored =  port_of_destination