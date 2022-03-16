class watch:
    def __init__(self, watch_material, watch_color, watch_crown, watch_face):
        self._material = watch_material
        self._color = watch_color
        self._crown = watch_crown
        self._face = watch_face

    def crown_adjust_autoadjust(self):
        print(str.format('time is now {} adjusted.', self._crown))

    @property
    def watch_material(self):
        return self._material

    @watch_material.setter
    def watch_material(self, value):
        self._material = value

    @property
    def watch_color(self):
        return self._color

    @watch_color.setter
    def watch_color(self, value):
        self._color = value

    @property
    def watch_face(self):
        return self._face

    @watch_face.setter
    def watch_face(self, value):
        self._face = value

    @property
    def watch_crown(self):
        return self._crown

    @watch_crown.setter
    def watch_crown(self, value):
        self._crown = value


mywatch = watch('leather', 'brown', 'automatically', 'digital')
print(mywatch.crown_adjust_autoadjust())

