class Student:


    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list) or not all(
                isinstance(s, str) for s in attrs):
            return self.__dict__
        dictionary = {}
        for elements in attrs:
            try:
                dictionary[elements] = self.__dict__[elements]
            except:
                pass
        return dictionary
