#!/usr/bin/python3
"""BaseModel Class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    "Create the BaseMdel Class"
    def __init__(self, *args, **kwargs):
        """Initilize public instance attributes

            args(list): Empty list
            kwargs(dict): dictionary that
            contain key/value of the attirbutes
        """
        # **kwargs
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if not kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == '__class__':
                    continue
                setattr(self, key, value)
        models.storage.new(self)

    def save(self):
        """updates the public instance attribut
            update_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing
        all keys/values of the instance:"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = str(type(self).__name__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """Return Representation of the
            Ojbect [<class name>] (<self.id>) <self.__dict__>"""
        c = self.__dict__.copy()
        return "[{}] ({}) {}".format(type(self).__name__, self.id, c)
