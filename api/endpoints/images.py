from flask_restplus import Resource, Namespace, reqparse
from flask_accepts import accepts, responds
from api.models.image import Image
from api.schemas.image_schema import ImageSchema


ns = Namespace('image', description="Operations related to images")

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, location='path')


@ns.route("/")
class ImageResource(Resource):

    @ns.expect(parser)
    @responds(schema=ImageSchema, api=ns, status_code=200)
    def get(self, **kwargs):
        return Image('test', 1000)

    @accepts(schema=ImageSchema, api=ns)
    @responds(schema=ImageSchema, api=ns, status_code=201)
    def post(self):
        return Image('test', 500)


@ns.route("s/")
class ImageListResource(Resource):

    @responds(schema=ImageSchema(many=True), api=ns, status_code=200)
    def get(self):
        return [Image('test', 1000)]
