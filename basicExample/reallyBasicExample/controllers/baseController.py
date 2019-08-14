from abc import ABC, abstractmethod
from django.shortcuts import redirect

class BaseController(ABC):

    instance  = None

    @classmethod
    def getInstance(cls):
        if(cls.instance is None):
            cls.instance = BaseController()

        return cls.instance