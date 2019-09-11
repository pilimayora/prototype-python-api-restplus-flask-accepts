import marshmallow as ma
from api.schemas.base_schema import BaseSchema


class ImageSchema(BaseSchema):
    __envelope__ = {"single": "image", "many": "images"}

    id = ma.fields.Int()
    name = ma.fields.Str()
    width = ma.fields.Int()
