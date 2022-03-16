class boat:

    def __init__(self, boat_size, boat_color, boat_type, boat_wheel ):
        self._boat_size = boat_size
        self._color = boat_color
        self._type = boat_type
        self._wheel = boat_wheel

    def wheel_turn_still(self):
        print(str.format('The steering wheel {0} is turning', self._wheel))

    @property
    def boat_size(self):
        return self._boat_size

    @boat_size.setter
    def boat_size(self, value):
        self._boat_size = value

    @property
    def boat_color(self):
        return self.boat_color

    @boat_color.setter
    def boat_color(self, value):
        self.boat_color = value

    @property
    def boat_type(self):
        return self.boat_type

    @boat_type.setter
    def boat_type(self, value):
        self.boat_type = value

    @property
    def boat_wheel(self):
        return self.boat_wheel

    @boat_wheel.setter
    def boat_wheel(self, value):
        self.boat_wheel = value

my_boat = boat(30, 'white', 'sailboat', 'helm')
print(my_boat.wheel_turn_still())



