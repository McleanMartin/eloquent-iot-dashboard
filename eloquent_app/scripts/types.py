import strawberry
from typing import List
import strawberry.django
from strawberry import auto
from eloquent_app.models.devices import *


@strawberry.django.type(Device)
class Device():
    name:str
    api_key:str
    remote_address:str
