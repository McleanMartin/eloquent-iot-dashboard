import strawberry
from .types import Device

@strawberry.type
class Query:
    devices: list[Device] = strawberry.django.field()

schema = strawberry.Schema(
    query=Query,
)