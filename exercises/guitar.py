class guitar:
    def __init__(self, body, bridge, neck, turning_keys):
        self._body = body
        self._bridge = bridge
        self._neck = neck
        self._keys = turning_keys

    def tuning_keys_turning(self):
        print(str.format('the keys are now {0} turning', self._keys))

    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, value):
        self._body = value

    @property
    def bridge(self):
        return self._bridge

    @bridge.setter
    def bridge(self, value):
        self._bridge = value

    @property
    def neck(self):
        return self._neck

    @neck.setter
    def neck(self, value):
        self._neck = value

    @property
    def turning_keys(self):
        return self._keys

    @turning_keys.setter
    def turning_keys(self, value):
        self._keys = value


my_guitar = guitar('solid', 'fixed', 'short', 'tuned')
print(my_guitar.tuning_keys_turning())
