class horse:
    def __init__(self, horse_size, horse_color, horse_tail, horse_galloping):
        self._size = horse_size
        self._color = horse_color
        self._tail = horse_tail
        self._galloping = horse_galloping

    def horse_gallop_walk(self):
        print(str.format('The horse is now {0} walking', self.horse_gallop_walk))

    @property
    def horse_size(self):
        return self._size

    @horse_size.setter
    def horse_size(self, value):
        self._size = value

    @property
    def horse_color(self):
        return self._color

    @horse_color.setter
    def horse_color(self, value):
        self._color = value

    @property
    def horse_tail(self):
        return self._tail

    @horse_tail.setter
    def horse_tail(self, value):
        self._tail = value

    @property
    def horse_galloping(self):
        return self._galloping

    @horse_galloping.setter
    def horse_galloping(self, value):
        self._galloping = value


my_horse = horse('tall', 'light brown', 'long', 'running')
print(my_horse.horse_gallop_walk())

