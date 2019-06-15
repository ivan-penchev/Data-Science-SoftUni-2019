import jsonpickle
import json
class Car(object):
    def __init__(self):
        self._id = None
        self._price = None
        self._name = None
        self._car_data = None
        self._car_extra_data = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @id.deleter
    def id(self):
        del self._id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def car_data(self):
        return self._car_data

    @car_data.setter
    def car_data(self, value):
        self._car_data = value

    @car_data.deleter
    def car_data(self):
        del self._car_data

    @property
    def car_extra_data(self):
        return self._car_extra_data

    @car_extra_data.setter
    def car_extra_data(self, value):
        self._car_extra_data = value

    @car_extra_data.deleter
    def car_extra_data(self):
        del self._car_extra_data

    def toJSON(self):
        jsonpickle.set_preferred_backend('json')
        jsonpickle.set_encoder_options('json', ensure_ascii=False)
        return jsonpickle.encode(self)
